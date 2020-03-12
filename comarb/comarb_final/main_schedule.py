import schedule
import subprocess
import sys
import time


def comarb():
    job = [sys.executable, "D:\\OneDrive\\Jugando con Python\\comarb\\comarb_final\\main.py"]
    subprocess.call(job)
    # subprocess.Popen("D:\OneDrive\Jugando con Python\comarb\comarb_final\main.py",)


schedule.every().day.at("06:30").do(comarb)
schedule.every().day.at("10:30").do(comarb)
schedule.every().saturday.at("06:45").do(comarb)  # sábado
schedule.every().sunday.at("06:45").do(comarb)  # domingo

while True:
    schedule.run_pending()
    print(f"--> {time.ctime()}")
    time.sleep(1)
