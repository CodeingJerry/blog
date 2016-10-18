from models.blog import Blog
from models.tag import Tag
from routes import *
from routes.user import admin_required, current_user
from util.upload import upload
from models import db
import math

main = Blueprint('blog', __name__)

Model = Blog
PER_PAGE = 3


@main.route('/', defaults={'page':1})
@main.route('/page/<int:page>')
def index(page):
    # ms = Model.query.all()
    pagination = Model.query.order_by(Blog.created_time.desc()).paginate(page, PER_PAGE, False)
    total = pagination.total/PER_PAGE
    total = int(math.ceil(total))
    ts = Tag.query.all()
    if current_user():
        u = current_user()
        uid = u.id
    else:
        uid = 0
    return render_template('blog_index.html', pagination=pagination, total=total, tag_list=ts, uid=uid)


@main.route('/new')
@admin_required
def new():
    ts = Tag.query.all()
    return render_template('blog_new.html', tag_list=ts)


@main.route('/<int:id>')
def show(id):
    m = Model.query.get(id)
    ts = Tag.query.all()
    if current_user():
        u = current_user()
        uid = u.id
    else:
        uid = 0
    return render_template('blog.html', blog=m, tag_list=ts, uid=uid)


@main.route('/edit/<id>')
@admin_required
def edit(id):
    b = Model.query.get(id)
    ts = Tag.query.all()
    return render_template('blog_edit.html', blog=b, tag_list=ts)


@main.route('/pic/<id>')
@admin_required
def edit_pic(id):
    b = Model.query.get(id)
    return render_template('blog_edit_pic.html', id=b.id)


@main.route('/editpic/<id>', methods=['POST'])
def change_pic(id):
    if not upload():
        flash(u"请上传结尾为'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'的文件")
    filename = upload()
    print('debug filename, ', filename)
    b = Model.query.get(id)
    b.picture = r'http://res.myform.com/' + filename
    b.save()
    return redirect(url_for('.show',id=id))


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    m = Model(form)
    m.user_id = current_user().id
    m.tag_id = int(form.get('tag_id'))
    # m.tag_id = Tag.query.filter_by(name=tag).first()
    m.save()
    return redirect(url_for('blog.show', id=m.id))


@main.route('/update/<int:id>', methods=['POST'])
def update(id):
    form = request.form
    t = Model.query.get(id)
    t.update(form)
    return redirect(url_for('blog.show', id=id))


@main.route('/delete/<int:id>')
def delete(id):
    t = Model.query.get(id)
    t.delete()
    return redirect(url_for('blog.show', id=id))
