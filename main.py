import gif
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym


# from mpl_toolkits import mplot3d


@gif.frame
def plot_solid_of_revolution(f, a, b, angle, display=False):
    """
    Plot the solid of revolution of function f around y-axis.
    :param f: function to be revolutioned
    :param a: left bound of the revolution
    :param b: right bound of the revolution
    :param angle: angle of revolution
    :param display: if True, display the plot

    """

    # Preparing the figure and the axis for the plot of the solid of revolution and the function f
    fig = plt.figure(figsize=(12, 6))
    ax2 = fig.add_subplot(1, 2, 1, projection='3d')
    ax2.set_title('Solid of Revolution')
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')
    ax2.set_xlim(-10, 10)
    ax2.set_ylim(-10, 10)
    ax2.set_zlim(-10, 10)
    ax2.view_init(elev=20, azim=20)
    ax2.grid(True)

    ax1 = fig.add_subplot(1, 2, 2)
    ax1.set_title('Function of Revolution')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_xlim(-10, 10)
    ax1.set_ylim(-10, 10)
    ax1.set_aspect('equal')
    ax1.grid(True)
    ax1.set_axisbelow(True)
    ax1.set_facecolor('#f2f2f2')

    n = 40
    x = np.linspace(a, b, n)
    y = f(x)
    t = np.linspace(0, angle, n)

    xn = np.outer(y, np.cos(t))
    yn = np.outer(y, np.sin(t))
    zn = np.zeros_like(xn)

    for i in range(len(y)):
        zn[i:i + 1, :] = np.full_like(zn[0, :], y[i])

    # Plotting the solid of revolution and the function f
    ax2.plot_surface(xn, yn, zn, cmap=plt.cm.YlGnBu_r)
    ax1.plot(x, y)

    if display:
        plt.show()


def exact_volume_of_solid_revolution(f, a, b, axis):
    """
    Calculate the exact volume of a solid of revolution.
    :param f: function to be revolutioned symbolic representation with sympy
    :param a: left bound of the revolution
    :param b: right bound of the revolution
    :param axis: axis of revolution
        x,y or tuple of coefficient of line
                    if it's a tuple, it's first two elements are taken as slope and intercept of the line and the rest is ignored
    :return: volume of the solid revolution
 """
    x = sym.Symbol('x', real=True)
    if axis == 'x':
        return sym.N(np.pi * sym.integrate(f ** 2, (x, a, b)), 7)
    elif axis == 'y':
        return sym.N(2 * np.pi * sym.integrate(x * sym.Abs(f), (x, a, b)), 7)
    elif isinstance(axis, tuple):
        slope = axis[0]
        intercept = axis[1]
        line = slope * x + intercept
        print(sym.diff(f, x))
        return sym.N(np.pi / ((slope ** 2 + 1) * np.sqrt(slope ** 2 + 1)) * sym.integrate(((1 + slope * sym.diff(f, x)) * (f - line) ** 2), (x, a, b)), 7)
    else:
        return "Error: axis must be x or y or tuple of coefficient of line"


def approximate_volume_of_solid_revolution(f, a, b, axis, n):
    """
    Calculate the approximate volume of a solid of revolution with Simpson's rule.
    :param f: function to be revolutioned symbolic representation with sympy
    :param a: left bound of the revolution
    :param b: right bound of the revolution
    :param axis: axis of revolution
        x,y or tuple of coefficient of line,
            if it's a tuple, it's first two elements are taken as slope and intercept of the line and the rest is ignored
    :param n: number of divisions (must be even)
    :return: approximate volume of the solid revolution
 """
    if n % 2 == 1:
        return "Error: n must be even"
    x = sym.Symbol('x', real=True)
    h = (b - a) / n
    if axis == 'x':
        f = f ** 2
        scalar = np.pi * (h / 3.)
        odd_index = 4 * np.sum([f.subs(x, a + i * h) for i in range(1, n) if i % 2 == 1])
        even_index = 2 * np.sum([f.subs(x, a + i * h) for i in range(1, n - 1) if i % 2 == 0])
    elif axis == 'y':
        f = x * sym.Abs(f)
        scalar = 2 * np.pi * (h / 3.)
        odd_index = 4 * np.sum([f.subs(x, a + i * h) for i in range(1, n) if i % 2 == 1])
        even_index = 2 * np.sum([f.subs(x, a + i * h) for i in range(1, n - 1) if i % 2 == 0])
    elif isinstance(axis, tuple):
        slope = axis[0]
        intercept = axis[1]
        line = slope * x + intercept
        scalar = np.pi / ((slope ** 2 + 1) * np.sqrt(slope ** 2 + 1)) * (h / 3.)
        f = ((1 + slope * sym.diff(f, x)) * (f - line) ** 2)
        odd_index = 4 * np.sum([f.subs(x, a + i * h) for i in range(1, n) if i % 2 == 1])
        even_index = 2 * np.sum([f.subs(x, a + i * h) for i in range(1, n - 1) if i % 2 == 0])
    else:
        return "Error: axis must be x or y or tuple of coefficient of line"
    return sym.N(scalar * (f.subs(x, a) + f.subs(x, b) + odd_index + even_index), 5)


x = sym.Symbol('x', real=True)
print(exact_volume_of_solid_revolution(sym.Abs(x), -1, 1, (1, 4)))
# print(approximate_volume_of_solid_revolution(sym.sin(x) + x ** 2, 0, 1, (2, 2), 6))
# frames = []
# for i in np.linspace(0, 2 * np.pi, 10):
#     frame = plot_solid_of_revolution(lambda x: np.sin(x) + x ** 2, -3, 3, i)
#     frames.append(frame)
#
# gif.save(frames, 'images/vol3.gif', duration=500)
#
plot_solid_of_revolution(lambda x: x ** 3, -2, 2, 2 * np.pi, True)
