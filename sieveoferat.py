# find all prime numbers up to a given limit
# check divisibility of each prime
# can only be divided by the number 1 and itself
# create a list of consecutive numbers
# let p equal 2 the smallest prime number
# get the multiple of p by counting to n
# find first number greater than p
# grab all evens above 2 up to n and remove them
# grab
def find_primes(maxnum):
    first_prime = 2
    checklist = []
    # push to the checklist a list of numbers from 2 to the maxnum
    for i in range(maxnum):
        if i + 1 >= 2:
            checklist.append(i + 1)
    # iterate through the checklist and remove all evens above 2
    for i in checklist:
        if i%2 == 0 and i != first_prime:
            checklist.remove(i)
    # starting at num 3 remove every third index
    thirds = []
    for i in range(1, len(checklist), 3):
        if checklist[i] != 3:
            thirds.append(i)
    for num in checklist:
        if thirds[i] == checklist[i]:
            checklist.remove(num)
    print(thirds)
    print(checklist)
            
find_primes(30)