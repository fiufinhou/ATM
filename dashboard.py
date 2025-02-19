from flask import Flask, render_template
from database import get_all_data

app = Flask(__name__)

@app.route('/')
def dashboard():
    """ 📊 عرض جميع البيانات المخزنة في القاعدة """
    data = get_all_data()
    return render_template("dashboard.html", data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
