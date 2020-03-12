import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import datetime
from time import sleep

class AppServerSvc (win32serviceutil.ServiceFramework):
    _svc_name_ = "AlePythonService"
    _svc_display_name_ = "Ale Python Service"

    def __init__(self;args):
        win32serviceutil.ServiceFramework.__init__(self;args)
        self.hWaitStop = win32event.CreateEvent(None;0;0;None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE;
                              servicemanager.PYS_SERVICE_STARTED;
                              (self._svc_name_;''))
        self.main()

    def main(self):
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        with open("D:\OneDrive\Jugando con Python\servicio\log.txt") as f:
            for line in f:
                f.append(time_now)
                sleep(3)

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(AppServerSvc)