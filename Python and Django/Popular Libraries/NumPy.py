import numpy as np 

# 1. Arrays
# Create NumPy Array
my_list=[1,2,3]
np.array(my_list)

my_matrix=[[1,2],[1,2],[3,4]]
np.array(my_matrix)

zerotofour=np.arange(0,5)
print(zerotofour)

zeros=np.zeros(3)
ones=np.ones(3)
print(zeros)
print(ones)

identity=np.eye(4)
print(identity)

# 2. Create random data
rand=np.random.rand(5,2) # returns numbers uniformly distributed between 0 and 1
print(rand)
rand=np.random.randn(5,2) # returns numbers normally distributed between 0 and 1
print(rand)
rand=np.random.randint(1,100,10)
print(rand)

# 3. Reshape an array
array=np.arange(0,100)
array=array.reshape(10,10)
print(array)
array=array.reshape(2,50)
print(array)
print(array.shape) #returns dimensions

print(array.argmax()) # returns max value

# 4. Array math
array=np.arange(0,10)
rand=np.random.randint(1,100,10)
print(array)
print(rand)
new=array+rand
print(new)
