from flask import Blueprint, render_template

auth_bp = Blueprint('/auth', __name__, template_folder='templates')


@auth_bp.route('/', methods=['GET', 'POST'])
def auth_index():
    return "Access Denied", 403

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html', website_title="Jobbly", page_name="Login")


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('auth/register.html', website_title="Jobbly", page_name="Sign Up")


@auth_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    return "<h1>login</h1>"