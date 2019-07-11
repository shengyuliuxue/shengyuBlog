#_*_ coding: utf-8 _*_
"""
    :author: Sheng Yu
    :copyright: © 2019 Sheng Yu <594549026@qq.com>
    :license: MIT, see LICENSE for more details
    :date: 2019-07-11
"""

from flask import Flask
from blog.extensions import db



def create_app():
    app = Flask(__name__)
    #app 未完成，如何调用其他方法？
    #app 可以作为参数，让别的方法调用它
    app.config.from_object(settings.config)
    register_extension(app)
    return app

def register_extension(app):
    db.init_app(app)







