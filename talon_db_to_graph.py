import networkx as nx
import argparse
import pandas as pd
import pickle
import os
from utils import *

def get_args():

	desc = 'Loads a GTF into a graph'
	parser = argparse.ArgumentParser(description=desc)

	parser.add_argument('-db', '-d', dest='db',
		help='TALON database to load into graph')
	parser.add_argument('--o', dest='oname', default=None,
		help='Output directory/prefix to store graph')

	args = parser.parse_args()
	return args

def make_oname(oname):

	if not oname: oname = os.getcwd()+'/splicing_graph.p'
	else: oname = oname+'_splicing_graph.p'

	return oname

def main():

	args = get_args()
	db = args.db
	oname = make_oname(args.oname)

	sg = utils.SpliceGraph(talon_db=db)

	# save to output file
	with open(oname, 'wb') as ofile:
		pickle.dump(sg, ofile)

if __name__ == '__main__': main()