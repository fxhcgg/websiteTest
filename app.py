from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()  # 加载 .env 文件

app = Flask(__name__)

# 获取 Mongo URI
mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)
db = client.test  # 你可以换成你自己的数据库名

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
