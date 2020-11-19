from sympy import *
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h ,k,l = symbols('f g h k l', cls=Function)

f=2*x**5-x**3-3*x**2-6*x+4
g=x**4+x**3-x**2-2*x-2
q, r = div(f, g, domain='QQ')
print("Expand f in term of g")
print(q)
print(r)
h=r
q,r=div(g,h,domain='QQ')
print("expanding degree four polynomial")
print(q)
print(r)
k=r
q,r=div(h,k,domain='QQ')
print("Expanding degree three polynomial")
print(q)
print(r)
l=r
q,r=div(k,l,domain='QQ')
print("Expanding degree two polynomial")
print(q)
print(r)
print("GCD of  given  f and g polynomial is :")
result = gcd(f,g)
print(result)
