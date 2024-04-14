import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

def target(n,size):
    x,y=np.meshgrid(np.linspace(-1,1,size),np.linspace(-1,1,size))
    r = np.sqrt(x**2+y**2)
    img = (0<np.cos(np.pi*r*n))*(r<1)
    
    return img

def hit_pattern(x,y,s,N) :
    xx=x+np.random.normal(size=N)*s
    yy=y+np.random.normal(size=N)*s
    
    return xx,yy

def precacc(N,labels=['Low accuracy','High accuracy','Low precision','High precision'],figsize=[10,8],fontsize=15):
    cm=['white','crimson']
    rw=colors.ListedColormap(cm)

    cases = [[0.25,0.3,0.1],
            [0.25,0.3,0.02],
            [0.5,0.5,0.1],
            [0.5,0.5,0.02]]
    fig,axes=plt.subplots(2,2,figsize=figsize)
    axes=axes.ravel()
    for ax,h in zip(axes,cases) :
        x,y = hit_pattern(N*h[0],N*h[1],N*h[2],20)
        ax.imshow(target(5,N),cmap=rw)
        ax.scatter(x,y,s=25,color='black')
        for name in ['left','right','top','bottom'] :
            ax.spines[name].set_visible(False)
        ax.set_xticks([])
        ax.set_yticks([])

    axes[0].set_ylabel(labels[0],fontsize=fontsize)
    axes[2].set_ylabel(labels[1],fontsize=fontsize)
    axes[2].set_xlabel(labels[2],fontsize=fontsize)
    axes[3].set_xlabel(labels[3],fontsize=fontsize);