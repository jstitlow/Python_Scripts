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
    
    # specify the FQ centroid files
    #reference_file = '/Users/joshtitlow/Desktop/airyscan_smFISH_data/20180910_SypeGFP_rRNA_msp_smFISH_stim/aligned/smFISH_channel/_batch/_FISH-QUANT__all_spots_180913_test1.txt'
    #target_file = '/Users/joshtitlow/Desktop/airyscan_smFISH_data/20180910_SypeGFP_rRNA_msp_smFISH_stim/aligned/smFISH_channel/_batch/_FISH-QUANT__all_spots_180913_test2.txt'

    # read the FQ files from the data header to get centroid positions
    ref_file = pd.read_csv(args.ref_file, sep='\t', header=13)
    targ_file = pd.read_csv(args.target_file, sep='\t', header=13)

    xpos_ref = ref_file['Pos_X']
    ypos_ref = ref_file['Pos_Y']
    zpos_ref = ref_file['Pos_Z']

    xpos_targ = targ_file['Pos_X']
    ypos_targ = targ_file['Pos_Y']
    zpos_targ = targ_file['Pos_Z']

    # convert data into a numpy array
    target_df = np.column_stack((xpos_targ,ypos_targ,zpos_targ))

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
    codetect = 100 * (float(len(ref_file[ref_file.targ_dist > float(args.threshold)]))) / (float(len(ref_file.index)))
    print "Co-detection =", codetect,"%"

    # write ref_file to csv
    ref_file.to_csv('test_list.csv', index=False)

if __name__=='__main__':
    main(sys.argv[1:])