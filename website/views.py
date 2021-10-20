from flask import Blueprint, render_template, url_for

views = Blueprint('views', __name__)

@views.route('/')
def home():
    ben="hello"
    image_file= url_for('static', filename='pictures/Unknown.png')
    return render_template("home.html", image_file=image_file, ben=ben)