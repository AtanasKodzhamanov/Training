# Python's built-in heap module, heapq, differs from the standard implementation of a heap in two ways. 
# Firstly, it uses zero-based indexing, and this means that it stores the root node at index zero instead 
# of the size of the heap. As a result, the relationship between the index of the children and parent nodes 
# is slightly different. Secondly, the built-in heapq module does not offer a direct way to create a max heap.
# Instead, we must modify the value(s) of each element when inserting it into the heap and when removing it
# from the heap. For example, multiply everything by -1


import heapq

# Construct an empty Min Heap
minHeap = []
heapq.heapify(minHeap)

# Construct an empty Max Heap
# As there are no internal functions to construct a Max Heap in Python,
# So, we will not construct a Max Heap.

# Construct a Heap with Initial values
# this process is called "Heapify"
# The Heap is a Min Heap
heapWithValues = [3,1,2]
heapq.heapify(heapWithValues)

# Trick in constructing a Max Heap
# As there are no internal functions to construct a Max Heap
# We can multiply each element by -1, then heapify with these modified elements.
# The top element will be the smallest element in the modified set,
# It can also be converted to the maximum value in the original dataset.
# Example
maxHeap = [1,2,3]
maxHeap = [-x for x in maxHeap]
heapq.heapify(maxHeap)
# The top element of maxHeap is -3
# Convert -3 to 3, which is the maximum value in the original maxHeap

# Insert an element to the Min Heap O(log N)
heapq.heappush(minHeap, 5)

# Insert an element to the Max Heap
# Multiply the element by -1
# As we are converting the Min Heap to a Max Heap
heapq.heappush(maxHeap, -1 * 5)

# Get top element from the Min Heap O(1)
# i.e. the smallest element
minHeap[0]
# Get top element from the Max Heap
# i.e. the largest element
# When inserting an element, we multiplied it by -1
# Therefore, we need to multiply the element by -1 to revert it back
-1 * maxHeap[0]

# Delete top element from the Min Heap O(log N)
heapq.heappop(minHeap)

# Delete top element from the Max Heap
heapq.heappop(maxHeap)

# Length of the Min Heap O(1)
len(minHeap)

# Length of the Max Heap
len(maxHeap)