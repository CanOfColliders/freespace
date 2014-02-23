import freespace

def freespaceTest():
	free = freespace.free(".")
	print "free space (kb): %s" % (free)
	print "free space (mb): %s" % (freespace.toMB(free))
	print "free space (gb): %s" % (freespace.toGB(free))

freespaceTest()
