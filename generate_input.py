import numpy

shape = 501


def target(x):
    noise = numpy.random.normal(size=shape) * 20
    return numpy.log(x) * 100 + 10 + noise


x = numpy.linspace(10, 300, shape)
y = target(x)
mat = numpy.stack([x, y], axis=1)
print(f"{mat.shape=}")
numpy.savetxt("times.txt", mat, fmt="%.7g", delimiter="\t")
