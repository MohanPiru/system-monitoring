import platform
import psutil
from flask import Flask, render_template

# @app.route("/")
# def i
# print(f"operating system :\n{platform.platform()}")

# print(f"processor's information :\n{platform.processor()}")



app = Flask(__name__)

@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent(interval=0.5)
    mem_metric = psutil.virtual_memory().percent
    Message1 = None
    Message2 = None
    if cpu_metric > 2 :
        Message1 = "High CPU usage Detected, scale up!!!"
    if mem_metric > 50 :
        Message2 = "High memory usage Detected, scale up!!!"    
    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message1=Message1, message2=Message2)

if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0')