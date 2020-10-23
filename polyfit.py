# -*- encoding: utf-8 -*-
import numpy as np


def p_function(p, x):
    return [p(i) for i in x]


def vector_inner_product(f1, f2, x, function=True):
    sum = 0
    if function:
        for i in range(len(x)):
            sum += f1(x[i]) * f2(x[i])
    else:
        for i in range(len(x)):
            sum += f1[i] * f2(x[i])
    return sum


def main():
    x = [0, .5, .6, .7, .8, .9, 1.]
    y = [1., 1.75, 1.96, 2.19, 2.44, 2.71, 3.]
    # omega = [1., 1., 1., 1., 1., 1., 1.]
    a, p, alpha, beta = [], [], [], []
    inner_product = []
    p.append(np.poly1d([1]))
    for n in range(3):
        inner_product.append(vector_inner_product(p[n], p[n], x))
        f_inner = vector_inner_product(y, p[n], x, function=False)
        px = p[n] * [1, 0]
        xp = vector_inner_product(px, p[n], x)
        a.append(f_inner / inner_product[n])
        alpha.append(xp / inner_product[n])
        if n > 0:
            beta.append(
                vector_inner_product(p[n], p[n], x) / vector_inner_product(
                    p[n - 1], p[n - 1], x))
            p.append(np.poly1d([1, -alpha[n]]) * p[n] - beta[n - 1] * p[n - 1])
        else:
            p.append(np.poly1d([1, -alpha[n - 1]]))
    s = np.poly1d([0])
    for n in range(3):
        s += a[n] * p[n]
    print(s)


if __name__ == '__main__':
    main()
