
def evaluate_internal(degree1,x1,constant_term1,*coefficients1):
    s=constant_term1
    k=1
    pwr=x1
    if (degree1!=len(coefficients1)):
        return "need ", degree1, " coefficient(s)"
    while (k<degree1+1):
        s+=coefficients1[k-1]*pwr**k
         k+=1
    return s
if __name__ == "__main__":
    wantto=y
    while (wantto=y):
        Degree=int(input("Degree of the polynomial: "))
        xvalue=int(input("Value of x: "))
        constantvalue=int(input("Value of constant: "))
        coefficients=[]
        for i in range(Degree):
            append.coefficients(int(input("Coefficient of the x^", i, "term: ")))
        evaluate_internal(Degree,xvalue,constantvalue,coefficients)
        wantto=input("Do you want to evaluate another polynomial(y/n)? ")


