from src.app import app

@app.route('/')
def hello():
    return '<h1>Hello from RENEDO!</h1>'