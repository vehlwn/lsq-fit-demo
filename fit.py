import numpy
import scipy.optimize
import matplotlib.pyplot as plt


data = numpy.loadtxt("times.txt")
data_x = data[:, 0]
data_y = data[:, 1]


x0 = numpy.random.normal(size=2)
method = "lm"
verbose = 2


def target(x, params):
    (a, b) = params
    return a * numpy.log(x) + b


def residual(params):
    return target(data_x, params) - data_y


def plot_curve(res):
    tmp_x = numpy.linspace(data_x[0], data_x[-1], 100)
    plt.plot(data_x, data_y, ".", markersize=2, label="Time data", zorder=1)
    plt.plot(tmp_x, target(tmp_x, res.x), label="Least squares curve", zorder=2)
    plt.xlabel("Bytes")
    plt.ylabel("Seconds")
    plt.legend()
    plt.grid(True, linestyle=":")
    plt.savefig("out.png", dpi=300)


res = scipy.optimize.least_squares(residual, x0=x0, method=method, verbose=verbose)
print("Found params:", res.x)
plot_curve(res)
