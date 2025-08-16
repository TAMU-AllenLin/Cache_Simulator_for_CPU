from prompt_user import user_input

class Cacheline: 
    def __init__(self):
        self.valid = False
        self.tag = None
        
        
class DirectMappedCache: 
    def __init__ (self, cache_size_bytes, block_size_bytes):
        self.block_size = block_size_bytes
        self.numlines = cache_size_bytes // block_size_bytes #tells how many "chunks" the cache can hold 
        self.cache = [Cacheline() for _ in range(self.numlines)] #generate the cache 
        
        self.hits = 0 #counter for number of hits 
        self.misses = 0 #counter for number of misses 
        
        print(f"Cache intializied with {self.numlines} blocks.")
        
    def access(self, address):
        '''access assigns the index of the cache by finding the block address (memory address // block size) and tag and then checking 
        to see if that line hits or misses and increments accordingly. If it is a hit (aka line is valid and the tag matches) then hit +1,
        if it is a miss (aka its not valid or tag doesnt match) then misses +1 then set valid to true and line tag to the tag. 
        '''
        block_address = address // self.block_size #calculates the block address 
        
        index = block_address % self.numlines #calculates the index = block_address % num_lines
        
        tag = block_address // self.numlines 
        
        line = self.cache[index] 
        
        if line.valid and line.tag == tag:
            print(f"Address {address}: Hit at index {index}")
            self.hits += 1 
            return True #cache was hit 
        else:
            print(f"Address {address}: Miss at index {index}")
            self.misses += 1 
            line.valid = True 
            line.tag = tag 
            return False 
    
     
    
    def stats(self):
        '''stats does some basic calculations to determine statistics like total number of accesses, hit rate, and miss rate'''
        total_accesses = self.hits + self.misses 
        hit_rate = self.hits / total_accesses if total_accesses > 0  else 0
        miss_rate = self.misses / total_accesses if total_accesses > 0 else 0 
        return{
            "Total accesses: ": total_accesses,
            "Number of hits: ": self.hits,
            "Number of misses: ": self.misses,
            "Hit rate: ": hit_rate,
            "Miss rate: ": miss_rate 
        }
    
if __name__ == "__main__": 
    cache_size, block_size = user_input()
    cache = DirectMappedCache(cache_size, block_size)
    
    while True: 
        user_address = input("Enter memory address to access ('q' to quit): ")
        
        if user_address.lower() == 'q':
            print("User quit.")
            break 
        try: 
            memory_address = int(user_address)
            cache.access(memory_address)
            cache.stats()
        except ValueError:
            print("Invalid Input. Enter a number.")