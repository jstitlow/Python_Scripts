# Calculate percentage of spots detected by separate smFISH probes
# Josh Titlow- November 30, 2018
# 
# Requires 2 files from FISHquant analysis
#      -NOTE**** need to delete last row of file SPOTS_END
#      -passed as command line arguments
#      -ref_file
#      -target_file
#
# Requires threshold distance (in nm) for assigning co-detection
#      -passed as command line argument
#      -threshold
#      -300nm is reasonable
#
# Code summary
#
# -gets 3D centroid coordinates from spots in ref_file and target_file
# -adds coordinates into a NumPy array
# -for each ref point, finds target nearest neighbor distance using KDtree in scipy spatial module
# -calculates codetection as % of ref points that have a neighbor within the specified threshold
# -prints codection % and number of spots in each channel
#
# TO DO 
# > use pandas to remove row that includes SPOTS_END


import pandas as pd
import numpy as np
from scipy import spatial
import argparse
import sys

def main(argList):
    
    parser= argparse.ArgumentParser()
    
    # specify the FQ centroid files and co-detection distance threshold in nm
    parser.add_argument('-ref_file', help='FQ_spots file for reference channel')
    parser.add_argument('-target_file', help='FQ_spots file for co-detection')
    parser.add_argument('-threshold', help='distance to calculate nearest neighbor')
        
    args= parser.parse_args(args=argList)
  
    # read the FQ files from the data header to get centroid positions (remove SPOTS END row)
    ref_file = pd.read_csv(args.ref_file, sep='\t', header=18) 
    #ref_file = ref_file[~ref_file.Pos_Y.str.contains("SPOTS_END")]
    targ_file = pd.read_csv(args.target_file, sep='\t', header=18)
    #targ_file = targ_file[~targ_file.Pos_Y.str.contains("SPOTS_END")]
    
    xpos_ref = ref_file['Pos_X']
    ypos_ref = ref_file['Pos_Y']
    zpos_ref = ref_file['Pos_Z']

    xpos_targ = targ_file['Pos_X']
    ypos_targ = targ_file['Pos_Y']
    zpos_targ = targ_file['Pos_Z']

    # convert data into a numpy array
    target_df = np.column_stack((xpos_targ,ypos_targ,zpos_targ))
    #target_df = [target_df.Pos_Y.str.contains("SPOTS_END") == False]

    # create list to store amplitude of co-detected spot, ref/targ ratio, and target distance
    targ_amp = []
    targ_dist = []
    
    for index, row in ref_file.iterrows():

        # get 3D position from X,Y,Z position columns
        pt  = row['Pos_X'], row['Pos_Y'], row['Pos_Z']

        # find nearest neighbor and calculate distance
        distance,index = spatial.KDTree(target_df).query(pt)

        # add nearest neighbor amp and dist to a list
        targ_amp.append(targ_file['AMP'].iloc[index])
        targ_dist.append(distance)

    # add lists to ref_file
    ref_file['target_amp'] = targ_amp
    ref_file['r_t_ratio'] = ref_file['AMP'].div(targ_amp)
    ref_file['targ_dist'] = targ_dist

    # calculate co-detection percentage
    codetect = 100 * (float(len(ref_file[ref_file.targ_dist < float(args.threshold)])))/(float(len(ref_file.index)))
    
    print "Co-detection =", codetect,"%"
    print "Number of spots in ch1 =", (len(ref_file))
    print "Number of spots in ch2 =", (len(targ_file))

    # write ref_file to csv
    ref_file.to_csv('test_list.csv', index=False)

if __name__=='__main__':
    main(sys.argv[1:])
    
    

