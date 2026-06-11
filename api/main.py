from flask import Flask, request, jsonify
# 同域名部署，跨域自动消失，可以删掉CORS，保留也不报错
app = Flask(__name__)

# 内存存储留言（重启部署会清空，文末附SQLite持久化版本）
messages = [
    {"name": "Vercel部署测试", "content": "一站式前后端部署成功！"}
]

# 获取所有留言
@app.route('/api/get_messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

# 新增留言接口
@app.route('/api/add_message', methods=['POST'])
def add_message():
    req_data = request.get_json()
    name = req_data.get("name")
    content = req_data.get("content")
    if name and content:
        messages.append({"name": name, "content": content})
        return jsonify({"status": "success"})
    return jsonify({"status": "fail", "msg": "昵称和留言不能为空"})

# ✅ 关键：Vercel自动托管，必须删除 app.run()
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)

app = app.wsgi_app