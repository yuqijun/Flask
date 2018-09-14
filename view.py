from App import app,db
from flask import session,redirect,render_template,request,url_for,flash
from App.migreat import User,Question,Answer
from functools import wraps


def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if session.get('user_telephone'):
            return func(*args,**kwargs)
        return redirect(url_for('login'))
    return wrapper




@app.route('/')
def index():
    content = {
        'questions': Question.query.all()
    }
    return render_template('index.html',**content)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        username = request.form.get('username')
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            flash('该账号已存在，请输入其他账号')
            return render_template('register.html')
        else:
            if password != password2:
                flash('两次输入的密码不一致请重新输入')
                return render_template('register.html')
            else:
                user = User(username=username, telephone=telephone, password=password, )
                db.session.add(user)
                db.session.commit()
                # 并且跳转到登录页面
                return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    # 登录页面如果为GET请求
    if request.method == "GET":
        # 则展现登录页面
        return render_template('login.html')
    # 如果登录页面为POST请求
    else:
        telephone = request.form.get('telephone')
        password = request.form.get('password')
        user = User.query.filter(User.telephone == telephone, User.password == password).first()
        if user:
            session['user_telephone'] = user.telephone
            session.permanent = True
            return redirect(url_for('index'))
        else:
            flash('请输入正确的帐号密码，如未注册请先注册帐号密码!')
            return render_template('login.html')


@app.route('/loginout/')
def login_out():
    session.clear()
    return redirect(url_for('login'))


@app.route('/question/',methods=['GET','POST'])
def question_():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        caption = request.form.get('caption')
        content = request.form.get('content')
        question = Question(caption=caption,content=content)
        user_telephone = session.get('user_telephone')
        user = User.query.filter(User.telephone == user_telephone).first()
        question.author = user
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/detail/<question_id>')
def detail(question_id):
    question_modle = Question.query.filter(Question.message_id==question_id).first()
    return render_template('detail.html',question=question_modle)


@app.route('/add_answer/',methods=['POST'])
def add_answer():
    content = request.form.get('answer-content')
    question_id = request.form.get('question_id')
    answer = Answer(content=content)
    user_telephone = session['user_telephone']
    user = User.query.filter(User.telephone == user_telephone).first()
    answer.user = user
    question = Question.query.filter(Question.message_id==question_id).first()
    answer.question = question
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for("detail",question_id=question_id))


@app.context_processor
def my_context_processor():
    user_telephone = session.get('user_telephone')
    if user_telephone:
        user = User.query.filter(User.telephone == user_telephone).first()
        if user:
            return {'user': user}
    else:
        return{}