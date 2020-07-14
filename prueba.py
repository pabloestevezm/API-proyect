from app import app_

@app_.route('/')
def hello():
    return '<h1>Hello!</h1>'