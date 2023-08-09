# seive.py
# By: Sam Schmitz
# sieve of Eratosthes
# function that finds all the prime numbers less than or equal to n

def seive(n):
    primes = makeLst(n) #Create the list of potential primes
    #remove numbers from primes that are divisible by i and <= the square
    for i in primes:    #i=the current num and a prime
        for j in primes[i:]: #iterate through the numbers after i
            if (j >= (i**2)) and (j % i == 0):  #checks if j will be struck
                primes.remove(j)    #strike j
    return primes

def makeLst(n): #makes a list of the numbers 2-n
    lst = []
    for i in range(n-2):
        lst.append(i+2)
    return lst

def seives(n):
    a, l = [], []
    for p in range(n-2):    #Create the list of possible squares
        a.append(p+2)
    #print(a)
    for p in range(int(n**.5) - 2): #CHeck the numbers to see if they should be struck
        #print(a[p])
        if a[p] != 0:   #act only if the number has yet to be struck
            j = (p+2) ** 2
            while j <= (n-1):   #strike the numbers that are not square by turning them to 0
                #print(j, a[j-2])
                a[j-2] = 0
                j += (p + 2)
    #print(a)
    for p in range(n-2):    #copy the values that are unstruck into the list of primes. 
        if a[p] != 0:
            l.append(a[p])
    return l

def main():
    lst = seive(100)
    print (lst)
    l = seives(100)
    print (l)

main()
