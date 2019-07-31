#_*_ coding: utf-8 _*_
"""
    :author: Sheng Yu
    :copyright: © 2019 Sheng Yu <594549026@qq.com>
    :license: MIT, see LICENSE for more details
    :date: 2019-07-11
"""
import os
from flask import Flask
from flask import render_template

def create_app(config=None):

    app = Flask(__name__,instance_relative_config=True)

    app.config.from_mapping(
        SECRECT_KEY='shengyu',
        DATABASE=os.path.join(app.instance_path, 'blog.sqlite'),
    )
    if config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import posts
    app.register_blueprint(posts.bp)
    return app










