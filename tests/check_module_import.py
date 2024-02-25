
import astropy.io.fits as fits      # Appears in IsolineAverage
import copy                         # Appears in lectures 10 and 11
import dask_ndfilters as da_ndfilt  # Appears in lecture 11
import dask_ndmorph as ndmorph      # Appears in lecture 11
import dask.array as da             # Appears in lecture 11
import dask.bag as dbag             # Appears in lecture 11
import dask.diagnostics as diag     # Appears in lecture 11
import doctest                      # Appears in lectures 10 and 11
import functools                    # Appears in lectures 10 and 11
import graphviz                     # Appears in lecture 5
import importlib                    # Appears in lectures 8 and 10
import itertools                    # Appears in lectures 10
import matplotlib as mpl            # Appears in all lectures
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.patches as patches
import networkx as nx               # Appears in lecture 7, may not be needed
import numpy as np                  # Appears in all lectures
import os                           # Appears in lectures 1 and 6
import pandas as pd                 # Appears in all lectures
import plotly.figure_factory as FF  # Appears in lectures 4 and 6
import plotly.graph_objs as go
import plotly.offline as py
import pydot                        # Appears in lectures 1 and 9
import pyvista as pv                # Appears in lecture 11
import scipy.io as sio              # Appears in lectures 2, 3, 5, 7, 8, 9, and 11
import scipy.ndimage as ndimage
import scipy.special as spec
import scipy.stats as stats
import seaborn as sns               # Appears in lectures 6, 7, 8, 9, 10, and 11
import skimage                      # Appears in all lectures
import skimage.filters as flt       
import skimage.io as io
import skimage.morphology as morph
import skimage.restoration as res
import skimage.transform
import sklearn.tree as tree         # Appears in lecture 5
import string                       # Appears in lecture 11  
import sys                          # Appears in lecture 4 and 8
import tensorflow as tf             # Appears in lectures 2, 5, and 9
import tensorflow_datasets as tfds  # Appears in lecture 2
import tensorflow.compat.v1 as tf
import tensorflow.keras.losses as losses
import tifffile as tiff             # Appears in lectures 4 and 8
import webcolors                    # Appears in lecture 6

# Local imports
# import amglib.readers as rd # Local module
# import confmap as cm        # Local module appears in lecture 8
# import plotsupport as ps    # Local module 

# Tricky imports
import itk # appears in lecture 11
import ipyvolume as p3 # Appears in lecture 6
import SimpleITK as sitk # Appears in lecture 9
import skimage.morphology.greyreconstruct as gr # Appears in lecture 7

# import numpy
# import matplotlib.pyplot
# import scipy 
# import mpl_toolkits.mplot3d
# import skimage
# import sklearn
# import pandas
# import collections
# import sklearn.metrics
# import skimage.morphology
# import plotly.offline
# import seaborn
# import graphviz
# import keras.models
# import bokeh
# import dask
# import tqdm.notebook
# import doctest
# import IPython.display
# import dask_image.ndfilters
# import dask_image.ndmorph
# import dask.array
# import dask.dot 
# import functools
# import IPython.display
# import pydot
# import subprocess
# import tensorflow
# import sys
# import plotnine
# import itertools
# import webcolors
# import ipywidgets
# import ipyvolume
# import timeit
# import itk
# import itkwidgets
# import SimpleITK