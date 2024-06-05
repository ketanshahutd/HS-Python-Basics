a = int(input("enter a number :"))
def find_product(a):  
    prod = 1
    while(a>0):
        prod = prod*(a%10)
        a = a//10
    return prod
result = find_product(a)
print("the product is :",result)    
