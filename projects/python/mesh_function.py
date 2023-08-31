import numpy as np

# f is a function,
def mesh_function(f, t):
    return [f(x) for x in t ]

def func(t):
    if t >= 0 and t <= 3:
        return np.exp(-t)
    else:
        if t > 3 and t<= 4:
            return np.exp(-3*t)
        else:
            raise ValueError("The function is defined on domain: <0,4>")

def test_mesh_function():
    t = np.array([1, 2, 3, 4])
    f = np.array([np.exp(-1), np.exp(-2), np.exp(-3), np.exp(-12)])
    fun = mesh_function(func, t)
    assert np.allclose(fun, f)

if __name__ == '__main__':
    test_mesh_function()