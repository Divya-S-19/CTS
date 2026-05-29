class Converter:
    def c_to_f(self, c):
        return (c * 9/5) + 32

    def f_to_c(self, f):
        return (f - 32) * 5/9

    def c_to_k(self, c):
        return c + 273.15


conv = Converter()

print("C to F:", conv.c_to_f(25))
print("F to C:", conv.f_to_c(77))
print("C to K:", conv.c_to_k(25))