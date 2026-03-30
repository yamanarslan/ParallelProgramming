import time
import tracemalloc

def performance(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        t1 = time.perf_counter()
        
        result = func(*args, **kwargs)
        
        t2 = time.perf_counter()
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        wrapper.counter += 1
        wrapper.total_time += (t2 - t1)
        wrapper.total_mem += peak
        
        return result
    
    wrapper.counter = 0
    wrapper.total_time = 0
    wrapper.total_mem = 0
    
    return wrapper
