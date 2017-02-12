import urllib2, base64

def push2flowroute():
	print('Pushing to flowroute...')
	data = '''{
		"to":"18586954116",
		"from":"12013555241",
		"body":"You are almost out of soap. Click the URL for options: https://sleepy-depths-92195.herokuapp.com/"
	}'''
	url = 'https://api.flowroute.com/v2/messages'
	req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
	base64string = base64.b64encode('%s:%s' % ('79011468','1b303c87a8176316387f552236b71c50'))
	req.add_header("Authorization", "Basic %s" % base64string) 
	f = urllib2.urlopen(req)
	for x in f:
		print(x)
	f.close()

push2flowroute()