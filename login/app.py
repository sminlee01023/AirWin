import os #절대경로를 지정하기 위한 Os모듈 임포트
from flask import Flask
from flask import request #회원정보 제출했을때 받아오기 위한 request, post요청을 활성화시키기 위함
from flask import redirect   #페이지 이동시키는 함수
from flask import render_template
from models import db
from models import Fcuser 
from flask import session 
from flask_wtf.csrf import CSRFProtect
from forms import RegisterForm, LoginForm

app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])  #겟, 포스트 메소드 둘다 사용
def register():   #get 요청 단순히 페이지 표시 post요청 회원가입-등록을 눌렀을때 정보 가져오는것
    if request.method == 'GET':
        return render_template("register.html")
    else:
        #회원정보 생성
        userid = request.form.get('userid') 
        username = request.form.get('username')
        password = request.form.get('password')
            
        print(userid,password)  #콘솔창에 ID, PW 출력 (확인용, 딱히 필요없음)
        
        if not (userid and username and password) :
            return "모두 입력해주세요"
        else:
            fcuser = Fcuser()
            fcuser.password = password           #models의 FCuser 클래스를 이용해 db에 입력한다.
            fcuser.userid = userid
            fcuser.username = username 
            db.session.add(fcuser)  # id, name 변수에 넣은 회원정보 DB에 저장
            db.session.commit()  #커밋
            return "Log-in" #post요청일시는 '/'주소로 이동. (회원가입 완료시 화면이동)
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET','POST'])  
def login():  
    form = LoginForm() #로그인 폼 생성
    if form.validate_on_submit(): #유효성 검사
        session['userid'] = form.data.get('userid') #form에서 가져온 userid를 session에 저장

        return redirect('/') #로그인에 성공하면 홈화면으로 redirect
            
    return render_template('login.html', form=form)

@app.route('/')
def hello():
    userid = session.get('userid', None)
    return render_template('hello.html',userid=userid)    # 이번 포스팅에는 필요없음(지난포스팅꺼)

if __name__ == "__main__":
    basedir = os.path.abspath(os.path.dirname(__file__)) #db파일을 절대경로로 생성
    dbfile = os.path.join(basedir, 'db.sqlite')#db파일을 절대경로로 생성

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + dbfile   
#sqlite를 사용함. (만약 mysql을 사용한다면, id password 등... 더 필요한게많다.)
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True 
#사용자 요청의 끝마다 커밋(데이터베이스에 저장,수정,삭제등의 동작을 쌓아놨던 것들의 실행명령)을 한다.
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
#수정사항에 대한 track을 하지 않는다. True로 한다면 warning 메시지유발
    app.config['SECRET_KEY'] = 'wcsfeufhwiquehfdx'

    csrf = CSRFProtect()
    csrf.init_app(app)

    db.init_app(app)
    db.app = app
    db.create_all()  #db 생성


    
    app.run(host='127.0.0.1', port=5000, debug=True) 
     #포트번호는 기본 5000, 개발단계에서는 debug는 True


@app.route('/logout',methods=['GET'])
def logout():
    session.pop('userid',None)
    return redirect('/')