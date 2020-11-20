import numpy as np
from numpy.linalg import norm
from myMatrixTools import *

"""
Performs Jacobi iterations to solve the line system of
equations, Ax=b, starting from an initial guess, ``x0``.

Terminates when the change in x is less than ``tol``, or
if ``max_iter`` [default=200] iterations have been exceeded.

Receives 5 parameters:
    1.  a, the NxN matrix that method is being performed on.
        if a is None or NxM, where N != M - the functions returns None.
    2.  b, vector of solution. if b is None - the functions returns None.
    3.  x,  the desired initial guess.
        if x is None, the initial guess will bw determined as a vector of 0's.
    4.  tolerance, the desired limitation of tolerance of solution's anomaly.
        if tolerance is None, the default value will set as 1e-16.
    5.  max_iter, the maxim number of possible iterations to receive the most exact solution.
        if max_iter is None, the default value will set as 200.
        
Returns 3 variables:
    1.  x, the estimated solution
    2.  rel_diff, the relative difference between last 2
        iterations for x
    3.  k, the number of iterations used.  If k=max_iter,
        then the required tolerance was not met.
"""


def jacobi_calc(a, b, x=None, tolerance=.001, max_iter=200):
    if a is None or b is None:
        return None

    if not is_matrix_square(a):
        print('Matrix IS NOT squared (NxN) - cannot preform jacobi algorithm\n')
        return None

    if is_diagonally_dominant(a):
        print('Matrix IS diagonally dominant - preforming jacobi algorithm\n')
    else:
        print('Matrix IS NOT diagonally dominant - cannot preform jacobi algorithm\n')
        return None

    if x is None:
        x = [0 for i in range(0, len(a))]

    rel_diff = 0
    x_prev = x
    k = 0

    print('Iteration  Solution')
    print('Guess\t\t' + str(x))

    while k < max_iter:

        for i in range(0, len(a)):
            subs = .0

            for j in range(0, len(a)):
                if i != j:
                    subs -= a[i][j] * x_prev[j]

            x[i] = (subs + b[i]) / a[i][i]

        difference = []
        zip_object = zip(x.copy(), x_prev.copy())

        for x_i, x_prev_i in zip_object:
            difference.append(x_i - x_prev_i)

        rel_diff = norm(np.array(difference)) / norm(x)

        if k > 0 and tolerance > rel_diff:
            break

        k = k + 1
        x_prev = x.copy()
        print(str(k) + '\t\t\t' + str(x))

    return x, rel_diff, k


"""
Performs Gauss-Siedel iterations to solve the line system of
equations, Ax=b, starting from an initial guess, ``x0``.

Terminates when the change in x is less than ``tol``, or
if ``max_iter`` [default=200] iterations have been exceeded.

Receives 5 parameters:
    1.  a, the NxN matrix that method is being performed on.
        if a is None or NxM, where N != M - the functions returns None.
    2.  b, vector of solution. if b is None - the functions returns None.
    3.  x,  the desired initial guess.
        if x is None, the initial guess will bw determined as a vector of 0's.
    4.  tolerance, the desired limitation of tolerance of solution's anomaly.
        if tolerance is None, the default value will set as 1e-16.
    5.  max_iter, the maxim number of possible iterations to receive the most exact solution.
        if max_iter is None, the default value will set as 200.
        
Returns 3 variables:
    1.  x, the estimated solution
    2.  rel_diff, the relative difference between last 2
        iterations for x
    3.  k, the number of iterations used.  If k=max_iter,
        then the required tolerance was not met.
"""


def gauss_siedel_calc(a, b, x=None, tolerance=1e-16, max_iter=200):
    if a is None or b is None:
        return None

    if not is_matrix_square(a):
        print('Matrix IS NOT squared (NxN) - cannot preform jacobi algorithm\n')
        return None

    if is_diagonally_dominant(a):
        print('Matrix IS diagonally dominant - preforming jacobi algorithm\n')
    else:
        print('Matrix IS NOT diagonally dominant - cannot preform jacobi algorithm\n')
        return None

    if a is None or b is None:
        return None

    if x is None:
        x = [0 for i in range(0, len(a))]

    x_prev = x
    k = 0
    rel_diff = 0
    print('Iteration  Solution')
    print('Guess\t\t' + str(x))

    while k < max_iter:

        for i in range(0, len(a)):
            x_prev[i] = x[i]
            x[i] = b[i]

            for j in range(0, len(a)):
                if i != j:
                    x[i] -= a[i][j] * x[j]

            x[i] = x[i] / a[i][i]

        difference = []
        zip_object = zip(x.copy(), x_prev.copy())

        for x_i, x_prev_i in zip_object:
            difference.append(x_i - x_prev_i)

        rel_diff = norm(np.array(difference)) / norm(x)

        if k > 0 and tolerance > rel_diff:
            break

        k = k + 1
        x_prev = x.copy()
        print(str(k) + '\t\t\t' + str(x))

    return x, rel_diff, k
