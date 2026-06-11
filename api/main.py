from flask import Flask, request, jsonify
import os

app = Flask(__name__)

messages = [
    {"name": "Vercel部署测试", "content": "一站式前后端部署成功！"}
]

@app.route('/api/get_messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

@app.route('/api/add_message', methods=['POST'])
def add_message():
    req_data = request.get_json()
    name = req_data.get("name")
    content = req_data.get("content")
    if name and content:
        messages.append({"name": name, "content": content})
        return jsonify({"status": "success"})
    return jsonify({"status": "fail", "msg": "昵称和留言不能为空"})

# 兼容Vercel Serverless导出（关键修复点）
def handler(event, context):
    return app(event, context)

# 本地调试用，线上不会执行
if __name__ == "__main__":
    app.run()
