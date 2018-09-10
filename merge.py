import pandas as pd

left = pd.read_csv('/Users/joshtitlow/Desktop/smFISH_screen/priority_list.csv')
right = pd.read_csv('/Users/joshtitlow/Desktop/smFISH_screen/NMJ.csv')
merge = pd.merge(left, right, how='left', on=['CPTI'])
left = merge
right = pd.read_csv('/Users/joshtitlow/Desktop/smFISH_screen/cb.csv')
merge = pd.merge(left, right, how='left', on=['CPTI'])
left = merge
right = pd.read_csv('/Users/joshtitlow/Desktop/smFISH_screen/mb.csv')
merge = pd.merge(left, right, how='left', on=['CPTI'])
left = merge
right = pd.read_csv('/Users/joshtitlow/Desktop/smFISH_screen/VNC.csv')
merge = pd.merge(left, right, how='left', on=['CPTI'])
left = merge
right = pd.read_csv('/Users/joshtitlow/Desktop/smFISH_screen/overview.csv')
merge = pd.merge(left, right, how='left', on=['CPTI'])

merge.to_csv('/Users/joshtitlow/Desktop/smFISH_screen/merge.csv')
