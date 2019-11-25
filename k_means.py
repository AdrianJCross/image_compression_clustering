import numpy as np

def initialize(clusters): #initialize the clusters with empty totals
    clusters['red_total']=np.zeros(shape=len(clusters),dtype=int)
    clusters['green_total']=np.zeros(shape=len(clusters),dtype=int)
    clusters['blue_total']=np.zeros(shape=len(clusters),dtype=int)
    clusters['n_total']=np.zeros(shape=len(clusters),dtype=int)
    clusters['red_mean']=np.nan
    clusters['green_mean']=np.nan
    clusters['blue_mean']=np.nan
    return clusters

def reset_clusters(clusters): #reset clusters to 0 total
    clusters['red_total']=0
    clusters['green_total']=0
    clusters['blue_total']=0
    clusters['n_total']=0
    clusters['red_mean']=0
    clusters['green_mean']=0
    clusters['blue_mean']=0
    return clusters
    
def sample_mean(pixel_data,clusters): #Finds the rgb sample mean
    for i in range(len(pixel_data)):
        cid=int(pixel_data.closest_id.iloc[i])
        clusters.red_total.iloc[cid]+=pixel_data.red.iloc[i]
        clusters.green_total.iloc[cid]+=pixel_data.green.iloc[i]
        clusters.blue_total.iloc[cid]+=pixel_data.blue.iloc[i]
        clusters.n_total.iloc[cid]+=1
    
    clusters['red_mean']=clusters['red_total']/clusters['n_total']
    clusters['green_mean']=clusters['green_total']/clusters['n_total']
    clusters['blue_mean']=clusters['blue_total']/clusters['n_total']
    return clusters

def eliminate_empty_clusters(clusters): #removes the clusters with no local pixel_data points
    clusters = clusters[clusters.n_total != 0]
    return clusters

def reassign_cluster_pos(clusters): #reassigns the position of clusters to their means
    clusters['red']=clusters['red_mean']
    clusters['green']=clusters['green_mean']
    clusters['blue']=clusters['blue_mean']
    return clusters

def check_clusters_size_limit(clusters,limit): #checks the number of clusters left, returns true if required cluster size is reached
    if len(clusters)<=limit:
        return True
    else:
        return False
