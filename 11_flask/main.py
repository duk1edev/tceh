from flask import Flask

app = Flask('__name__')


@app.route('/')
def home():
    return 'Hello first Flask App'

@app.route('/duk1e')
def duk1e():
    return ('<h2>Hello duk1e</h2>' + '<h5>Olololo</h5>')

if __name__ == '__main__':
    app.run()
