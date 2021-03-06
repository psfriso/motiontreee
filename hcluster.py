from numpy import *
import sys
from analyzingTree import *

class cluster_node:
    def __init__(self,name="", isEff = False ,error = False,left=None,right=None,distance=0.0,id=None,size = 0):
        self.left=left
        self.right=right
        self.name = name
        self.id=id
        self.distance=distance
        self.size = size
        self.isEff = isEff
        self.error = error

def L2dist(p1,p2,data):
    return data[p1,p2]

def neighbours(clust1,clust2,avg):
    # find if two clusters are close in space
    distCutOff = 6.2
    memb1 = get_cluster_resdiues(clust1) # members of cluster1
    memb2 = get_cluster_resdiues(clust2) # members of cluster1
    #
    distances = []
    for p1 in memb1:
        for p2 in memb2:
            distances += [ avg[ p1,p2] ]
    minDist = min(distances)
    return  minDist<distCutOff

def dissimilarity(clust1,clust2,sd):
    # find the top-20 average dissimilarity
    memb1 = get_cluster_resdiues(clust1) # members of cluster1
    memb2 = get_cluster_resdiues(clust2) # members of cluster1
    #nDisToAvg =max(10,int(0.10*len(memb1)*len(memb2)))
    #if nDisToAvg> 30: print nDisToAvg
    nDisToAvg = 20
    SDs = []
    for p1 in memb1:
        for p2 in memb2:
            SDs += [ L2dist(p1,p2,sd) ]
    # how many distances?
    nDist =len(SDs)
    out = 0.0
    if nDist < nDisToAvg:
        out = sum(SDs)/float(nDist)
    else:
         maxN =sorted(SDs,reverse=True)[0:nDisToAvg]
         out = sum(maxN)/float(len(maxN))
    #print out, len(SDs)
    return out



def hcluster(n,labels,sd,avg,distance=dissimilarity):
    #cluster the rows of the "features" matrix
    #distances={}
    currentclustid=-1

    # clusters are initially just the individual rows
    clust=[]
    for i in range(n):
        clust += [cluster_node( isEff=False, name = labels[i],size = 1 , id=i)]
    c = 1
    while len(clust)>1:
    #     print "ITERATION ",c, " of ",n-1
    #     sys.stdout.write(str(c)+' ')
        # Find a pair of nodes close in space
         for i in range(len(clust)):
             for j in range(i+1,len(clust)):
                 if neighbours(clust[i],clust[j],avg):
                     lowestpair=(i,j)
                     break
             else:
                # continue # executed if the loop ended normally (no break)
                 for i in range(len(clust)):
                     for j in range(i+1,len(clust)):
#                         if neighbours(clust[i],clust[j],avg):
                         lowestpair=(i,j)
                         print "WARNING: possible disconnected motion. Distance ", \
                               distance(clust[lowestpair[0]],clust[lowestpair[1]],sd)
             break # executed if 'continue' was skipped (break)

    #     print lowestpair, neighbours(clust[lowestpair[0]],clust[lowestpair[1]],avg)
         closest = distance(clust[lowestpair[0]],clust[lowestpair[1]],sd)
        # dissimilarity(clust[lowestpair[0]],clust[lowestpair[1]],sd)
         # loop through every pair looking for the smallest distance
         for i in range(len(clust)):
             for j in range(i+1,len(clust)):
                 d = distance(clust[i],clust[j],sd)
                 if d < closest and neighbours(clust[i],clust[j],avg):
                     closest=d
                     lowestpair=(i,j)

         #sys.exit()
         # create the new cluster
         errorWarn = False
         if not neighbours(clust[lowestpair[0]],clust[lowestpair[1]],avg):
             errorWarn = True
         newcluster=cluster_node(left=clust[lowestpair[0]],
                              right=clust[lowestpair[1]],
                              distance=closest,id=currentclustid,
                              isEff = False,
                              error = errorWarn,
                              size = clust[lowestpair[0]].size +clust[lowestpair[1]].size,
                              name = "ADDED")
         #sys.exit()
         # Finding Effective Nodes
         # First condition: Cluster of 25 residues or more
         minEffNodeSize = 25
         minBranchSize = 7
         effNodeDist = 3.5
         if newcluster.size > minEffNodeSize:
             # check if both branches are larger than 5 residues
             lSize = newcluster.left.size
             rSize = newcluster.right.size
    #         print "left ", lSize, " right ",rSize
             if lSize > minBranchSize and rSize > minBranchSize:
                 # check distance
    #             print newcluster.distance
                 if newcluster.distance > effNodeDist :
    #                 print "we found and effective node "
                     newcluster.isEff = True

         # cluster ids that weren't in the original set are negative
         currentclustid-=1
         del clust[lowestpair[1]]
         del clust[lowestpair[0]]
         clust.append(newcluster)
    #     print "Cluster size", newcluster.size
         c += 1

    return clust[0]
