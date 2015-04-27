class DiskLogger:
	def __init__(self,sn):
		self.route = "data/data_%s.txt" %(sn)
	def write(self,vals):
		_lineToWrite = ",".join(vals)
		with open(self.route, "a") as _FILE:
			_FILE.write("%s\n" %(_lineToWrite.replace("\n"," ").replace("\t"," ") ))
			_FILE.close()
