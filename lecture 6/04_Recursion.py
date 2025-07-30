def rec(n):
    if n==0:
        return
    print(n)
    rec(n-1)            #here what we did was after printing n , our fn called itself again , and above we gave it a conditional statements where it stopped until it reached 0
                        #QUICK FACT , NORMAL RECURSION LIMIT IS 996
rec(10)

#wap to print factorial of any number using recursion

def fact(n):
    if n==1 or n==0:
        return 1
    return fact(n-1)*n
print(fact(5))
