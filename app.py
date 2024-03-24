import platform
import psutil
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent(interval=0.5)
    mem_metric = psutil.virtual_memory().percent
    disk_metric = psutil.disk_usage('/').percent
    os = platform.platform()
    processor = platform.processor()
    cpu_count=psutil.cpu_count()

#this is for getting disk partitions
    # len=len(psutil.disk_partitions())
    # lis = []

    # for i in range(len):
    #    lis.append(psutil.disk_partitions()[i].device)
    #    disk_partitions=lis

    Message1 = None
    Message2 = None
    Message3 = None

    if cpu_metric > 50 :
        Message1 = "High CPU usage Detected, scale up!!!"
    if mem_metric > 50 :
        Message2 = "High memory usage Detected, scale up!!!" 
    if disk_metric > 80 :
        Message3 = "High Disk usage Detected, scale up!!!"       
    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric,disk_metric=disk_metric,os=os,processor=processor,cpu_count=cpu_count, message1=Message1, message2=Message2, message3=Message3)


@app.route('/get_process_info', methods=['GET'])
def get_process_info():
    processes = psutil.process_iter()
    process_info = []
    for process in processes:
        process_info.append({"pid": process.pid, "name": process.name()})
    return {"process_info": process_info}

@app.route("/running")
def run():
    return render_template("process.html")
  
    

if __name__=='__main__':
    app.run(debug=True, host = '0.0.0.0')