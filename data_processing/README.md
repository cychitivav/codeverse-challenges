# Data manipulation and transformation course
The information in this directory is the result of the course given by [Platzi](https://platzi.com/clases/2912-pandas-numpy/47974-por-que-numpy-y-pandas/).

### Why NumPy and Pandas?
#### Why NumPy?
* It is a library focused on numerical computation and array handling.
* It is very fast, up to 50 times faster than using a Python or C list.
* It optimizes memory storage.
* In addition, it handles different types of data.
* It is a very powerful library, you can create neural networks from scratch.

#### Why Pandas?
* Pandas is focused on data manipulation and analysis.
* It is built on top of fast NumPy.
* It requires little code to manipulate data.
* Supports multiple file formats.
* It sorts the data in an intelligent alignment.
* You can handle large amounts of data, do analytics and create dashboards.

The way to import these libraries is as follows:

```python	
import numpy as np
import pandas as pd
```

## NumPy
NumPy is a library that allows us to work with arrays, matrices and vectors. It is very useful for data manipulation and analysis.

### Creating arrays
Arrays are the most basic data structure in NumPy. They are similar to lists, but they are more efficient and have more functions. To create an array, we use the `np.array()` function.

```python
arr = np.array([1, 2, 3, 4, 5])
```	
