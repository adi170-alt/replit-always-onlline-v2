from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Your Acount/bot is alive!, if u see this and u didnt fork this then read the Instructions again"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()
