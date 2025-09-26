def evaluate_polynomial(degree, x, constant_term, *coefficients):
    s=constant_term
    k=1
    pwr=x
    if (degree!=len(coefficients)):
        return "Should have raised ValueError"
    while (k<degree+1):
        s+=coefficients[k-1]*pwr**k
        k+=1
    return s
