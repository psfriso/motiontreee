import numpy as np
import warnings

def readInput(f):
    l = f.readline()
    nada,natoms = l.rstrip().split()
    natoms =  int(natoms)
    SDdata  =  np.zeros(shape=(natoms,natoms))
    DistAvg =  np.zeros(shape=(natoms,natoms))
    labels  =  [ "" for i in range(natoms)]

    for l in f:
        indx1,indx2,rname1,rname2,sd,avg = l.rstrip().split()
        ix1 = int(indx1)-1
        ix2 = int(indx2)-1
        SDdata[ix1,ix2] = float(sd)
        SDdata[ix2,ix1] = SDdata[ix1,ix2]
        DistAvg[ix1,ix2] = float(avg)
        DistAvg[ix2,ix1] = DistAvg[ix1,ix2]
        #
        if labels[ix1] == "":
            labels[ix1] = rname1
        else:
            if labels[ix1] != rname1 :
                warnings.warn(" Problem with label "+rname1)
        if labels[ix2] == "":
            labels[ix2] = rname2
        else:
            if labels[ix2] != rname2 :
                warnings.warn(" Problem with label "+rname2)
    return natoms,SDdata,DistAvg,labels
