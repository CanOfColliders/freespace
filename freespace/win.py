import ctypes

def free(path):
	""" Returns the free space in the given path (in kb) """
	storage = ctypes.c_ulonglong(0)
	ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(path), None, None, ctypes.pointer(storage))
	return int(free.value/1024)


