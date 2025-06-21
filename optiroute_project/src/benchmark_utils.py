import time
import tracemalloc

def measure_time_and_memory(func, *args, **kwargs):
    tracemalloc.start()
    start_time = time.time()
    
    result = func(*args, **kwargs)
    
    end_time = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    elapsed_time = end_time - start_time
    peak_memory_kb = peak / 1024  # Convert to KB

    return result, elapsed_time, peak_memory_kb
