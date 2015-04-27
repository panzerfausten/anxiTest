_words = ['AMOR','ALMO','MODO','ORAR','TOMA','SURENO','ABUSAR','APARTE','BARATO','PASTOR']

with open('patron.html','r') as _patron:
	_strPatron = _patron.readlines()
	for _i, _w in enumerate(_words):
		_strOut = _strPatron.replace("<div id='big_number'>WORD</div>","<div id='big_number'>%s</div>" %(_w))
		with open(str(_i) +".html",'w') as _fileOut:
			_fileOut.write(_strOut)
