import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.colors as colors
from sklearn.metrics import confusion_matrix
# from seaborn import heatmap
import numpy as np

def buildCMap(plots) :
    cmaplist = []

    for p0 in plots :
        cmaplist.append(p0.get_color())
        
    return ListedColormap(cmaplist)

def heatmap(img, ax=None, cmap='inferno', fontsize=14, precision=3) :
    if ax is None :
        _,ax=plt.subplots(1)
        
    ax.imshow(img,cmap=cmap,origin='upper')
    ax.set(xticks=np.arange(0,img.shape[0]),yticks=np.arange(0,img.shape[0]))
    props = dict(boxstyle='round', facecolor='lightgray', alpha=1) 
    for i in range(img.shape[1]):
        for j in range(img.shape[0]):
            text = ax.text(j, i, "{0:0.{1}f}".format(img[i, j],precision),
                           ha="center", va="center", fontsize=fontsize, color="k",bbox=props)

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

    
def showHitMap(gt,pr,ax=None, annot_kws = None) :
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
    heatmap(cmat, annot=True,ax=ax[0], annot_kws=annot_kws); ax[0].set_title('Confusion matrix');
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
    
def visualize_normalization(img, ob, dc,norm) :
    m, s  = img.mean(), img.std()
    mo,so = ob.mean(), ob.std()
    md,sd = dc.mean(), dc.std()
    mn,sn = norm.mean(),norm.std()
    
    fig = plt.figure(figsize=(10,4))
    ax1 = plt.subplot2grid(shape=(2, 4), loc=(0, 0))
    ax2 = plt.subplot2grid(shape=(2, 4), loc=(0, 1))
    ax3 = plt.subplot2grid(shape=(2, 4), loc=(1, 0))
    ax4 = plt.subplot2grid(shape=(2, 4), loc=(1, 1))
    ax5 = plt.subplot2grid((2, 4), (0, 2), colspan=2,rowspan=2)

    ax1.imshow(img,clim=[m-s,m+s],cmap='gray')
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax1.set_title('Measured')

    ax2.imshow(dc,clim=[md-2*sd,md+2*sd],cmap='gray')
    ax2.set_xticks([])
    ax2.set_yticks([])
    ax2.set_title('Bias')

    ax3.imshow(ob,clim=[mo-2*so,mo+2*so],cmap='gray')
    ax3.set_xticks([])
    ax3.set_yticks([])
    ax3.set_title('Source profile')
    

    ax4.imshow(dc,clim=[md-2*sd,md+2*sd],cmap='gray')
    ax4.set_xticks([])
    ax4.set_yticks([])
    ax4.set_title('Bias')
    

    ax5.imshow(norm,clim=[mn-5*sn,1],cmap='gray')
    ax5.set_xticks([])
    ax5.set_yticks([]);
    ax5.set_title('Normalized')
    

    ax1.annotate('-',
                xy=(0.24, 0.63), xycoords='figure fraction',
                horizontalalignment='center', verticalalignment='center',
                fontsize=50)

    ax3.annotate('-',
                xy=(0.24, 0.215), xycoords='figure fraction',
                horizontalalignment='center', verticalalignment='center',
                fontsize=50)

    ax5.annotate('=',
                xy=(0.5, 0.43), xycoords='figure fraction',
                horizontalalignment='center', verticalalignment='center',
                fontsize=30)

    ax1.annotate('', xy=(0.01, 0.43), xycoords='figure fraction', xytext=(0.47,0.43),
    arrowprops=dict(arrowstyle="-",lw=2))
    plt.tight_layout()

    