from matrix_solver import jacobi_calc, gauss_siedel_calc
from myMatrixTools import *


def main():
    tol = 0.001
    a=b=[]

    n = int(input("enter matrix squared size (positive integer) : "))

    x = [0 for n in range(n)]
    a = ([3, -1, 1],
         [0, 1, -1],
         [1, 1, -2])

    b = [4,-1,-3]

    methods ={0:gauss_siedel_calc,1:jacobi_calc}
    method = int(input("\nTo solve with Gauss-Siedel method PRESS 0\nTo solve with Jacobi method PRESS 1\n"))

    if method in methods:
        sol,rel_diff,k = methods[method](a, b, x, tol)
        print('\nSolution : {0}\nRelative Difference : {1}\nIterations : {2}'.format(sol,rel_diff,k))
    else :
        print('invalid value selected')
        exit(-1)


if __name__ == "__main__":
    main()