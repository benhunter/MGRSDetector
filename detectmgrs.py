import re

def regexCheck(regex, item):
	expr = re.compile(regex)
	m = expr.match(item)
	return m

item = '11SNV377214'
# item = 'test 11SNV377214 test'

mgrsRegEx = "\d{1,2}[^ABIOYZabioyz][A-Za-z]{2}([0-9][0-9])+"
# result = re.compile(mgrsRegEx).match(item)
result = re.compile(mgrsRegEx).findall(item)
print(result)
