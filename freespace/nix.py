import subprocess
import os

def free(path):
	""" Returns the free space in the given path (in kb) """
	storage = os.statvfs(path)
	return int(storage.f_bavail * storage.f_frsize/1024)
