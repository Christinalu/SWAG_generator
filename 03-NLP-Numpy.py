#-----------NLP Crash Course--------------
#------CMPT 340: Biomedical Imaging-------
#-----------------------------------------
#-----------------------------------------
#-----------------------------------------
#--------------SECTION 3:-----------------
#----------------Numpy--------------------
#*****************************************
#---Overview of sections:-----------------
#---3.1 Importing Libraries
#---3.2 Examining the ndarray
#---3.3 Memory Usage
#---3.4 Important functions in numpy
#---3.5 Generating zeros function
#---3.6 Linspace Function
#---3.7 Random generation function
#---3.8 Reshaping Function
#---3.9 Slicing
#*****************************************
#*****************************************


# Introduction to numpy
# 3.1 Importing Libraries
import numpy as np

# Function Info:
# arange()
# np.arange([start,] stop[, step,], dtype=None)
np.arange(10)

np.arange(1,10)

np.arange(1,10,2)
np.arange(1,10,0.5)

np.arange(1,10,dtype='float64')

# 3.2 Examining the ndarray
arr = np.arange(1,10)

arr.ndim

arr.shape

arr.size
arr.dtype
arr.itemsize

# 3.3 Memory Usage
arr.itemsize * arr.size

# Why use Numpy? Compare the time to do the same operation using
# numpy and normal python lists
# %timeit list1 = range(1,1000)
# %timeit list2 = np.arange(1,1000)


# 3.4 Important functions in numpy
# List to array
np.asarray([1,2,3,4,5])

list2d = [[1,2,3],[4,5,6]]
arr2d = np.asarray(list2d)

# 3.5 Generating zeros function
# zeros(shape, dtype=float, order='C')

listzeros = np.zeros((3,4), dtype='int32')

# 3.6 Linspace Function
# np.linspace(start, stop, num=50, endpoint=True, retstep=False)

np.linspace(1,4,num=4)
np.linspace(1,4,num=8)
np.linspace(1,4,num=8,endpoint=False)

# 3.7 Random generation function
np.random.random((3,4))


# 3.7.1 Max, min, mean, median, std etc
# ***Uncomment each line and run the code***

# np.max(a, axis=None, out=None, keepdims=False)
# np.min(a, axis=None, out=None, keepdims=False)
# np.mean(a, axis=None, dtype=None, out=None, keepdims=False)
# np.median(a, axis=None, out=None, overwrite_input=False)
# np.std(a, axis=None, dtype=None, out=None, ddof=0, keepdims=False)
# np.sum(a, axis=None, dtype=None, out=None, keepdims=False)

rarr = np.random.random((3,4))

np.max(rarr, axis=0)
np.max(rarr, axis=1)

np.min(rarr, axis=0)
np.min(rarr, axis=1)

np.median(rarr, axis=0)
np.median(rarr, axis=1)

# 3.8 Reshaping Function
# np.reshape(a, newshape, order='C')
new_rarr = np.reshape(rarr, (12,))
new_rarr = np.reshape(rarr, (12,1))

# 3.9 Slicing
rarr = np.random.random((4,5))

rarr[:,:]
rarr[1:3,:]

rarr[:,1:]
rarr[:,1:3]

rarr[1:3,1:3]

rarr[[0,3],:]
rarr[:,[0,3]]


rarr[:-1,:]
rarr[-1:,:]
