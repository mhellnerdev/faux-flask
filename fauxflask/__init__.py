from flask import Flask


app = Flask(__name__)


from fauxflask import views
from fauxflask import admin_views

