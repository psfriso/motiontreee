from PIL import Image,ImageDraw
from PIL import ImageFont
import hcluster


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
