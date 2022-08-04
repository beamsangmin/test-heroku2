from flask import Flask, render_template
from flask import *
from linebot.models import *
from linebot import *
import json
import requests   


app = Flask(__name__)

# Channel access token and Channel secret 
line_bot_api = LineBotApi('KtzrTuJet6PYQfzQRQEnV6F6QrC8VQTH+hzLKTfpj99SxRp1vG00aidjuAHU/YLayESkb22eatO0SU/YoYxSYbpK1bEQOUITQ7o8M2yR2phcLSsiwsJxd6dnXp4s77eB1RFC1r/6nzedhhQb1uQkXwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('277fb1c0412709857645ac19242f7be7')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/test", methods=['POST'])
def callback():
    body = request.get_data(as_text=True)
    print(body)
    return 'OK'

if __name__ == '__main__': app.run(debug=True)