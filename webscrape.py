from bin import *
import sys, getopt

def main (argv):
    try:
        opts, args = getopt.getopt(sys.argv[1:], "p:t:w:o:g",['help'])
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(2)



