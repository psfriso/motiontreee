
    #     if len(clust)==1:
    #         subClust = extract_clusters(clust[0],4.0)
    #         for elem in subClust:
    #             listaElem = get_cluster_resdiues(elem)
    #             listaRes = [ labels[x] for x in listaElem ]
    #            # print  " ".join( map(str,listaElem))
    #            # print  " ".join(listaRes)

    #     if len(clust)==1:
    #         # Tree depth
    #         maxDepth = get_maxDepth( clust[0] )
    #         print "Max Depth ", maxDepth
    #         maxDepthEffNode = get_TD( clust[0] )
    #         print "Max TD ", maxDepthEffNode

        # if len(clust)==1:
        #     # Tree depth
        #     algo = sub_clusters(clust[0],30)
        #     print type(algo)
        #     for key in algo:
        #         print key, algo[key].id,algo[key].size,algo[key].distance
        #     for key in algo:
        #         listaElem = get_cluster_resdiues(algo[key])
        #         listaRes = [ labels[x] for x in listaElem ]
        #         print len(listaRes)
        #        # print  " ".join(listaRes)
