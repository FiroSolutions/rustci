#python >=3.6
import requests, json
import os, sys
from subprocess import Popen, PIPE, STDOUT


print('Checking Cargo.toml')
#check if file is here
print('Uploading Cargo.toml')
command = "cat Cargo.toml | nc termbin.com 9999"
fluff = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT)
link = fluff.stdout.read()#b'https://termbin.com/7a3u\n\x00'
link = link.decode().split('\n')[0]
aa = requests.get('https://rust.firosolutions.com/apiadd', json={'urllink':link})
print('Result:')
for x in json.loads(requests.get("https://rust.firosolutions.com/paste/{}/jsonresponse".format(json.loads(aa.text).get('pasteid'))).text).get('libs'):
	if len(x)==4:
		print('\033[1;31m Found a vulnerability for {} \033[0;0m'.format(x[0]))
		print('\033[0;92m Description: \033[0;0m')
		print(x[3].get(list(x[3].keys())[0]).get('description'))
		print("Link:", x[3].get(list(x[3].keys())[0]).get('link'))
	else:
		print("Library:",x[0], 'Your Version:', x[1], 'Latest Version', x[2])


print('View result on:')
print('https://rust.firosolutions.com/paste/{}/jsonresponse'.format(json.loads(aa.text).get('pasteid')))

