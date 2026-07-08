import numpy as np

#Introduction to Numpy

#Checking the version
print(np.__version__)

#Take  a list
my_list = [1,2,3,4]
my_list = my_list * 2
print(my_list)

#Calling an array
array = np.array([1,2,3,4])
array = array*2
print(array)
print(type(array))

#Multidimensional Array -> A multidimensional array is an array with two or more dimensions (rows, columns, etc.).
array = np.array([[['A','B','C'], ['D','E','F'],['G','H','I']]
                  ,[['J','k','L'],['M','N','O'],['P','Q','R']]
                  ,[['S','T','U'],['V','W','X'],['Y','Z',' ']]])
print(array.ndim)
print(array.shape)
print(array[0][0][1])
print(array[0,0,0])
print(array[1,1,1])
word = array[0,0,0] + array[2,0,0] + array[2,0,0]
print(word)

#Slicing -> Slicing is the process of extracting a subset of elements from a NumPy array using index ranges.

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])
# array[start:end:stop] <- slice
#row
print(array[0:4])
print(array[1:4])
print(array[0:4:2])
print(array[::-1])

#column
print(array[:,-1])

#Arithmetic -> Arithmetic operations are mathematical operations performed on NumPy arrays.
#Scalar Arithmetic -> Scalar arithmetic performs operations between every element of an array and a single scalar value.
array = np.array([1,2,3])
print(array)
print(array +1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5)

#Vectorized math functions -> Vectorized math functions apply mathematical operations to every element of an array without using loops.

arrays = np.array([1,2,3])
print(np.sqrt(array))
print(np.ceil(array))
print(np.floor(array))
print(np.round(array))
print(np.pi)

#EXERCISE
radii = np.array([1,2,3])
print(np.pi*radii**2)

#Element-wise Arithmetic -> Element-wise arithmetic performs operations between corresponding elements of two arrays having compatible shapes.

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
print(array1+array2)
print(array1*array2)
print(array1/array2)
print(array1-array2)
print(array1**array2)

#Comparison operators -> Comparison operators compare array elements with another array or value and return a Boolean array.

scores = np.array([91,89,100,92,93,95])
print(scores==100)
print(scores>=80)
print(scores<80)

#or

scores[scores<90] = 0
print(scores)

#Broadcasting -> Broadcasting is NumPy's mechanism for automatically expanding arrays with compatible shapes to perform element-wise operations.
array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3],[4]])

print(array1.shape)
print(array2.shape)
print(array1*array2)

array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(array1.shape)
print(array2.shape)

print(array1*array2)

#Aggregate Function ->  Aggregate functions combine multiple array elements into a single summary value, such as sum, mean, minimum, or maximum.
array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array))
print(np.var(array))
print(np.min(array))
print(np.max(array))
print(np.argmin(array))
print(np.argmax(array))
print(np.median(array))

print(np.sum(array,axis=0))
print(np.sum(array,axis=1))

#Filtering - Filtering in NumPy means selecting only those elements that satisfy a condition.
ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])

teenager = ages[ages<18]
print(teenager)

adults = ages[(ages>=18) & (ages < 65)]
print(adults)

senior_teenager = ages[(ages<18)|(ages>=65)]
print(senior_teenager)

seniors = ages[ages>=65]
print(seniors)

evens = ages[ages%2 ==0]
print(evens)

odds = ages[ages%2 !=0]
print(odds)

adults = np.where(ages >= 18, ages, 0)
print(adults)

#Random Numbers
rng = np.random.default_rng()
print(rng.integers(1,7))
print(rng.integers(low=1,high=7))
print(rng.integers(low=1,high=101))

#Set a size -> Number of random numbers needed
print(rng.integers(low=1,high=101, size=3)) #1D
print(rng.integers(low=1,high=101, size=(3,2))) #2D

#Set a seed
rng = np.random.default_rng(seed=1)
print(rng.integers(low=1,high=101, size=(3,2))) #Output remains same

print(np.random.uniform(low=-1, high=1, size=3))

#Shuffling the array
array = np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

#Random choice -> np.random.choice() or rng.choice() is used to randomly select element(s) from an array or list.

fruits = np.array(["banana", "coconut", "pineapple", "apple", "orange"])
#fruits = rng.choice(fruits)
fruits = rng.choice(fruits, size=(3,3))
print(fruits)

breads = np.array(["🥐","🥯","🥨","🥖","🍞"])
breads = rng.choice(breads, size=(3,3))
print(breads)