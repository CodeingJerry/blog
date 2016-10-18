from models.user import User
# from models.topic import Topic
from routes import *
from flask import request, redirect, url_for
# for decorators
from functools import wraps
from util.upload import upload


main = Blueprint('user', __name__)

Model = User


def current_user():
    uid = session.get('uid')
    if uid is not None:
        u = User.query.get(uid)
        return u


def admin_required(f):
    @wraps(f)
    def function(*args, **kwargs):
        # your code
        print('admin required')
        u = current_user()
        uid = u.id
        # if request.args.get('uid') != '1':
        if uid != 1:
            print('not admin')
            abort(404)
        return f(*args, **kwargs)
    return function


@main.route('/')
def index():
    # ms = Model.query.all()
    return render_template('auth_index.html')


@main.route('/show/<int:id>')
def show(id):
    m = Model.query.get(id)
    return render_template('auth_show.html', user=m)


@main.route('/login', methods=['POST'])
def login():
    form = request.form
    u = User(form)
    user = Model.query.filter_by(username=u.username).first()
    if u.valid_login(user):
        session.permanent = True
        session['uid'] = user.id
        return redirect('/')
    else:
        return redirect(url_for('.index'))


@main.route('/logout')
def logout():
    # remove the uid from the session if it's there
    session.pop('uid', None)
    return redirect(url_for('user.index'))


@main.route('/register', methods=['POST'])
def register():
    form = request.form
    u = User(form)
    if u.valid():
        u.save()
        session.permanent = True
        session['uid'] = u.id
        return redirect('/user')
    else:
        return redirect(url_for('.index'))


@main.route('/avatar')
def cgavatar():
    return render_template('change_avatar.html')


@main.route('/edit-avatar', methods=['POST'])
def change_avatar():
    if not upload():
        flash(u"请上传结尾为'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'的文件")
    filename = upload()
    u = current_user()
    u.avatar = r'http://res.myform.com/' + filename
    u.save()
    flash(u'头像修改成功')
    return redirect(url_for('.show',id=u.id))