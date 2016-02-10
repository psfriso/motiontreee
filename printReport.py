import analyzingTree as hc

def printErrors(clust):
    # get error-prone nodes
    errorNodes= hc.error_nodes(clust)
    if len(errorNodes) > 0:
        print "Problematic Nodes Found"
        print "======================="
        c =1
        for key in errorNodes:
            if errorNodes[key].isEff:
                print c , ": CRITICAL Error Node ",errorNodes[key].id, " distance split", errorNodes[key].distance
            else:
                print c , ": Error Node ",errorNodes[key].id, " distance split", errorNodes[key].distance
            printSplitElemByNode(hc.get_elems_ResID(errorNodes[key].left),hc.get_elems_ResID(errorNodes[key].right))
            c += 1
        print "+++++++++++++++++++++++++++++++++++++++"+"\n"


def printTreeProperties(clust):
    print "SUMMARY"
    print "======="
    print "Particles in tree ", clust.size
    print "Max Tree Depth ", hc.get_maxDepth( clust )
    print "Number of effective nodes ", hc.count_eff_nodes( clust )
    print "Tree Depth (eff nodes) ", hc.get_TD( clust )
    print "+++++++++++++++++++++++++++++++++++++++"+"\n"


def printSplitElemByNode(coll1,coll2):
    print " SPLITS:"
    print  " ".join(coll1)
    print " AND: "
    print  " ".join(coll2)


def printEffNodes(clust):
    # Buscar e imprimir los eff nodes
    effNodes = hc.eff_nodes(clust)
#    print effNodes
    if len(effNodes)==0:
        return None
    print "Effective Nodes"
    print "==============="
    c =1
    for key in effNodes:
        #
        print "\n",c , ": Eff Node ",effNodes[key].id, " distance split", effNodes[key].distance
        printSplitElemByNode(hc.get_elems_ResID(effNodes[key].left),hc.get_elems_ResID(effNodes[key].right))
        c += 1
    print "+++++++++++++++++++++++++++++++++++++++"+"\n"


def printSubClusters(clust,size):
    subClust = hc.extract_clusters(clust,size)
    print "********************************************"
    print "*** With cutoff distance ",size, " there are ", len(subClust)," clusters"
    c=0
    for elem in subClust:
        c += 1
        print "\nCluster ",c
        listaElem = hc.get_elems_ResID(elem)
        print  " ".join(listaElem)
    print "+++++++++++++++++++++++++++++++++++++++"+"\n"

def printMotionType(clust):
    # based on effective nodes
    print "Motion At Effective Nodes Classification"
    print "========================================"
    listaNodos = hc.typeOfMotionAtEffNode(clust)
    c=1
    if listaNodos is None:
        print " No Nodes: Oscillation motion"
        print "+++++++++++++++++++++++++++++++++++++++"+"\n"
        return

    for key in listaNodos:
        print c,": NODE ",key, " is " ,hc.analyzeMotionType( listaNodos[key] ), "motion"
        c = c+1
    print "+++++++++++++++++++++++++++++++++++++++"+"\n"
