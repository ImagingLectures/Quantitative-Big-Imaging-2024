import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.colors as colors
from sklearn.metrics import confusion_matrix
from seaborn import heatmap
import numpy as np

def buildCMap(plots) :
    cmaplist = []

    for p0 in plots :
        cmaplist.append(p0.get_color())
        
    return ListedColormap(cmaplist)

def magnifyRegion(img,roi, figsize, cmap='gray',vmin=0,vmax=0,title='Original') :
    if vmin==vmax:
        vmin=img.min()
        vmax=img.max()
    fig, ax = plt.subplots(1,2,figsize=figsize)
    
    ax[0].imshow(img,cmap=cmap,vmin=vmin, vmax=vmax)
    ax[0].plot([roi[1],roi[3]],[roi[0],roi[0]],'r')
    ax[0].plot([roi[3],roi[3]],[roi[0],roi[2]],'r')
    ax[0].plot([roi[1],roi[3]],[roi[2],roi[2]],'r')
    ax[0].plot([roi[1],roi[1]],[roi[0],roi[2]],'r')
    ax[0].set_title(title)
    subimg=img[roi[0]:roi[2],roi[1]:roi[3]]
    ax[1].imshow(subimg,cmap=cmap,extent=[roi[0],roi[2],roi[1],roi[3]],vmin=vmin, vmax=vmax)
    ax[1].set_title('Magnified ROI')

    
def showHitMap(gt,pr,ax=None) :
    if ax is None :
        fig, ax = plt.subplots(1,2,figsize=(12,4))
        
    m=4*gt*pr+ 2*gt*(1-pr) + 3*(1-gt)*pr + (1-gt)*(1-pr)
    clst = np.array([[64,64,64],
                     [51, 204, 255],
                     [255, 0, 102],
                     [255, 255,255]])/255.0
    cmap = colors.ListedColormap(clst)
    mi=ax[1].imshow(m, cmap=cmap,interpolation='none')
    cb=plt.colorbar(mi,ax=ax[1],ticks=[1.35, 2.1, 2.85,3.6], shrink=0.75); 
    cb.ax.set_yticklabels(['True Negative', 'False Negative', 'False Positive', 'True Positive']);
    ax[1].set_title('Hit map')
    
    cmat = confusion_matrix(gt.ravel(), pr.ravel(), normalize='all')
    heatmap(cmat, annot=True,ax=ax[0]); ax[0].set_title('Confusion matrix');
    ax[0].set_xticklabels(['Negative','Positive']);
    ax[0].set_yticklabels(['Negative','Positive']);
    ax[0].set_ylabel('Ground Truth')
    ax[0].set_xlabel('Prediction');
    
def showHitCases(gt,pr,ax=None, cmap='viridis') :
    if ax is None :
        fig,ax = plt.subplots(1,4,figsize=(15,5))
        
    ax[0].imshow(gt*pr,cmap=cmap,interpolation='none'), ax[0].set_title('True Positive')
    ax[1].imshow(gt*(1-pr),cmap=cmap,interpolation='none'), ax[1].set_title('False Negative')
    ax[2].imshow((1-gt)*pr,cmap=cmap,interpolation='none'), ax[2].set_title('False Positive')
    ax[3].imshow((1-gt)*(1-pr),cmap=cmap,interpolation='none'), ax[3].set_title('True Negative')
    