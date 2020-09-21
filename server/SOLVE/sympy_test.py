from sympy import symbols,pi,Eq,latex,sympify

if __name__ == "__main__":
    x, y = symbols('x y',complex = True)

    expr = sympify("0.1*cos(pi*x+pi)")
    expr2 = y
    print(latex(expr))
