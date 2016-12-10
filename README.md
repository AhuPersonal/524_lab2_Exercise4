[![Build Status](https://travis-ci.org/AhuPersonal/524_lab2_Exercise4.svg?branch=master)](https://travis-ci.org/AhuPersonal/524_lab2_Exercise4)

# Find Prime Package

findprime package is designed to find prime numbers in given the range.


#### Installation

Start the command line  

`pip install git+git://github.com/AhuPersonal/524_lab2_Exercise4.git`

OR

`pip install git+https://github.com/AhuPersonal/524_lab2_Exercise4.git`


#### Usage

This package contains **find** function, you can specify lower and upper range values to this function the find out the result:

```
# Import package and function
from findprime import find

# Get prime number list
numbers = find(1,10)

# Print the number list
print(numbers)
[2, 3, 5, 7]
```

**Test Cases:**

This package has a integrated built-in test cases to validate the results. Exceptions are not handled inside the package and are expected to be handled by the caller.
TypeExceptions are tested in the package.