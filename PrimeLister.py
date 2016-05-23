print("Here is a list of all the prime numbers from 2-100,000!!! It'll take a while to rpint out ALL of them so bear")
# I will now start the main thing!
# Takes myNum, an integer
# Returns True if n is prime
# Returns False if n is composite
def isPrime(y, list):
        x = range(1,int(y))
        num = y - 2
        o = 0
        for number in x:
                rder = int(y) % int(number)
# I have created a for loop to check all the numbers if they are prime
                if rder != 0:   
                        o = o + 1
# If the remainder is not 0 then it will continue
                        if o == num:
                                print(y)
                                list.append(y)
 
#Creating a empty list
primeList = []
# Opening the prime list text document 
myPrimes = open("primes.txt", "w")
# Starting a range from 2 top 10001 
rangeList = range(2, 10001)
# going through the list to find the primes
for n in rangeList:
        g = isPrime(n, primeList)
 
for x in primeList:
        myPrimes.write(str(x) + "\n")
#closing the list now we done   
myPrimes.close()
 
 
