### Install ####

1. Install python3.9 with exe file
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
