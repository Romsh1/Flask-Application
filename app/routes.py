from app import flask_app

@flask_app.route("/index")
@flask_app.route("/")
def index():
    return "Hello World!"

@flask_app.route("/dashboard")
def dashboard():
    return "This is dashboard"