# ZPF
# encoding=utf-8

from logging.handlers import TimedRotatingFileHandler
import win32serviceutil
import win32service
import win32event
import os
import logging
import inspect
import time
import shutil
import watcher
 
class PythonService(win32serviceutil.ServiceFramework):
    _svc_name_ = "watcher" # call watcher.py
    _svc_display_name_ = "WatcherServicePython20201230" #jobName displayed on windows services
    _svc_description_ = "Watch directory and copy files" #Description of job
 
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.logger = self._getLogger()
        self.path = 'D:\\tmp\\test'
        self.T = time.time()
        self.run = True
 
    def _getLogger(self):
        '''Logging'''
        logger = logging.getLogger('[PythonService]')
        this_file = inspect.getfile(inspect.currentframe())
        dirpath = os.path.abspath(os.path.dirname(this_file))
        if os.path.isdir('%s\\log'%dirpath): #Create a log folder
            pass
        else:
            os.mkdir('%s\\log'%dirpath)
        dir = '%s\\log' % dirpath
        handler = TimedRotatingFileHandler(os.path.join(dir, "watcher.log"),when="midnight",interval=1,backupCount=20)
        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
 
        return logger
 
    def SvcDoRun(self):
        self.logger.info("service is run....")
        try:
            while self.run:
                self.logger.info('---Begin---')
                watcher.main()
                self.logger.info('---End---')
        except Exception as e:
            self.logger.info(e)
            time.sleep(60)
 
    def SvcStop(self):
        self.logger.info("service is stop....")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.run = False
 
 
if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(PythonService)