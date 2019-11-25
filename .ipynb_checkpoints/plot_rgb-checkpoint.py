import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_rgb_cluster_pix(cluster,pixel,name): #plots rgb for cluster and pixels
    cluster_fig = plt.figure()
    ax=Axes3D(cluster_fig)
    ax.scatter(cluster['red'],cluster['green'],cluster['blue'],color='red',s=10)
    ax.scatter(pixel['red'],pixel['green'],pixel['blue'],color='blue',s=10)
    ax.set_xlabel('red')
    ax.set_ylabel('green')
    ax.set_zlabel('blue')
    plt.savefig('/home/across/UTK_PhD/Machine_learning_fall_2019/project_4/plots/'+name+'.png')
    print('rgb plot saved with cluster and pixels')
    
def save_file(cluster,pixel_data,name):
    cluster.to_csv('/home/across/UTK_PhD/Machine_learning_fall_2019/project_4/data/'+name+'_clusters.csv',index=False)
    pixel_data.to_csv('/home/across/UTK_PhD/Machine_learning_fall_2019/project_4/data/'+name+'_pixel_data.csv',index=False)
    
def plot_rgb_cluster(cluster,pixel,name): #plots rgb for cluster and pixels
    cluster_fig = plt.figure()
    ax=Axes3D(cluster_fig)
    ax.scatter(cluster['red'],cluster['green'],cluster['blue'],color='red',s=10)
    ax.set_xlabel('red')
    ax.set_ylabel('green')
    ax.set_zlabel('blue')
    plt.savefig('/home/across/UTK_PhD/Machine_learning_fall_2019/project_4/plots/'+name+'cluster.png')
    print('rgb plot saved with clusters')
    
def plot_perc_diff(cluster_no,perc_diff,color_name,algorithm):
    plt.figure()
    plt.plot(cluster_no,perc_diff)
    plt.xlabel('Number of clusters')
    plt.ylabel('Percentage difference')
    plt.show()
    plt.savefig('/home/across/UTK_PhD/Machine_learning_fall_2019/project_4/plots/'+algorithm+'_'+color_name+'.png')
