from app import app

@app.route("/index")
@app.route("/")
def index():
    return "Hello World!"

@app.route("/dashboard")
def dashboard():
    return "This is dashboard"