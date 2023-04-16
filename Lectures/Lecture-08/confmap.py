import numpy as np
import matplotlib.pyplot as plt

def cdf(x,m,s) :
    return 0.5*(1+spec.erf((x-m)/(s*np.sqrt(2))))

def cdfc(x,m,s) :
    return 0.5*(spec.erfc((x-m)/(s*np.sqrt(2))))

def gaussian(x,m,s) :
    return 1/(np.sqrt(2*np.pi)*s)*np.exp(-(x-m)**2/(2*s**2))

def multi_gaussian(x,m,s) :
    return np.exp(-(x-m)**2/(2*s**2))

def multi_gaussian_plot(m,s) :
    if len(m) != len(s) :
        raise ValueError("Arguments have different lengths!")
        
    x_min = m.min()-3*s.max()
    x_max = m.max()+3*s.max()
    
    x=np.linspace(x_min,x_max,1000)
    
    #xx,yy = np.meshgrid(x,np.arange(len(m)))
    w = np.zeros([len(m),len(x)])
    
    for idx,(mm,ss) in enumerate(zip(m,s)) :
        w[idx]=np.exp(-(x-mm)**2/(2*ss**2))
    

    return x,w

def plot_thresholded_gaussians(m,s,gamma,ax=None) :
    if ax is None :
        fig,ax=plt.subplots(1)
        
        
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    
    if m[1]<m[0] :
        m[0],m[1] = m[1],m[0]
        s[0],s[1] = s[1],s[0]
        
    x,w = multi_gaussian_plot(m,s)
    
    # Visualization
    gidx = np.abs(x - gamma).argmin()
    
    ax.fill(x,w[1],label='True positive',alpha=0.3,ec=colors[0],lw=2)
    ax.fill(x,w[0],label='True negative',alpha=0.3,ec=colors[1],lw=2)

    ax.vlines([x[gidx]],ymin=0,ymax=1,color='magenta',label='Threshold $\gamma$={0}'.format(gamma))

    ax.fill_between(x[:gidx],0,w[1,:gidx],color=colors[2],label='False negative',alpha=0.3,ec=colors[2],lw=2)
    ax.fill_between(x[gidx:],0,w[0,gidx:],color=colors[3],label='False positive',alpha=0.3,ec=colors[3],lw=2)

    ax.legend();
    
def conf_plot(m,s) :
    if len(m) != len(s) :
        raise ValueError("Arguments have different lengths!")
        
    x_min = m.min()-3*s.max()
    x_max = m.max()+3*s.max()
    
    x=np.linspace(x_min,x_max,1000)
    
    w = np.zeros([len(m),len(x)])
    
    for idx,(mm,ss) in enumerate(zip(m,s)) :
        w[idx]=np.exp(-(x-mm)**2/(2*ss**2))
    
    return x,w

def conf_value(x,c,m,s) :
    """ Computes the confidence for a class given its value.
    
    Parameters
    ----------
    x - Values
    c - The selected class
    m - mean value vector for the segmented classes.
    s - standard deviation vector for the segmented classes.

    The m and s vectors must have the same number of elements as the number of classes in the segmented image.
    """
    w = np.exp(-(x-m)**2/(2*s**2))

    return w[c]/w.sum()
    

def conf_map(data,segm,m,s,c=None) :
    """  Computes the confidence map of a segmented image using the original image and class statistics.

    Parameters
    ----------
    data - The original image
    segm - An image segmented from 'data'
    m    - mean value vector for the segmented classes.
    s    - standard deviation vector for the segmented classes.

    The m and s vectors must have the same number of elements as the number of classes in the segmented image.

    """
    if len(m) != len(s) :
        raise ValueError("Arguments have different lengths!")
    
    classlabels = np.unique(segm)
    if len(classlabels) != len(m) :
        raise ValueError("Number of segmented classes doesn't match m array!")
    
    if c is None :
        res = np.array([conf_value(x,int(c),m=m,s=s) for x,c in zip(data.ravel(),segm.ravel())])  
    else :
        res = np.array([conf_value(x,int(c),m=m,s=s) for x in data.ravel()])
        
    res = res.reshape(data.shape)
    
    return res
