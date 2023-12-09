from flask import Flask
from .lib.core import (
    include, layout, macro,
    css, img, js
)



app = Flask(__name__)
app.jinja_env.globals.update({
    'inc': include, 'layout': layout, 'macro': macro,
    'css': css, 'img': img, 'js': js
})
app.secret_key = 'Dev.: David Santana <github.com/davidsantana06>'


from .views import *
