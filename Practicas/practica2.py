import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no: "Complex") -> "Complex":
        result_real = self.real + no.real
        result_imaginary = self.imaginary + no.imaginary
        return Complex(result_real, result_imaginary)

    def __sub__(self, no: "Complex") -> "Complex":
        result_real = self.real - no.real
        result_imaginary = self.imaginary - no.imaginary
        return Complex(result_real, result_imaginary)

    def __mul__(self, no: "Complex") -> "Complex":
        #a y c son reales
        #b y d son imaginarios
        result_real = self.real * no.real - self.imaginary * no.imaginary
        result_imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(result_real, result_imaginary)

    def __truediv__(self, no: "Complex") -> "Complex":
        #a y c son reales
        #b y d son imaginarios
        result_real_numerador = self.real * no.real + self.imaginary * no.imaginary
        result_real_denominador = no.real ** 2 + no.imaginary **2
        result_imaginary_numerador = self.imaginary * no.real - self.real * no.imaginary
        result_imaginary_denominador = no.real ** 2 + no.imaginary **2
        result_real = result_real_numerador / result_real_denominador
        result_imaginary = result_imaginary_numerador / result_imaginary_denominador
        return Complex(result_real, result_imaginary)
    
    def mod(self):
        result_raiz1 = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return Complex(result_raiz1, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')