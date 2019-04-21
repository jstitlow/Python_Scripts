import omero
import subprocess
import os
import pandas as pd

hostname = ('omero1.bioch.ox.ac.uk:4064')
username = ('bioc1301')
key = subprocess.Popen(['/opt/OMERO.py-5.4.8-ice36-b99/bin/omero', 'sessions', 'key'], stdout=subprocess.PIPE)
key = key.stdout.read()
PASS = getpass.getpass("Enter Password:")

conn = BlitzGateway(username, PASS, host='omero1.bioch.ox.ac.uk', port=4064, group='davisgroup')
conn.connect()
conn.SERVICE_OPTS.setOmeroGroup(-1)

indir = ('/usr/people/bioc1301/src/OMERO_scripts/OMERO_Figure_screen_dataset/test')
infiles = os.listdir(indir)

for ID in figure_IDs:
    image = conn.getObject('Image', ID)
    print image
        
for file in infiles:
    if file.endswith('.r3d'):
            file.append['old_ID']
            file = os.path.join(indir, file+'.ome_cmle.r3d')
            import_to_omero(file,hostname,username,key)

df = pd.DataFrame({'old_imageIds':old_ID, 'new_imageIds':new_ID})
df = df[['old_imageIds', 'new_imageIds']]
df.to_csv(os.path.join(indir,'new_NMJ_imageIDs.csv'), index=True)
conn.close()

def import_to_omero(filename,hostname,username,key):

    import_command = "/opt/OMERO.py-5.4.8-ice36-b99/bin/omero import "+filename+" -s "+hostname+" -u "+username+" -k "+ key
    popen = subprocess.Popen(import_command, shell=True, stdout=subprocess.PIPE)
    out, err = popen.communicate()

    omeroID = out.split(':')[1]
    print omeroID
    omeroID.append['new_ID']