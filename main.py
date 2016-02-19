import hcluster
import sys
import printReport as reporting
from write_dendrogram  import *
from plotTree import drawdendrogram
from io import readInput

def writeOutput(natoms,tree):
    print "Numero de particulas ",natoms
    aux = getNewick(tree, "", tree.distance)
    reporting.printNewickfile('tree_'+jobName+'.nw',aux)
    reporting.printErrors(tree)
    reporting.printTreeProperties(tree)
    reporting.printMotionType(tree)
    reporting.printEffNodes(tree)
    reporting.printSubClusters(tree,5.0)
    reporting.printSubClusters(tree,4.0)
    reporting.printSubClusters(tree,3.0)
    reporting.printSubClusters(tree,2.0)

def main(jobName,inputfile):
    f = open(inputfile)
    natoms,SDdata,DistAvg,labels = readInput(f)
    f.close()
    tree = hcluster.hcluster(natoms,labels,SDdata,DistAvg)
    writeOutput(natoms,tree)
    drawdendrogram(tree,outfile='MotionTree_'+jobName+'.tiff')


if __name__ == '__main__':
    jobName = sys.argv[1]
    inputfile = sys.argv[2]
    main(jobName,inputfile)
