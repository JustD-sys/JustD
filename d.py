import math

def f(x):
    return 1 + x * math.exp(-x)

def bisection(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Fungsi tidak berubah tanda di interval [a, b].")
        return None
    
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        print(f"Iterasi {i+1}: c = {c}, f(c) = {fc}")

        if abs(fc) < tol or (b - a) / 2 < tol:
            return c
        
        if f(a) * fc < 0:
            b = c
        else:
            a = c

    print("Metode tidak konvergen dalam iterasi maksimum.")
    return None

# Contoh penggunaan:
akar = bisection(-2, 1)
print("Akar ditemukan di:", akar)
