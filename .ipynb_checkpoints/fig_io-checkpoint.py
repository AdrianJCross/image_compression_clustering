#reads in picture and outputs rgb and clusters with closest cluster for each data point
#outputs clusters.csv for cluster locations
#outputs pixel_data.csv for each data point with rgb and closest cluster and closest cluster dist

import sys
import math
import timeit
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn import svm
from skimage import io
from PIL import Image

def read_in_fig(figure):
    image = io.imread(figure)
    io.imshow(image)
    io.show()
    rows = image.shape[0]
    cols = image.shape[1]

    #reads in rgb list from image
    r=[]#length of each should be 120*120
    g=[]
    b=[]
    c=[]
    cdist=[]
    for line in image:
        for pixel in line:
            temp_r,temp_g,temp_b=pixel
            r.append(temp_r)
            g.append(temp_g)
            b.append(temp_b)
            c.append(np.NaN)
            cdist.append(np.NaN)
    data = pd.DataFrame({'red': r,'green': g,'blue': b,'closest_id':c,'closest_dist':cdist})
    return data

def read_out_fig(pixel_data,image_input_name,name):#reads out image to same size as read in image in image_name
    image = io.imread(image_input_name)
    rows = image.shape[0]
    cols = image.shape[1]
    data = np.zeros( (rows,cols,3), dtype=np.uint8 )
    count=0
    
    for row in range(0,rows):
        for column in range(0,cols):
            data[row,column] = [pixel_data.r_cluster.iloc[count],pixel_data.g_cluster.iloc[count],pixel_data.b_cluster.iloc[count]]  #inputs pixel color for specific pixel 
            count+=1
    img = Image.fromarray( data )  
    img.save('/home/across/UTK_PhD/Machine_learning_fall_2019/project_4/images/'+name+'.png')                   


def initialize_clusters(n): #initialize clusters
    cluster = pd.DataFrame(index=range(0,n),columns=['red','green','blue'])
    cluster['red']=np.linspace(0,256,n)
    cluster['green']=np.linspace(0,256,n)
    cluster['blue']=np.linspace(0,256,n)
    return cluster
