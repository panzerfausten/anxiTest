_words = ['AMOR','ALMO','MODO','ORAR','TOMA','SAPO','LORO','ASCO','ELSA','GOTA','SURENO','ABUSAR','APARTE','BARATO','PASTOR','ARCOS','TORSO','VIOLIN','CERDO','NORTE','INSOMNIOS','ARGENTINO','CARRUAJE','CAROLINA','ARDIERAS','ANIMALES','TALLERES','COMPLACIDO','CARREOLA','OCARINAS']

with open('patron.html','r') as _patron:
	_strPatron = _patron.readlines()
	for _i, _w in enumerate(_words):
		_strOut = []
		for _line in _strPatron:
			_r = _line.replace("<div id='big_number'>WORD</div>","<div id='big_number'>%s</div>" % _w)
			if (_i +1 == 10):
				_r = _r.replace("window.location.href = '2.html'","window.location.href = 'suds1.html'")
			elif(_i + 1 == 20):
				_r = _r.replace("window.location.href = '2.html'","window.location.href = 'suds2.html'")
			elif(_i + 1 == 30):
				_r = _r.replace("window.location.href = '2.html'","window.location.href = 'suds3.html'")
			else:
				_r = _r.replace("window.location.href = '2.html'","window.location.href = '%i.html'" %(_i+2))
			_r = _r.replace("saveData(getSubjectName(),_startTime,getUnixTime(),'1',awns)","saveData(getSubjectName(),_startTime,getUnixTime(),'%i',awns)" %(_i+1))
			_strOut.append(_r.replace("<div id='div_title'> Prueba 1/20</div>","<div id='div_title'> Prueba %i/30</div>" %(_i+1)))
	
		with open(str(_i+1) +".html",'w') as _fileOut:
			for _line in _strOut:
				_fileOut.write(_line)
