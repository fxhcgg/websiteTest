from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import psycopg2
import os

app = FastAPI()

# 允许前端跨域请求
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境建议限定域名
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_conn():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT", "5432")
    )

@app.get("/")
def home():
    return {"msg": "Hello AR Fullstack Demo!"}

@app.get("/users", response_model=List[str])
def get_users():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [row[0] for row in rows]

@app.get("/map_nodes")
def get_map_nodes():
    # 简单示例地图节点数据
    nodes = [
        {"id": 1, "name": "Room A101", "floor": 1, "x": 100, "y": 200},
        {"id": 2, "name": "Room A102", "floor": 1, "x": 300, "y": 220},
        {"id": 3, "name": "Hall B1",  "floor": 1, "x": 150, "y": 450},
    ]
    return nodes