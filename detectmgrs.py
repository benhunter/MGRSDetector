import re


def getMgrsStrings(text):
	'''
	Return a list of all MGRS strings found in text.
	'''
	mgrsRegEx = r'(\d{1,2}\s*[^ABIOYZabioyz]\s*[A-Za-z]{2}\s*(\d\s*){2,})'
	mgrsIter = re.compile(mgrsRegEx).finditer(text)
	return [''.join(i.group(0).split()) for i in mgrsIter]


def test_getMgrsStrings():
	''' 
	pytest
	'''

	text = '11SNV377214'
	assert getMgrsStrings(text) == ['11SNV377214']

	text = 'test 11S     NV377214test06  D  FG  123      123test 11SNV377215'
	assert getMgrsStrings(text) == ['11SNV377214', '06DFG123123', '11SNV377215']
