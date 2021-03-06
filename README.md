# Jacobi & Gauss-Seidel Algorithms Using Python

#### The following methods solve the line system of
#### equations, Ax=b,using Jacobi OR Gauss-Seidel algorithms, 
#### starting from an initial guess, ``x0``.
#
##### The algorithms will terminate when the change in x is less than ``tolerance``, or
##### if ``max_iter`` [default=200] iterations have been exceeded.
#
**_For each function:  (jacobi_calc() or gauss_seidel_calc())_**
#
  **Receives 5 parameters :**
1.  **_a_**, the NxN matrix that the method is being performed on.
          if a is None or NxM, where N != M - the functions returns None.
2.  **_b_**, vector of solution. if _b_ is None - the functions returns None.
3. **_x_**,  the desired initial guess.
          if _x_ is None, the initial guess will bw determined as a vector of 0's.
4.  **_tolerance_**, the desired limitation of tolerance of solution's anomaly.
          if _tolerance_ is None, the default value will set as 1e-16.
5.  **_max_iter_**, the maxim number of possible iterations to receive the most exact solution.
          if _max_iter_ is None, the default value will set as 200.
#
  **Returns 3 variables :**
1. **_x_**, the estimated solution.
2.  **_rel_diff_**, the relative difference between last 2
          iterations for x.
3. **_k_**, the number of iterations used. If _k=max_iter_,
          then the required tolerance was not met.
#
**included files :**
- **main.py** - contains basic usage demonstration of jacobi_calc() or gauss_seidel_calc(), using a 3x3 matrix, and basic arguments.
- **main2.py** - constains larger user-input of size _N_, matrix _a_ and vector _b_
- **myMatrixTools.py** - constains few basic matrix manipulation and analysis functions for usage.
#
**requirments :**
- python>3.0
- Numpy version 1.19.3 (previous to 1.19.4 -> had some issues initializing it)
- all input should be valid (n/N = ints, the rest can be floats) -> no validations were made
- all functions, **myMatrixTools.py** functions infcluded, must recieve valid parameters! -> no validations were made
