from matrix_solver import jacobi_calc, gauss_seidel_calc
from myMatrixTools import print_matrix


def main():
    tol = 1e-16

    n = int(input("enter matrix squared size (positive integer) : "))

    x = []
    for i in range(0, n):
        x.append(0)

    a = []
    b = []
    print("Insert a ,matrix values ({0} value for {0} rows)".format(n))
    for i in range(n):
        row = []
        print("row number {} :".format(i+1))
        for j in range(n):
            row.append(float(input()))
        a.append(row)

    print_matrix(a)

    print("Insert b matrix values ({0} values)".format(n))
    for i in range(0, n):
        ele = int(input())
        b.append(ele)

    methods = {0: gauss_seidel_calc, 1: jacobi_calc}
    method = int(input("\nTo solve with Gauss-Seidel method PRESS 0\nTo solve with Jacobi method PRESS 1\n"))

    if method in methods:
        sol, rel_diff, k = methods[method](a, b, x, tol)
        print('\nSolution : {0}\nRelative Difference : {1}\nIterations : {2}'.format(sol, rel_diff, k))
    else:
        print('invalid value selected')
        exit(-1)


if __name__ == "__main__":
    main()
