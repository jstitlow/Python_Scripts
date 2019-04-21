# FQ_outline script
# MK Thompson- 29 March 2018
# Generates FQ outline files for each image in a directory
# Uses sys so arguments can be called directly from the command line
# Caveat of sys is that arguments are all mandatory and must be called in order
# Arg.parse is an alternative that can be used to specify arguments and make them optional
<<<<<<< HEAD
=======
# Usage:
# > python FQ_outline.py indir outdir template_file 
>>>>>>> 62675e050218d15ed7a8d444d6571f7996f34f09

import os
import subprocess
import sys

#indir = '/Users/joshtitlow/Desktop/batch/'
#outdir = '/Users/joshtitlow/Desktop/'
#template_file = '/Users/joshtitlow/Desktop/outline_template.txt'

def main(arglist):
<<<<<<< HEAD
    
=======

>>>>>>> 62675e050218d15ed7a8d444d6571f7996f34f09
    indir = arglist[0]
    outdir = arglist[1]
    template_file = arglist[2]

    #infiles = [os.path.join(indir, i) for i in os.listdir(indir) if i.endswith('.tiff')]
<<<<<<< HEAD
    filenames = [i for i in os.listdir(indir) if i.endswith('.tiff')]
    #newfilenames = [i.split('.ome-1.tiff')[0] for i in os.listdir(indir) if i.endswith('.tiff')]
    suffix = '.ome-1__outline.txt'
=======
    filenames = [i for i in os.listdir(indir) if i.endswith('.tif')]
    #newfilenames = [i.split('.ome-1.tiff')[0] for i in os.listdir(indir) if i.endswith('.tiff')]
    suffix = '__outline.txt'
>>>>>>> 62675e050218d15ed7a8d444d6571f7996f34f09
    #outlinenames = ['%s%s' % (i, suffix) for i in filenames]

    #template_file = '/Users/joshtitlow/Desktop/outline_template.txt'
    with open(template_file, 'r') as f:
        lines = f.readlines()

    for i in filenames:
<<<<<<< HEAD
        print ('processing %s' % i)
        outname = '%s%s' % (i.split('.ome-1.tiff')[0], suffix)
=======
        print 'processing %s' % i
        outname = '%s%s' % (i.split('.tif')[0], suffix)
>>>>>>> 62675e050218d15ed7a8d444d6571f7996f34f09
        outfile = os.path.join(outdir, outname)
        with open(outfile, 'w') as g:
            newlines = lines[:]
            fields = newlines[4].split('\t')
            fields[1] = i
            thisline = '\t'.join(fields)+'\n'
            newlines[4] = thisline
            for line in newlines:
                g.write(line)
<<<<<<< HEAD
                
=======

>>>>>>> 62675e050218d15ed7a8d444d6571f7996f34f09
if __name__ == '__main__':
    main(sys.argv[1:])
