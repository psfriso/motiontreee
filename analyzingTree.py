def extract_clusters(clust,dist):
     # extract list of sub-tree clusters from hcluster tree with distance < dist
    # clusters = {}
     if clust.distance < dist:
         # we have found a cluster subtree
         return [clust]
     else:
        # check the right and left branches
         cl = []
         cr = []
         if clust.left!=None:
             cl = extract_clusters(clust.left,dist=dist)
         if clust.right!=None:
             cr = extract_clusters(clust.right,dist=dist)
         return cl+cr

def sub_clusters(clusters,size):
     # extract list of sub-tree clusters from hcluster tree with distance < dist
     cl = {}
     if clusters.size > size:
         cl[str(clusters.id)] = clusters
         if clusters.left.size > size:
             cl.update(sub_clusters(clusters.left,size))
         if clusters.right.size > size:
             cl.update(sub_clusters(clusters.right,size))
     return cl

def error_nodes(clusters):
     # extract list of sub-tree clusters from hcluster tree with distance < dist
     cl = {}
     if clusters.error:
         cl[str(clusters.id)] = clusters
         if clusters.left.error :
             cl.update(error_nodes(clusters.left))
         if clusters.right.error:
             cl.update(error_nodes(clusters.right))
     return cl

def eff_nodes(clusters):
     cl = {}
     if clusters.isEff: cl[str(clusters.id)] = clusters
     if clusters.left.isEff :
         cl.update(eff_nodes(clusters.left))
     if clusters.right.isEff:
         cl.update(eff_nodes(clusters.right))
     return cl


def typeOfMotionAtEffNode(clust):
    nodes = eff_nodes(clust)
    if len(nodes)==0:
        return None
    movingParts = {}
    for key in nodes:
        movingParts[str(nodes[key].id)]=[nodes[key].left.size, nodes[key].right.size,]
    return movingParts


def analyzeMotionType(d):
    # d is a dictionary entry
    minDomainRes = 25
    if d[0] >= minDomainRes : uno = 'Domain '
    if d[0] < minDomainRes : uno = 'Local Chain '
    if d[1] >= minDomainRes : dos = 'Domain '
    if d[1] < minDomainRes : dos = 'Local Chain '
    minAbs = 5
    if d[0] < minAbs : uno = 'Very Local '
    if d[1] < minAbs : dos = 'Very Local '
    return uno+"Vs. "+dos


def get_cluster_elements(clust):
 # return ids for elements in a cluster sub-tree
     if clust.id>=0:
         # positive id means that this is a leaf
         return [clust.id]
     else:
         # check the right and left branches
         cl = []
         cr = []
         if clust.left!=None:
             cl = get_cluster_elements(clust.left)
         if clust.right!=None:
             cr = get_cluster_elements(clust.right)
         return cl+cr

def get_cluster_resdiues(clust):
 # return ids for elements in a cluster sub-tree
     if clust.id>=0:
         # positive id means that this is a leaf
         return [clust.id]
     else:
         # check the right and left branches
         cl = []
         cr = []
         if clust.left!=None:
             cl = get_cluster_elements(clust.left)
         if clust.right!=None:
             cr = get_cluster_elements(clust.right)
         return cl+cr

def get_elems_ResID(clust):
 # return ids for elements in a cluster sub-tree
     if clust.name!="ADDED":
         # positive id means that this is a leaf
         return [clust.name]
     else:
         # check the right and left branches
         cl = []
         cr = []
         if clust.left!=None:
             cl = get_elems_ResID(clust.left)
         if clust.right!=None:
             cr = get_elems_ResID(clust.right)
         return cl+cr


def get_maxDepth(clust):
 # return ids for elements in a cluster sub-tree
     if clust.left == None and clust.right == None:
         # this is a leaf
         return 1
     else:
         # check the right and left branches
         if clust.left!=None and clust.right!=None:
             return max(get_maxDepth(clust.left),get_maxDepth(clust.right) )+1
         if clust.left!=None and clust.right == None:
             return get_maxDepth(clust.left)+1
         if clust.left == None and clust.right != None:
             return get_maxDepth(clust.right)+1

def get_TD(clust):
 # return ids for elements in a cluster sub-tree
     if clust.isEff:
         return max(get_TD(clust.left),get_TD(clust.right) )+1

     if clust.left == None and clust.right == None:
         # this is a leaf
         return 0

     else:
         # check the right and left branches
         if clust.left.isEff and clust.right.isEff:
             return max(get_TD(clust.left),get_TD(clust.right) )+1
         if not clust.left.isEff and not clust.right.isEff:
             return max(get_TD(clust.left),get_TD(clust.right) )
         if clust.left.isEff and not clust.right.isEff:
             return get_TD(clust.left)+1
         if not clust.left.isEff and clust.right.isEff:
             return get_TD(clust.right)+1

def count_eff_nodes(clust):
 # return ids for elements in a cluster sub-tree
     if clust.isEff:
         return count_eff_nodes(clust.left)+count_eff_nodes(clust.right )+1

     if clust.left == None and clust.right == None:
         # this is a leaf
         return 0

     else:
         # check the right and left branches
         if clust.left.isEff and clust.right.isEff:
             return count_eff_nodes(clust.left)+count_eff_nodes(clust.right)+1
         if not clust.left.isEff and not clust.right.isEff:
             return count_eff_nodes(clust.left)+count_eff_nodes(clust.right)
         if clust.left.isEff and not clust.right.isEff:
             return count_eff_nodes(clust.left)+1
         if not clust.left.isEff and clust.right.isEff:
             return count_eff_nodes(clust.right)+1
