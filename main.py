import numpy as np
from bitmap import BitMap
from primesieve import n_primes
from random import randint
# define hash_familiy classs and its methods inside my_solution method
def my_solution_t1(capacity):                                           
  class HashFamily:
    def __init__(self, capacity):                                     
      #capacity = n
      #buckets = p >= n
      # a = [1, p-1]
      # b = [0, p-1]
      # is hash function if: 
      self._capacity = capacity
      self._buckets = self.get_next_prime(capacity)                                           
      self._a = randint(1,self._buckets-1)                                     
      self._b = randint(0,self._buckets-1)                                              
      self._table = BitMap(self._buckets)                                   
      self._n =  0                                                          

    def get_next_prime(self, capacity):
        p = capacity + 1
        isPrime = False
        while not isPrime:
            p += 1
            sqrtp = int(np.sqrt(p))
            for i in range(2, sqrtp + 1):
                if p % i == 0:
                    isPrime = False
                    break
            else:
                isPrime = True
        return p    

    def get_hash(self, key):                                                   
      position = ((self._a*key + self._b)%self._buckets)%self._capacity
      self._n += 1
      return position

    def get_function(self):                                                 
      return self._a,self._b,self._buckets, capacity

    def set_item(self,pos):                                                 
      position = self._table.set(pos)                  
      return position                                                       

    def get_item(self,position):
      boolean = self._table.test(position)
      if boolean == 0: return False
      else: return True
      return boolean                                                        

    def load_factor(self):
       return (self._n / self._buckets)

  return HashFamily(capacity)

# Compute numbers of buckets and build hash_table
capacity = input('Please enter the range of values into the universe: ')
try:
   val = int(capacity)
except ValueError:
    print("No.. input string is not an Integer. It's a string")
    sys.exit("program is aborted....")

member = my_solution_t1(val)

print(member._table)
for i in range(0,int(capacity)):
    value = np.random.randint(1, val)
    # next = i
    pos= member.get_hash(value)
    print( "value",value,"hash",pos)
    pos=member.set_item(pos)
print(member._table)
