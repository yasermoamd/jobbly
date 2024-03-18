from flask import Blueprint ,render_template

dashboard_bp = Blueprint('/dashboard', __name__, template_folder='templates')


@dashboard_bp.route('/')
def dashboard():
    return "<h1>Dashboard</h1>"

