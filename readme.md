#freespace

Freespace is a simple cross-platform python module, returning the free disk space for a given path.


###Usage

To check free space

	import freespace 
	print "space available (in kb): %s" % (freespace.free("/path/to/folder"))
	>>> space available (in kb): 12345

freespace returns an integer in kb, to convert it right away, use

	freespace.toMB(freespace.free("/path/to/folder"))
	freespace.toGB(freespace.free("/path/to/folder"))

###Legal

MIT License.

(c) 2014 CanOfColliders
