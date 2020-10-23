# -*- encoding: utf-8 -*-
import matplotlib.pyplot as plt


def f(x):
    return 1 / (1 + x ** 2)


def lagrange(x, begin: int, end: int, n: int):
    xn = [i / n for i in range(begin * n, end * n + 1, n)]
    yn = [f(i) for i in xn]
    sum = 0
    for k in range(len(yn)):
        multi = 1
        for i in range(len(xn)):
            if i != k:
                multi *= (x - xn[i]) / (xn[k] - xn[i])
        sum += yn[k] * multi
    return sum


def main():
    begin = -5
    end = 5
    n = 10
    xn = [i / n for i in range(begin * n, end * n + 1)]
    yn = [f(i) for i in xn]
    ln = [lagrange(i, begin, end, n) for i in xn]
    ymax=max(1,max(ln),-min(ln))
    plt.plot(xn, yn, color='r', label='f(x)')
    plt.plot(xn, ln, color='b', label='Ln(x)')
    plt.legend()
    plt.axis([begin,end,-ymax*2,ymax*2])
    plt.show()


if __name__ == '__main__':
    main()
