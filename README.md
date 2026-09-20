NumPy - Numerical Python

What is NumPy?



-NumPy is the fundamental package for numerical computing in Python. It provides a powerful N-dimensional array object (ndarray) and tools for working with these arrays. -NumPy is the foundation for most scientific Python libraries and is essential for data science, machine learning, and scientific computing.

Why Choose NumPy?
->Performance: NumPy is much faster than Python lists for numerical calculations, especially when working with large amounts of data.
->Memory Efficiency: NumPy arrays use less memory than Python lists because they store data in a more efficient way.
->Vectorization: NumPy allows us to perform operations on entire arrays without using lengthy for loops, making code shorter and easier to understand.
->Broadcasting: NumPy can perform calculations between arrays of different shapes without manually changing their sizes.
->Integration: NumPy works well with libraries like Pandas, SciPy, Matplotlib, and Scikit-learn, making it very useful for data science and machine learning.
->Open Source: NumPy is free to use and has a large community that continuously develops and improves the library.

-Installation
Using pip (recommended)
-bash
pip install numpy
Using conda
bash
conda install numpy
From source
bash
git clone https://github.com/numpy/numpy.git
cd numpy
pip install -e .
Quick Start
Creating Arrays
python

import numpy as np

# From a list
arr = np.array([1, 2, 3, 4, 5])

# Common initialization methods
zeros = np.zeros((3, 4))           # 3x4 matrix of zeros
ones = np.ones((2, 3))             # 2x3 matrix of ones
range_arr = np.arange(0, 10, 2)    # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5)    # 5 evenly spaced numbers from 0-1
random_arr = np.random.rand(3, 3)  # 3x3 random matrix
Array Properties
python
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr.ndim)      # Number of dimensions: 2
print(arr.shape)     # Shape: (2, 3)
print(arr.size)      # Total elements: 6
print(arr.dtype)     # Data type: int64
Indexing and Slicing
python
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Basic indexing
print(arr[0])        # First element: 0
print(arr[-1])       # Last element: 9

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])     # First element: 10
print(arr[-1])    # Last element: 50
print(arr[2])     # Element at index 2: 30

# Slicing
print(arr[2:5])      # Elements from index 2 to 4: [2, 3, 4]
print(arr[::2])      # Every other element: [0, 2, 4, 6, 8]

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

print(arr[2:5])   # [2, 3, 4]
print(arr[:4])    # First 4 elements: [0, 1, 2, 3]
print(arr[5:])    # From index 5: [5, 6, 7, 8, 9]
print(arr[::2])   # Every other element: [0, 2, 4, 6, 8]
print(arr[::-1])  # Reverse array

# 2D indexing
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix[0, 1])  # Row 0, Column 1: 2
print(matrix[:, 1])  # All rows, Column 1: [2, 5]
Mathematical Operations
python
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print(matrix[0, 1])  # Row 0, Column 1: 2
print(matrix[1, 2])  # Row 1, Column 2: 6
print(matrix[:, 1])  # All rows, Column 1: [2, 5]
print(matrix[0, :])  # All columns of Row 0: [1, 2, 3]

# Element-wise operations
print(a + b)         # [6, 8, 10, 12]
print(a * b)         # [5, 12, 21, 32]
print(np.sqrt(a))    # [1., 1.41421356, 1.73205081, 2.]

# Matrix operations
matrix = np.array([[1, 2], [3, 4]])
print(matrix.T)      # Transpose
print(np.dot(matrix, matrix))  # Matrix multiplication

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(a + b)       # [6, 8, 10, 12]
print(a - b)       # [-4, -4, -4, -4]
print(a * b)       # [5, 12, 21, 32]
print(a / b)       # [0.2, 0.333..., 0.428..., 0.5]
print(a ** 2)      # [1, 4, 9, 16]
print(np.sqrt(a))  # [1., 1.414..., 1.732..., 2.]

Aggregation Functions
python
arr = np.array([1, 2, 3, 4, 5])

print(np.sum(arr))      # Sum: 15
print(np.mean(arr))     # Mean: 3.0
print(np.std(arr))      # Standard deviation: 1.41421356
print(np.min(arr))      # Minimum: 1
print(np.max(arr))      # Maximum: 5
Reshaping and Flattening
python
arr = np.arange(12)

arr = np.array([1, 2, 3, 4, 5])

print(np.sum(arr))   # 15
print(np.mean(arr))  # 3.0
print(np.std(arr))   # 1.414...
print(np.min(arr))   # 1
print(np.max(arr))   # 5


# Reshape
reshaped = arr.reshape(3, 4)      # Convert to 3x4 matrix

# Flatten
flattened = reshaped.flatten()    # Convert back to 1D

# Ravel (returns view, more efficient)
raveled = reshaped.ravel()
Broadcasting
python
# Operations on arrays of different shapes
matrix = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 2
print(matrix * scalar)  # Each element multiplied by 2

column = np.array([[1], [2]])
print(matrix + column)  # Broadcasts column across all rows
Boolean Indexing
python
arr = np.array([1, 2, 3, 4, 5, 6])

# Filter elements greater than 3
mask = arr > 3
print(arr[mask])       # [4, 5, 6]

# Complex conditions
print(arr[(arr > 2) & (arr < 6)])  # [3, 4, 5]
Core Topics
✅ Array creation and initialization
✅ Array properties (dimensions, shape, size, dtype)
✅ Type conversion with astype()
✅ Advanced indexing and slicing techniques
✅ Array manipulation (reshape, flatten, ravel)
✅ Copy vs View semantics
✅ Random number generation
✅ Mathematical operations (arithmetic, trigonometric, logarithmic)
✅ Aggregation functions (sum, mean, std, min, max)
✅ Sorting and searching
✅ Broadcasting rules and advanced broadcasting
✅ Array stacking and splitting
✅ Linear algebra operations
✅ Fourier transforms
✅ Polynomial fitting
Performance Comparison
python
import numpy as np
import time

# Python list approach
python_list = list(range(1000000))
start = time.time()
sum(python_list)
print(f"Python list: {time.time() - start:.6f}s")

# NumPy approach
numpy_arr = np.arange(1000000)
start = time.time()
numpy_arr.sum()
print(f"NumPy array: {time.time() - start:.6f}s")
# NumPy is typically 10-100x faster
Common Use Cases
Data Science & Analysis

Process large datasets efficiently with vectorized operations

Machine Learning

Numerical backbone for TensorFlow, PyTorch, Scikit-learn

Scientific Computing

Physics simulations, climate modeling, bioinformatics

Financial Analysis

Time series analysis, portfolio optimization, risk modeling

Image Processing

Manipulate and analyze image data

Documentation & Resources
📚 Official NumPy Documentation
🎓 NumPy User Guide
💻 NumPy Tutorials
🐛 Issue Tracker
💬 NumPy Discourse
Contributing

We welcome contributions! Please see CONTRIBUTING.md for guidelines.

Development Setup
bash
git clone https://github.com/numpy/numpy.git
cd numpy
pip install -e ".[dev]"
pytest numpy
Citation

If you use NumPy in your research, please cite it:

bibtex
@article{Harris2020array,
  title={Array programming with NumPy},
  author={Harris, Charles R and others},
  journal={Nature},
  volume={585},
  pages={357--362},
  year={2020}
}
License

NumPy is licensed under the BSD 3-Clause License

Acknowledgments

NumPy is developed by a community of contributors and is maintained by the NumPy team. We thank all contributors who have helped make NumPy what it is today.

Ready to get started? Install NumPy with pip install numpy and explore the official documentation.
