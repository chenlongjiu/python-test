dictionary = (['father','chen'], ['name','stanley'],['mother','na'])
result = dict(dictionary)
print result
print(result['father'])
if result.has_key('father'):
	print 'has father'
else:
	print 'no father'
