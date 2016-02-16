# from scipy.cluster import hierarchy
# def getNewick(node, newick, parentdist, leaf_names):
#     if node.is_leaf():
#         return "%s:%.2f%s" % (leaf_names[node.id], parentdist - node.dist, newick)
#     else:
#         if len(newick) > 0:
#             newick = "):%.2f%s" % (parentdist - node.dist, newick)
#         else:
#             newick = ");"
#         newick = getNewick(node.get_left(), newick, node.dist, leaf_names)
#         newick = getNewick(node.get_right(), ",%s" % (newick), node.dist, leaf_names)
#         newick = "(%s" % (newick)
#         return newick
#
# tree = hierarchy.to_tree(Z,False)
# getNewick(tree, "", tree.dist, leaf_names)
import hcluster

        # self.left=left
        # self.right=right
        # self.name = name
        # self.id=id
        # self.distance=distance
        # self.size = size
        # self.isEff = isEff
        # self.error = error

def getNewick(node, newick, parentdist):
    if node.id >= 0:
        return "%s:%.2f%s" % (node.name, parentdist - node.distance, newick)
    else:
        if len(newick) > 0:
            newick = "):%.2f%s" % (parentdist - node.distance, newick)
        else:
            newick = ");"
        newick = getNewick(node.left, newick, node.distance)
        newick = getNewick(node.right, ",%s" % (newick), node.distance)
        newick = "(%s" % (newick)
        return newick

#tree = hierarchy.to_tree(Z,False)
#getNewick(tree, "", tree.dist)
