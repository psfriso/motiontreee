import hcluster as hc

def printErrors(clust,labels):
    # get error-prone nodes
    errorNodes= hc.error_nodes(clust)
    if len(errorNodes) > 0:
        print "Problematic Nodes Found"
        print "======================="
        c =1
        for key in errorNodes:
            if errorNodes[key].isEff:
                print c , ": CRITICAL Node ",errorNodes[key].id, " distance split", errorNodes[key].distance
            else:
                print c , ": Node ",errorNodes[key].id, " distance split", errorNodes[key].distance
            print "Splits:"
            listaElem = hc.get_cluster_resdiues(errorNodes[key].left)
            listaRes = [ labels[x] for x in listaElem ]
            print  " ".join(listaRes)
            print "AND "
            listaElem = hc.get_cluster_resdiues(errorNodes[key].right)
            listaRes = [ labels[x] for x in listaElem ]
            print  " ".join(listaRes)
            c += 1
        print "+++++++++++++++++++++++++++++++++++++++"
