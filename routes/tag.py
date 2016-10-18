from models.tag import Tag
from models.blog import Blog
from routes import *
from routes.user import admin_required, current_user


main = Blueprint('tag', __name__)

Model = Tag


@main.route('/')
def index():
    ms = Model.query.all()
    u = current_user()
    return render_template('tag_index.html', tag_list=ms, uid = u.id)


@main.route('/new')
@admin_required
def new():
    return render_template('tag_new.html')


@main.route('/<int:id>')
def show(id):
    print('show tag, ', id, type(id))
    m = Model.query.get(id)
    t = Model.query.all()
    print(id, m)
    return render_template('tag.html', tag=m, tag_list=t)


@main.route('/edit/<id>')
@admin_required
def edit(id):
    t = Model.query.get(id)
    return render_template('tag_edit.html', tag=t)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    m = Model(form)
    m.save()
    return redirect(url_for('.index'))


@main.route('/update/<int:id>', methods=['POST'])
def update(id):
    form = request.form
    t = Model.query.get(id)
    t.update(form)
    return redirect(url_for('.index'))


@main.route('/delete/<int:id>')
@admin_required
def delete(id):
    t = Model.query.get(id)
    t.delete()
    return redirect(url_for('.index'))
