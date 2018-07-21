
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm
def plot_qubo(mat, logscale=False, offset=1.1, title="Plot of QUBO values"):
    """
    Args:
        mat: numpy NDArray
            n x n QUBO matrix as a Numpy NDArray
        offset: float
            To keep colorbar away from zero, must be > 1
            (even log(1) gets a 'non-positive' value complaint from colorbar)
        title: str
            Optional, text describing the plot in the title

    Returns: :class:`matplotlib.figure.Figure`
    """
    fig = plt.figure(figsize=(8, 6))
    ax = fig.gca()
    ax.set_title(title)

    if logscale:
        norm = LogNorm(vmin=offset + mat.min(), vmax=offset + mat.max())
        im = ax.matshow(offset + mat, cmap='PuBu_r', norm=norm)
    else:
        im = ax.matshow(mat, cmap='PuBu_r')

    fig.colorbar(im, ax=ax, extend='max')
    return fig
import pickle as pkl 

with open("clique_cover_qubo_mat.pkl", 'rb') as fh:
    q = pkl.load(fh)


# In[2]:


plot_qubo(q)


# In[14]:





# In[31]:


import networkx as nx

Gvc = nx.from_numpy_matrix(q)
nx.draw_networkx(Gvc)


# In[19]:


q=[list(i) for i in q]


# In[4]:


qzo = [[0 if i ==0. else 1 for i in q[j]] for j in range(len(q))]


# In[20]:


A=nx.adjacency_matrix(Gvc)


# In[6]:


A


# In[27]:


t=list(nx.all_node_cuts(Gvc))


# In[22]:


t


# In[28]:


Gvc.remove_node(16)
Gvc.remove_node(25)
Gvc.remove_node(26)
Gvc.remove_node(27)


# In[29]:


nx.draw_networkx(Gvc)

