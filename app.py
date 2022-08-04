from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/test", methods=['GET'])
def callback():
    print('xxxxx')
    return 'OK'

if __name__ == '__main__': app.run(debug=True)