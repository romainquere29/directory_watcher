### Install ####

1. Install python3.9 with exe file or download from MS Store
2. Check System >> Environment variables >> Path
3. Onpen PS terminal and check python path
	Get-Command python).Path
	C:\Program Files\Python39\python.exe

	
### 

$params = @{
  Name = "WatcherService3"
  BinaryPathName = '"C:\Program Files\Python39\python.exe D:\Git\watcher.py"'
  DisplayName = "Watcher Service3"
  StartupType = "Automatic"
  Description = "This is a test service."
}
New-Service @params


###########


python -V => Should be 3.9.0
PS D:\Git> python -m venv .\virtual_env\
PS D:\Git> .\virtual_env\Scripts\activate
pip install pypiwin32










PS C:\WINDOWS\system32> cd 'D:\Git\'
PS D:\Git> .\virtual_env\Scripts\activate
(virtual_env) PS D:\Git>
(virtual_env) PS D:\Git>
(virtual_env) PS D:\Git>
(virtual_env) PS D:\Git>
(virtual_env) PS D:\Git> python -V
Python 3.9.0
(virtual_env) PS D:\Git> pip freeze
future==0.18.2
pefile==2019.4.18
PyInstaller==3.2
pypiwin32==223
pywin32==300
 
 pip install pywin32

(virtual_env) PS D:\Git> cd .\directory_watcher\
(virtual_env) PS D:\Git\directory_watcher>
(virtual_env) PS D:\Git\directory_watcher>
(virtual_env) PS D:\Git\directory_watcher> python .\PythonService.py
Usage: 'PythonService.py [options] install|update|remove|start [...]|stop|restart [...]|debug [...]'
Options for 'install' and 'update' commands only:
 --username domain\username : The Username the service is to run under
 --password password : The password for the username
 --startup [manual|auto|disabled|delayed] : How the service starts, default = manual
 --interactive : Allow the service to interact with the desktop.
 --perfmonini file: .ini file to use for registering performance monitor data
 --perfmondll file: .dll file to use when querying the service for
   performance data, default = perfmondata.dll
Options for 'start' and 'stop' commands only:
 --wait seconds: Wait for the service to actually start or stop.
                 If you specify --wait with the 'stop' option, the service
                 and all dependent services will be stopped, each waiting
                 the specified period.
(virtual_env) PS D:\Git\directory_watcher> python .\PythonService.py install
Installing service watcher
Changing service configuration
Service updated


