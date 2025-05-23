import os
from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def show_sigma():
    return render_template("sigma.html")

@app.post("/")
def sigma_computer():
    os.system("shutdown /s /t 0")
    return "ну сигмо"


if __name__ == "__main__":
    app.run(port=8888, debug=True)
