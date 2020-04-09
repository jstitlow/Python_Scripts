import pickle
import subprocess
import os
import pandas as pd

figure_list = pd.read_csv('/usr/people/bioc1301/src/DavidGUI/darragh/CNS_figureIDs.csv')
#indir = '/Users/joshtitlow/src/DavidGUI/ana/answers/'
indir = ('/usr/people/bioc1301/src/DavidGUI/darragh/answers/')
infiles = os.listdir(indir)

d = {}

for index, row in figure_list.iterrows():
    figure =row['figure_id']
    thisfile = os.path.join(indir, str(figure)+'.pickle')
    try:
        with open(thisfile, 'rb') as f:
            p = pickle.load(f)
            #print('thispickle', p)
            d[figure] = p
    except:
        pass
#print(d)
df = pd.DataFrame.from_dict(d, orient =  'index')
df.to_csv(os.path.join(indir, 'questionnaire_results.csv'))
#print(df)
