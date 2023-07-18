#!/usr/bin/env python
# coding: utf-8

# In[1]:


class dsatur:
    V = [] #Vertices
    T = {} #Neighbor
    D_Satur = {}
    available = {}
    alr = {}
    


# In[2]:


def Vertice(G, v):  #Confirming whether the neighboring vertices is less or bigger in degree
    G.V += [v]
    G.T[v] = []
    G.D_satur[v] = 0
    G.alr[v] = None


# In[3]:


def Connecting_Vertices(G, a, b): #Connecting the vertices to form a graph
    if not a in G.V:
        G.Vertice(a)
    if not b in G.V:
        G.Vertice(b)
    G.T[a]+=[b]
    G.T[b]+=[a]


# In[4]:


def choose(G):  #Assigning the degree for the color
    n = -1
    for i in G.V:
        if G.available[i]:
            if n == -1:
                n=i
            elif G.D_Satur[i]>G.D_Satur[n]:
                n = i
            elif G.D_Satur[i]==G.D_Satur[n]and len(G.T[i])>len(G.T[n]):
                n = i
    return n


# In[5]:


def dsatur(G):  #Programing DSatur program with assigning colors
    for n in G.V:
        G.available[u] = True
    while True in G.available.values():
        n = G.choose()
        print('choose:', n)
        G.available[n] = False
        color.available = ['red', 'blue', 'green', 'black']
        
        for neighbor in G.T[n]:
            G.D_Satur[neighbor]+=1
            if G.alr[neighbor] in color.available:
                color.available.remove(G.alr[neighbor])
        print('color:', color.available)
        G.alr[n] = color.available[0]
        print(n, ':', G.alr[n])
        print()
        
        

