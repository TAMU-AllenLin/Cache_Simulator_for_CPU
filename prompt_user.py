def user_input():
    while True:
        try: 
            cache_size = int(input("Enter cache size (ex- 1024 = 1 KB): "))
            block_size = int(input("Enter block size in bytes: "))
            
            if cache_size <= 0 or block_size <= 0:
                print("Please enter a positive value")
                continue    
            
            if block_size > cache_size:
                print("Block size cannot be greater than cache size")
                continue 
            
            if cache_size % block_size != 0:
                print("Cache size must be a multiple of block size.")
                continue
            
            return cache_size, block_size 
            
        except ValueError:
            print("Please enter valid integer for sizes.")
    
def get_memory_acceses():
    mode = input("Enter mode ('manual' or 'file'): ").strip().lower()
    
    if mode == 'manual':
        addresses = input("Enter memory addresses (decima or hex) seperated by commas: ")
        
        return (int(addr, 0) for addr in addresses.split(',')) #int(addr,0) will handle hex and decimal
    
    elif mode == 'file':
        file_name = input("Enter file name (ex- trace.txt): " )
        accesses = []
        
        with open(file_name) as f:
            for line in f:
                parts = line.strip().split()
                if parts:
                    addr_str = parts[-1] #last part is the address 
                    accesses.append(int(addr_str, 0))
        return accesses
    
    else:
        print("Invalid Input. Try again.")
        return get_memory_acceses()
