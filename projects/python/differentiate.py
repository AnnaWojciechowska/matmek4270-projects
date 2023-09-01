import numpy as np


#dt - delta t or "mesh spacing"
def differentiate(u, dt):
    result = np.empty(u.size)
    # border elements
    result[0] = (u[1] - u[0]) / dt
    last_index = u.size -1
    result[last_index] = (u[last_index] - u[last_index - 1]) / dt

    for i in range(1,last_index):
        result[i] = (u[i + 1] - u[i - 1])/(2*dt)
    return result

#d[1:-1] = (u[2:] - u[0:-2])/(2*dt)
# or
#d[1:N_t] = (u[2:N_t+1] - u[0:N_t-1])/(2*dt)

def differentiate_vector(u, dt):
    result = np.empty(u.size)
    result[0] = (u[1] - u[0]) / dt
    last_index = u.size -1
    result[last_index] = (u[last_index] - u[last_index - 1]) / dt
    result[1:-1] = (u[2:] - u[:-2])/(2*dt)
    return result

def test_differentiate():
    t = np.linspace(0, 1, 10)
    dt = t[1] - t[0]
    u = t**2
    du1 = differentiate(u, dt)
    du2 = differentiate_vector(u, dt)
    assert np.allclose(du1, du2)

if __name__ == '__main__':
    test_differentiate()
