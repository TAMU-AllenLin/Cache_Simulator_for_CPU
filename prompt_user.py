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
    
    