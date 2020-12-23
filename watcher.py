#!python
import sys, os, datetime, time, shutil, hashlib, logging
#stat

savedSet=set()
source_dir = "D:\\tmp\\test\\"
dest_dir = "D:\\tmp\\test\\destination\\"
log_dir = "D:\\tmp\\test\\log\\"
filter = "*.ndpi"
new_file_action = "copy" #can be copy/move

logging.basicConfig(filename=os.path.join(log_dir, 'watcher.log'), level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def trace_failed(src):
	f = open(os.path.join(log_dir, "copy_failed.txt"), "a")
	f.write(format(datetime.datetime.now()))
	f.write(" : ")
	f.write(format(src))
	f.write("\n")
	f.close()

def trace_ok(src):
	f = open(os.path.join(log_dir, "copy_ok.txt"), "a")
	f.write(format(datetime.datetime.now()))
	f.write(" : ")
	f.write(format(src))
	f.write("\n")
	f.close()

def manage_new_files(src):
	(file_name, file_date, file_size, file_md5)=src
	shutil.copy(os.path.join(source_dir, file_name), dest_dir)
	md5_dst=md5(os.path.join(dest_dir, file_name))
	logging.debug("file_md5 : {}".format(file_md5))
	logging.debug("md5_dst : {}".format(md5_dst))
	if (file_md5 == md5_dst):
		logging.info("Files {} and {} are identical".format(os.path.join(source_dir, file_name),(os.path.join(dest_dir, file_name))))
		os.remove(os.path.join(source_dir, file_name))
		trace_ok(src)
		logging.info("Source has been removed")
	else:
		logging.info("Files are different")
		trace_failed(src)


if __name__ == "__main__":		
	first_occurence = True
	while True:
		logging.debug("###############################")
		logging.info("########## Start loop #########")
		logging.debug("###############################")
		logging.info('Time: {}'.format(time.ctime()))
		
		#Current situation => retrievedSet
		nameSet=set()
		for file in os.listdir(source_dir):
			fullpath=os.path.join(source_dir, file)
			if os.path.isfile(fullpath):
				nameSet.add(file)
		
		retrievedSet=set()
		for name in nameSet:
			stats=os.stat(os.path.join(source_dir, name))
			mtime=datetime.datetime.fromtimestamp(stats.st_mtime)
			#Check if file last modification time is > than 1 minute
			delta = datetime.datetime.now() - mtime
			#logging.debug("delta : {}".format(delta))
			if delta > datetime.timedelta(seconds=60):
				size=stats.st_size #If you add this, you will be able to detect file size changes as well.
				md5_file = md5(os.path.join(source_dir, name))
				#Create a tuple (file_name, file_date, file_size, file_md5)
				retrievedSet.add((name,mtime,size,md5_file))
		logging.debug("retrievedSet : {}".format(retrievedSet))
		
		#At the 1st occurence, set Saved=retrieved to bypass newSet and deletedSet 
		if (first_occurence):
			savedSet=retrievedSet
			
		newSet=retrievedSet-savedSet
		logging.info("newSet : {}".format(newSet))
		for file in newSet:
			logging.info('Manage new file : {}'.format(file))
			manage_new_files(file)

		deletedSet=savedSet-retrievedSet
		logging.debug("deletedSet : {}".format(deletedSet))
		
		savedSet=retrievedSet
		logging.debug("savedSet : {}".format(savedSet))
		
		first_occurence = False
		time.sleep(30)

	input('Press ENTER to exit')

