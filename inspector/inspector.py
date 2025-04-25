import inspect
import time
import sys
import torch 

# Store the first call time
t0 = None 

def gadget():
    global t0
    current_time = time.time() 
    if t0 is None: t0 = current_time 
    elapsed = current_time - t0 
    t0 = time.time()
    
    caller_frame = inspect.currentframe().f_back
    frame_info = inspect.getframeinfo(caller_frame)
    
    line_number = frame_info.lineno
    
    with open(frame_info.filename, 'r') as f:
        lines = f.readlines()
        line_content = lines[line_number - 2].rstrip()
    
    green_color = "\033[32m"
    reset_color = "\033[0m"
    output = f"{green_color}[line={line_number}] {elapsed:.6f}s {line_content}{reset_color}"
    print(output)
