from flask import Blueprint, request, render_template
from .model import Post

posts_bp = Blueprint('posts', __name__, template_folder='templates')

@posts_bp.route('/')
def list():
    # the following code was a test to see if we could use utilites > it worked
    # The Post class uses datetime_local to create a text version of the local time
    # When the variable date_created or date_modified is not provided > datetime_local provides the date
    p = Post(id=1, parent_id=0, text="This is my first post. I hope you like it.",
             date_created='2024-03-25 16:05')
    print(p.__dict__)
    # This code ^^^^^^ can be deleted

    user = {'is_is_authenticated': True}
    site_data = { 'title': 'Northside Chapel: Posts'}
    return render_template('display.html', data=site_data, current_user=user)

@posts_bp.route('/edit/<int:post_id>/<int:parent_id>', methods=['GET', 'POST'])
def edit(post_id, parent_id):
    if request.method == 'GET':
        return f"display edit post#{post_id} & parent id#{parent_id}"
    
    return 'IS A POST REQUEST'

@posts_bp.route('/add_new', methods=['GET', 'POST'])
def add_new():
    """
    """
    if request.method == 'POST':
        post = Post()
        text = request.form.get('text')
        post.parent_id = request.form.get('parent_id')
        post.add_new()

