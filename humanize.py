suffixes ={1024:["kib","mib","gib","tib"],1000:["kb","mb","gb","tb"]}

def approximate_size(size,a_kilobyte_is_1000_byte=True):
	""" Calculates the approximate size of a file 
	size-- file size in bytes 
	a_kilobyte_is_1000_byte-- If ture 1000 , False 1024
	returns approximate size 
	"""
	if size<0:
		raise ValueError("it's a negative number")
	multiple = 1000 if a_kilobyte_is_1000_byte else 1024
	for suf in suffixes[multiple]:
		size /= multiple
		if size<multiple:
			return "{0:.1f} {1}".format(size,suf)
	raise ValueError("it's too big to handle ")	






if __name__=="__main__":
	print(approximate_size(13928041088888888,False)) 
	