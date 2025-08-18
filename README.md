# Cache_Simulator_for_CPU

This project is a simple direct-mapped cache simulator written in Python. It allows users to configure cache size and block size, load memory access traces (either manually or from a file), and compute hit/miss statistics.

---

##Features 
- User-configurable **cache size** and **block size**  
- Supports **manual input** of memory accesses  
- Supports **file-based input** for larger traces  
- Reports:
  - Total memory accesses
  - Number of hits
  - Number of misses
  - Hit rate
  - Miss rate
 
## Project Structure 
```
cache_simulator_for_CPU/
├── direct_mapped_cache.py  # Main simulation runner
├── prompt_user.py          # Prompt user for inputs 
└── README.md               # Project documentation
```

---

## Requirements
- Python 3.x  
(No external libraries are required.)

---
