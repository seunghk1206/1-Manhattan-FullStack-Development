from numba import jit, cuda
a = 10**10
b = 10
print(cuda.gpus)
@jit(target = 'cuda')
def googolplex(a):
    return 10**10**a
googolplex(100)