#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np
import matplotlib.pyplot as plt

import rasterio
from rasterio.plot import show
from rasterio.mask import mask
from shapely.geometry import shape
import time
import multiprocessing as mp


# In[2]:


path_in = '/home/tomas/Escritorio/Doctorado/Cursos/2022_HPC/data/folder_in/'
path_out = '/home/tomas/Escritorio/Doctorado/Cursos/2022_HPC/data/folder_out/'


# In[3]:


band1 = rasterio.open(path_in +'red-002.tif')
band2 = rasterio.open(path_in + 'nir-003.tif')


# In[4]:


band1_red = band1.read().squeeze()
band1_red.shape


# In[5]:


band2_nir = band2.read().squeeze()
band2_nir.shape


# In[6]:


def ndvi(red_nir):
    red, nir = red_nir
    return (nir - red) / (nir + red)


# In[11]:


imagen = zip(band1_red, band2_nir)


# In[8]:


P = mp.cpu_count()

pool = mp.Pool(processes=P)
get_ipython().run_line_magic('time', 'res = pool.map(ndvi, imagen)')

pool.close()
pool.join()

print("cpu_count", P)
#print("Resultado:", res)

