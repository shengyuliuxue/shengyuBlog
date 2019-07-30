#_*_ coding: utf-8 _*_
"""
    :author: Sheng Yu
    :copyright: © 2019 Sheng Yu <594549026@qq.com>
    :license: MIT, see LICENSE for more details
    :date: 2019-07-11
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('links.html')








