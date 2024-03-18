from flask import Blueprint, render_template

root_bp = Blueprint('/', __name__, template_folder='templates')


@root_bp.route('/')
def index():
    return render_template('public/index.html', website_name="Jobbly", page_name="Home")