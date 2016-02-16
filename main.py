import os
from PIL import Image,ImageDraw
from PIL import ImageFont
from numpy import *
import hcluster
import sys
import warnings
import printReport as reporting
from write_dendrogram  import *

jobName = sys.argv[1]
inputfile = sys.argv[2]

f = open(inputfile)

l = f.readline()
nada,natoms = l.rstrip().split()

natoms =  int(natoms)



SDdata  =  zeros(shape=(natoms,natoms))
DistAvg =  zeros(shape=(natoms,natoms))
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


#print SDdata[0]

#create a list of images
#imlist = []
#for filename in os.listdir('./'):
#    if os.path.splitext(filename)[1] == '.jpg':
#        imlist.append(filename)
#n = len(imlist)

#extract feature vector for each image
#features = zeros((n,3))
#for i in range(n):
#    im = array(Image.open(imlist[i]))
#    R = mean(im[:,:,0].flatten())
#    G = mean(im[:,:,1].flatten())
#    B = mean(im[:,:,2].flatten())
#    features[i] = array([R,G,B])

tree = hcluster.hcluster(natoms,labels,SDdata,DistAvg)


#sys.exit()


#
def getheight(node):
    """ Return the height of a node. """

    if node.left==None and node.right==None:
        return 1
    else: # set height to sum of each branch
        return getheight(node.left)+getheight(node.right)


def getdepth(node):
    """ Return the depth of a node. """

    if node.left==None and node.right==None:
        return 0
    else: # max of each child plus own distance
        return max(getdepth(node.left),getdepth(node.right))+node.distance

def drawdendrogram(clust,outfile='clusters.tiff'):
    # height and width
    h=getheight(clust)*5
    w=1200
    depth=getdepth(clust)*0.7

     # width is fixed, so scale distances accordingly
    scaling=float(w-150)/depth

     # Create a new image with a white background
    img=Image.new('RGB',(w,h),(255,255,255))
    draw=ImageDraw.Draw(img)

    draw.line((0,h/2,10,h/2),fill=(255,0,0))

     # Draw the first node
    drawnode(draw,clust,10,(h/2),scaling,img)
    #img.save(jpeg)
    img.save(outfile, 'TIFF', quality=95 , dpi=(500.0, 500.0) )

def drawnode(draw,clust,x,y,scaling,img):
     if clust.id<0:
         h1=getheight(clust.left)*5
         h2=getheight(clust.right)*5
         top=y-(h1+h2)/2
         bottom=y+(h1+h2)/2
         # Line length
         ll=clust.distance*scaling*0.7
         if clust.isEff:
             draw.ellipse((x - 8 ,y - 8, x + 8, y + 8 ), fill = 'black')
         if clust.error:
             draw.ellipse((x - 12 ,y - 12, x + 12, y + 12 ), fill = 'red')
         # Vertical line from this cluster to children
         draw.line((x,top+h1/2,x,bottom-h2/2),fill=(0,0,0))

         # Horizontal line to left item
         draw.line((x,top+h1/2,x+ll,top+h1/2),fill=(0,0,0))

         # Horizontal line to right item
         draw.line((x,bottom-h2/2,x+ll,bottom-h2/2),fill=(0,0,0))

         # Call the function to draw the left and right nodes
         drawnode(draw,clust.left,x+ll,top+h1/2,scaling,img)
         drawnode(draw,clust.right,x+ll,bottom-h2/2,scaling,img)
     else:
        # font = ImageFont.truetype("sans-serif.ttf", 16)
        # font = ImageFont.truetype("arctik.1.ttf", 10)
        # draw.text((x, y),clust.name,(0,0,0))
        pass

print "Numero de particulas ",natoms

aux = getNewick(tree, "", tree.distance)
print aux

sys.exit("bye")

reporting.printErrors(tree)
reporting.printTreeProperties(tree)
reporting.printMotionType(tree)
reporting.printEffNodes(tree)
reporting.printSubClusters(tree,5.0)
reporting.printSubClusters(tree,4.0)
reporting.printSubClusters(tree,3.0)
reporting.printSubClusters(tree,2.0)

drawdendrogram(tree,outfile='MotionTree_'+jobName+'.tiff')
