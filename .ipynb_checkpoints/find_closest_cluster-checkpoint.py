import numpy as np
import pandas as pd

def find_coord_closest_cluster(coordinate, cluster): #find closest cluster for single coordinate
    coord_comp=(coordinate['red']-cluster['red'])**2+(coordinate['green']-cluster['green'])**2+(coordinate['blue']-cluster['blue'])**2                  
    minid=int(coord_comp.idxmin())
    mindist=np.sqrt(coord_comp.min())
    
    return minid,mindist

def find_all_closest_cluster(data_pixel,cluster): #find closest cluster for all coordinates
    for i in range(len(data_pixel)):
        data_pixel.closest_id.iloc[i], data_pixel.closest_dist.iloc[i]=find_coord_closest_cluster(data_pixel.iloc[i],cluster.copy())
        
    return data_pixel  

def update_pixels_to_closest_cluster(pixel_data,clusters): #updates pixel to the rgb value of closest cluster
    pixel_data['closest_id']=pixel_data['closest_id'].astype(int)
    r=clusters.red.iloc[pixel_data['closest_id']].copy()
    g=clusters.green.iloc[pixel_data['closest_id']].copy()
    b=clusters.blue.iloc[pixel_data['closest_id']].copy()
    r=r.tolist()
    g=g.tolist()
    b=b.tolist()
    cluster_addition = pd.DataFrame(list(zip(r, g,b)), columns =['r_cluster', 'g_cluster','b_cluster']) 
    pixel_data=pd.concat([pixel_data,cluster_addition],axis=1)
    return pixel_data
    
def reset_closest_cluster(data_pixel):
    data_pixel['closest_id']=0
    data_pixel['closest_dist']=0
    
    return data_pixel