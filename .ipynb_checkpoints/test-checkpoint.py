import subprocess
key = subprocess.Popen(['/opt/OMERO.py-5.4.8-ice36-b99/bin/omero', 'sessions', 'key'], stdout=subprocess.PIPE)
key = key.stdout.read()
print key

#proc = subprocess.Popen('ls', stdout=subprocess.PIPE)
#>>> output = proc.stdout.read()