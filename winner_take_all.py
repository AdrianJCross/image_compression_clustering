import numpy as np

def initialize(clusters): #initialize the clusters with empty totals
    clusters['red_temp']=np.zeros(shape=len(clusters),dtype=int)
    clusters['green_temp']=np.zeros(shape=len(clusters),dtype=int)
    clusters['blue_temp']=np.zeros(shape=len(clusters),dtype=int)
    clusters['phi']=np.zeros(shape=len(clusters))
    return clusters

def reset_clusters(clusters): #reset clusters to 0 total
    clusters['red_temp']=0
    clusters['green_temp']=0
    clusters['blue_temp']=0
    return clusters

def pixel_shift(pixel_data,clusters,epsilon): #shifts the cluster position
    for i in range(len(pixel_data)):
        red_shift=epsilon*(pixel_data['red']-clusters['red'])
        green_shift=epsilon*(pixel_data['green']-clusters['green'])
        blue_shift=epsilon*(pixel_data['blue']-clusters['blue'])
        clusters['red']=clusters['red']+red_shift
        clusters['green']=clusters['green']+green_shift
        clusters['blue']=clusters['blue']+blue_shift
    return clusters
    
    
def kohonen(pixel_data,clusters,epsilon_max,epsilon_min,k,k_max):
    epsilon=epsilon_max*(epsilon_min/epsilon_max)**(k/k_max)
  
    for i in range(len(pixel_data)):  
        phi=0
        std_dev=0
        cid=pixel_data.closest_id.iloc[i]
        
        for j in range (0,len(clusters)):
            std_dev_r=((clusters['red']-clusters.red.iloc[j])**2).sum()/(len(clusters)-1)
            std_dev_g=((clusters['green']-clusters.red.iloc[j])**2).sum()/(len(clusters)-1)
            std_dev_b=((clusters['blue']-clusters.red.iloc[j])**2).sum()/(len(clusters)-1)
            
            a=(clusters.red.iloc[cid]-clusters.red.iloc[j])**2+(clusters.green.iloc[cid]-clusters.green.iloc[j])**2+(clusters.blue.iloc[cid]-clusters.blue.iloc[j])**2
            std_dev=(std_dev_r+std_dev_g+std_dev_b)/3
            phi=np.exp(a/(2*std_dev)) #calculated phi value for shift
            clusters.phi.iloc[j]=phi
        
        red_shift=clusters['phi']*epsilon*(pixel_data['red']-clusters['red'])
        green_shift=clusters['phi']*epsilon*(pixel_data['green']-clusters['green'])
        blue_shift=clusters['phi']*epsilon*(pixel_data['blue']-clusters['blue'])
        clusters['red']=clusters['red']+red_shift
        clusters['green']=clusters['green']+green_shift
        clusters['blue']=clusters['blue']+blue_shift
    return clusters
    
    
    
    
    
    
def kohonen1234(pixel_data,clusters,epsilon_max,epsilon_min,k,k_max): #shifts the cluster position
    epsilon=epsilon_max*(epsilon_min/epsilon_max)**(k/k_max)
    red_shift=(pixel_data['red']-clusters['red'])
    green_shift=(pixel_data['green']-clusters['green'])
    blue_shift=(pixel_data['blue']-clusters['blue'])
    
    for j in range (0,len(clusters)):
        std_dev_r=((clusters['red']-clusters.red.iloc[j])**2).sum()/(len(clusters)-1)
        std_dev_g=((clusters['green']-clusters.red.iloc[j])**2).sum()/(len(clusters)-1)
        std_dev_b=((clusters['blue']-clusters.red.iloc[j])**2).sum()/(len(clusters)-1)
        std_dev=(std_dev_r+std_dev_g+std_dev_b)/3
        for i in range(0,len(clusters)):
            print(clusters)
            a=(clusters.red.iloc[i]-clusters.red.iloc[j])**2+(clusters.green.iloc[i]-clusters.green.iloc[j])**2+(clusters.blue.iloc[i]-clusters.blue.iloc[j])**2
            print('red',clusters.red.iloc[i]-clusters.red.iloc[j])
            print('green',clusters.green.iloc[i]-clusters.green.iloc[j])
            print('blue',clusters.blue.iloc[i]-clusters.blue.iloc[j])
            
            print(a)
            print(std_dev)

            phi=np.exp(a/(2*std_dev))
            clusters.red_temp.iloc[i]=red_shift
            clusters.red_temp.iloc[i]=phi
            clusters.red_temp.iloc[i]=epsilon
            clusters.red_temp.iloc[i]=clusters.red.iloc[i]+red_shiftclusters.red.iloc[i]*phi*epsilon
            clusters.green_temp.iloc[i]=clusters.green.iloc[i]+green_shift*phi*epsilon
            clusters.blue_temp.iloc[i]=clusters.blue.iloc[i]+blue_shift*phi*epsilon
    
    clusters['red']=clusters['red_temp']
    clusters['green']=clusters['green_temp']
    clusters['blue']=clusters['blue_temp']
    return clusters

