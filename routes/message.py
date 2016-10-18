from models.message import Message
from models.blog import Blog
from models.comment import Comment
from routes import *
from routes.user import admin_required, current_user


main = Blueprint('message', __name__)

Model = Message


@main.route('/cmsg')
def send_c_msg(cu, u, blog_id):
    m = Model()
    b = Blog.query.get(blog_id)
    m.message = cu.username + '评论了您的文章' + b.title
    m.user_id = u.id
    m.blog_id = blog_id
    m.save()
    print('debug m,', m, m.message, m.status)
    return 'OK'


@main.route('/rmsg')
def send_r_msg(cu, u, comment_id, blog_id):
    m = Model()
    c = Comment.query.get(comment_id)
    m.message = cu.username + '回复了您的评论' + c.content
    m.user_id = u.id
    m.blog_id = blog_id
    m.save()
    print('debug m,', m, m.message, m.status)
    return 'OK'


@main.route('/show/<int:user_id>')
def show(user_id):
    u = current_user()
    msgs = Message.query.filter_by(status=0,user_id=u.id).all()
    return render_template('msgs.html', msgs=msgs)