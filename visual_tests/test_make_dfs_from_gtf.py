import sys
import os
from collections import defaultdict
lib_path = '/'.join(os.path.abspath(__file__).split('/')[0:-2])
sys.path.append(lib_path+'/utils/')
sys.path.append(lib_path)
from SpliceGraph import SpliceGraph
from utils import *
import cProfile

# gtf = '/Users/fairliereese/mortazavi_lab/ref/gencode.v24/gencode.v24.annotation.txt'
# gtf = 'input_files/hippocampus_mapt.gtf'
gtf = 'input_files/test_combine_2.gtf'
sg = SpliceGraph()

# print('dana')
# cProfile.run('sg.create_dfs_gtf_dana(gtf)')
# print('fairlie')
# cProfile.run('sg.create_dfs_gtf(gtf)')

# print('dana')
# sg.create_dfs_gtf_dana(gtf)
print('fairlie')
sg.create_dfs_gtf(gtf)

# print(transcripts)
# print(exons)