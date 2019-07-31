import functools

from flask import (
    Blueprint,flash,g,redirect,render_template,request,session,url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from shengyuBlog.db import get_db

bp = Blueprint('posts', __name__, url_prefix='/posts')

@bp.route('/postid',methods=('GET','post'))
    def postid():
        return render_template('links.html')