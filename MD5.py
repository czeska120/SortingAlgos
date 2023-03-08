import hashlib
import time
import random

# CCDSALG MCO2
# @author ANG, Elliamae
# @author MOJICA, John Marvic
# @author PALLASIGUE, Diego
# @author SILVESTRE, Franczeska

# Python program to calculate MD5 hash value 

# Define class to represent 
class Obj:
    def __init__(self,str):
        self.key = str
        self.counter = 1
        self.next = None
    def increment(self):
        self.counter += 1 

# Get input
print("[MD5 - Hash Table] \n")
n = int(input("Enter string length (n): "))
k = int(input("Enter k value: "))

# Generate string with length n
str = "acgt"
seq = "".join((random.choice(str) for _ in range(n)))
collisions = 0

# Hash Table
htbl_kmer = [None for i in range(n)]

# Measure execution time
timeStart = time.time()

for i in range(n-k+1):
    substr = seq[i:i+k]

    # Call Hash function
    index = int(hashlib.md5(substr.encode()).hexdigest(), 16) % n

    # If there is already an element present in slot
    if(htbl_kmer[index] is not None):
        kmer = htbl_kmer[index]

        # If matching content
        if(kmer.key == substr):
            kmer.increment()
            continue
        while(kmer.next is not None):
            if(kmer.key == substr):
                kmer.increment()
                break
            else:
                kmer = kmer.next
                if(kmer.key == substr):
                    kmer.increment()
        
        # Insert in next slot if empty and does not match with current element
        if(kmer.next is None and kmer.key != substr):
            kmer.next = Obj(substr)
            collisions += 1
    else:
        htbl_kmer[index] = Obj(substr)

# Measure execution time
timeEnd = time.time()

# TESTING: Print resulting hash table (Comment out when testing large n)
# print("Original string: ", seq)
# print("Hash table | Occurences ")
# for i in range(n):
#    if(htbl_kmer[i] is not None):
#        print(htbl_kmer[i].key + " | ", htbl_kmer[i].counter)

# Print collisions and execution time
print("Collisions occurred: ", collisions)
print("Total execution time (in seconds): ", timeEnd - timeStart)
