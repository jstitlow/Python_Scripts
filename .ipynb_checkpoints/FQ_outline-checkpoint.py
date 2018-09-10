# FQ_outline script
# MK Thompson- 29 March 2018
# Generates FQ outline files for each image in a directory
# Uses sys so arguments can be called directly from the command line
# Caveat of sys is that arguments are all mandatory and must be called in order
# Arg.parse is an alternative that can be used to specify arguments and make them optional

import os
import subprocess
import sys

#indir = '/Users/joshtitlow/Desktop/batch/'
#outdir = '/Users/joshtitlow/Desktop/'
#template_file = '/Users/joshtitlow/Desktop/outline_template.txt'

def main(arglist):
    
    indir = arglist[0]
    outdir = arglist[1]
    template_file = arglist[2]

    #infiles = [os.path.join(indir, i) for i in os.listdir(indir) if i.endswith('.tiff')]
    filenames = [i for i in os.listdir(indir) if i.endswith('.tif')]
    #newfilenames = [i.split('.ome-1.tiff')[0] for i in os.listdir(indir) if i.endswith('.tiff')]
    suffix = '__outline.txt'
    #outlinenames = ['%s%s' % (i, suffix) for i in filenames]

    #template_file = '/Users/joshtitlow/Desktop/outline_template.txt'
    with open(template_file, 'r') as f:
        lines = f.readlines()

    for i in filenames:
        print 'processing %s' % i
        outname = '%s%s' % (i.split('.tif')[0], suffix)
        outfile = os.path.join(outdir, outname)
        with open(outfile, 'w') as g:
            newlines = lines[:]
            fields = newlines[4].split('\t')
            fields[1] = i
            thisline = '\t'.join(fields)+'\n'
            newlines[4] = thisline
            for line in newlines:
                g.write(line)
                
if __name__ == '__main__':
    main(sys.argv[1:])
