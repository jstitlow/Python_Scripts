############################################################################# 
# Calculate percentage of spots detected by separate smFISH probes          # 
# Josh Titlow- November 30, 2018                                            #
#                                                                           # 
# Requires 2 folders with output files from FISHquant analysis              #
# ******NOTE****** need to delete last row of file SPOTS_END                #
#      -files should have the same name                                     #
#      -passed as command line arguments                                    #
#      -ch1_indir                                                           #    
#      -ch2_indir                                                           #
#                                                                           #
# Requires threshold distance (in nm) for assigning co-detection            #
#      -passed as command line argument                                     #    
#      -threshold                                                           #
#      -300nm is reasonable                                                 #
#                                                                           #        
# TO DO                                                                     #
# add output from                                                           #    
#############################################################################

import pandas as pd
import numpy as np
from scipy import spatial
import argparse
import sys
import os


def main(argList):
    
    parser= argparse.ArgumentParser()
    
    # specify the FQ centroid files and co-detection distance threshold in nm
    parser.add_argument('-ch1_indir', help='FQ_spots file for reference channel')
    parser.add_argument('-ch2_indir', help='FQ_spots file for co-detection')
    #parser.add_argument('-threshold', help='distance to calculate nearest neighbor')
    threshold_range = [50,100,150,200,250,300,350,400,450,500] 
    args= parser.parse_args(args=argList)

    ch1_infiles = os.listdir(args.ch1_indir)

    # create list to store data
    filename = []
    co_detect = []
    ch1_spots = []
    ch2_spots = []
    threshold = []
    
    for t in threshold_range:
        print "calculating co-detection percentage for threshold =", t, "nm"
        # loop through files
        for i in ch1_infiles:
            if i.endswith('spots.txt'):
                ref_file = os.path.join(args.ch1_indir,i)
                #print "processing", i, "for threshold =", t
                ref_file = pd.read_csv(ref_file, sep='\t', header=18)
                #ref_file = ref_file[~ref_file.Pos_Y.str.contains("SPOTS_END")]
                targ_file = os.path.join(args.ch2_indir, i)
                targ_file = pd.read_csv(targ_file, sep='\t', header=18)
                #targ_file = targ_file[~targ_file.Pos_Y.str.contains("SPOTS_END")]

                # get centroid coordinates
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
                    #print pt
                    # find nearest neighbor and calculate distance
                    distance,index = spatial.KDTree(target_df).query(pt)

                    # add nearest neighbor amp and dist to a list
                    targ_amp.append(targ_file['AMP'].iloc[index])
                    targ_dist.append(distance)

                # add lists to ref_file
                ref_file['target_amp'] = targ_amp
                ref_file['r_t_ratio'] = ref_file['AMP'].div(targ_amp)
                ref_file['targ_dist'] = targ_dist

                # calculate co-detection percentage and add it to list
                codetect = 100 * (float(len(ref_file[ref_file.targ_dist < float(t)])))/(float(len(ref_file.index)))
                co_detect.append(codetect)

                # calculate number of spots and add to list, with filename
                ch1_spots.append(len(ref_file))
                ch2_spots.append(len(targ_file))
                filename.append(i)
                threshold.append(t)

                # write ref_file to csv
                #ref_file.to_csv('test_list.csv', index=False)
    
    # add data to dataframe and save
    df = pd.DataFrame({'filename':filename, 'threshold':threshold, 'co_detect':co_detect, 'ch1_spots':ch1_spots, 'ch2_spots':ch2_spots})
    df = df[['filename', 'threshold', 'co_detect', 'ch1_spots', 'ch2_spots']]
    df.to_csv('codetection_stats.csv', index=False)
    
if __name__=='__main__':
    main(sys.argv[1:])
    
    

