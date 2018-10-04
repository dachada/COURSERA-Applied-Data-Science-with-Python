
# coding: utf-8

# # Practice Assignment: Understanding Distributions Through Sampling
# 
# ** *This assignment is optional, and I encourage you to share your solutions with me and your peers in the discussion forums!* **
# 
# 
# To complete this assignment, create a code cell that:
# * Creates a number of subplots using the `pyplot subplots` or `matplotlib gridspec` functionality.
# * Creates an animation, pulling between 100 and 1000 samples from each of the random variables (`x1`, `x2`, `x3`, `x4`) for each plot and plotting this as we did in the lecture on animation.
# * **Bonus:** Go above and beyond and "wow" your classmates (and me!) by looking into matplotlib widgets and adding a widget which allows for parameterization of the distributions behind the sampling animations.
# 
# 
# Tips:
# * Before you start, think about the different ways you can create this visualization to be as interesting and effective as possible.
# * Take a look at the histograms below to get an idea of what the random variables look like, as well as their positioning with respect to one another. This is just a guide, so be creative in how you lay things out!
# * Try to keep the length of your animation reasonable (roughly between 10 and 30 seconds).

# In[1]:

import matplotlib.pyplot as plt
import numpy as np

get_ipython().magic('matplotlib notebook')

# generate 4 random variables from the random, gamma, exponential, and uniform distributions
x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000)+7
x4 = np.random.uniform(14,20, 10000)

# plot the histograms
plt.figure(figsize=(9,3))
plt.hist(x1, normed=True, bins=20, alpha=0.5)
plt.hist(x2, normed=True, bins=20, alpha=0.5)
plt.hist(x3, normed=True, bins=20, alpha=0.5)
plt.hist(x4, normed=True, bins=20, alpha=0.5);
plt.axis([-7,21,0,0.6])

plt.text(x1.mean()-1.5, 0.5, 'x1\nNormal')
plt.text(x2.mean()-1.5, 0.5, 'x2\nGamma')
plt.text(x3.mean()-1.5, 0.5, 'x3\nExponential')
plt.text(x4.mean()-1.5, 0.5, 'x4\nUniform')


# In[19]:

import matplotlib.animation as animation

def update(curr):
    if curr==n: 
        a.event_source.stop()
    ax1.cla()
    ax2.cla()
    ax3.cla()
    ax4.cla()
    ax1.hist(x1[:curr]+2.5,bins=bins, normed=True, alpha=0.5)
    ax2.hist(x2[:curr]-5, bins=bins, normed=True, alpha=0.5)
    ax3.hist(x3[:curr]-12, bins=bins, normed=True, alpha=0.5)
    ax4.hist(x4[:curr]-14, bins=bins, normed=True, alpha=0.5)
    plt.axis([-5,5,0,0.7])
    '''ax1.set_title('x1 Normal')
    ax2.set_title('x2 Gamma')
    ax3.set_title('x3 Exponential')
    ax4.set_title('x4 Uniform')'''
    ax1.annotate('x1 Normal\nn={}'.format(curr),[1,0.55])
    ax2.annotate('x2 Gamma\nn={}'.format(curr),[1,0.55])
    ax3.annotate('x3 Exponential\nn={}'.format(curr),[1,0.55])
    ax4.annotate('x4 Uniform\nn={}'.format(curr),[1,0.55])
        
n=100
fig, ((ax1, ax2),(ax3, ax4)) = plt.subplots(2,2,sharex=True, sharey=True)
bins = np.arange(-5,5,0.5)
a = animation.FuncAnimation(fig, update, interval=5)


# In[ ]:



