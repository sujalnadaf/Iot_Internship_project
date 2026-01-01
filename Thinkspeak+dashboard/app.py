from flask import Flask, render_template, jsonify
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="env_db"
)
cursor = db.cursor(dictionary=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/latest")
def latest():
    cursor.execute("""
        SELECT * FROM sensor_data
        ORDER BY id DESC
        LIMIT 1000
    """)
    data = cursor.fetchall()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
