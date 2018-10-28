import subprocess
host = '0.0.0.0'
port = 1234
#txtFile = 'stations.txt'
templateFile = 'interface.html'

        
def mpcCommand(cmd):
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	return p.stdout.read()
