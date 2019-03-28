#!/usr/bin/env python
# coding: utf-8

# ## Genetic Algorithm
# * Selection
# * Crossover
# * Mutation

# In[2]:


import numpy as np
import random


# In[ ]:


def fitness_fn(route, dist_mat):
    return 2


# In[ ]:


def selection(scores):
    return 2


# In[ ]:


def crossover(m,n):
    return n


# In[ ]:


def mutate(route, prob, dist_mat):
    return route


# In[52]:


def create_random_citymap(prob_sparse,size):
# Create random city map
#    represented using adjacency matrix, symmetrc

    dist_max = 10
    dist_mat = np.zeros((size,size))
    
    for i in range(0,size):
        for j in range (0,i):
            if random.random() > prob_sparse:
                dist_mat[i][j] = int(random.random()*dist_max)
                dist_mat[j][i] = dist_mat[i][j]
    return dist_mat


# np.random.randint(5, size=(2, 4))
# array([[4, 0, 2, 1],
#       [3, 2, 2, 0]])


# In[67]:


dm = create_random_citymap(0.01,5)
dm


# In[180]:


def rand_soln(dist_mat):
    #
    start = 0
    end = len(dist_mat) - 1
    
    route = np.array([start], dtype=int) # np.zeros(1, dtype=int)
    
    b_val = True
    pos = 0
    
    while b_val:
        values  = np.nonzero(dist_mat[route[pos]])
        rand_val = random.randint(0,len(values[0])-1)
        route = np.append(route, values[0][rand_val])
        
        if route[pos+1] == end :
            b_val = False
        else:
            pos += 1
    
    return route


# In[135]:


np.nonzero(dm[1])


# In[204]:


rand_soln(dm)


# In[ ]:




