import ctypes
import os

# Get full path of DLL
dll_path = os.path.abspath("legacy.dll")

print("DLL Path:", dll_path)

# Load DLL
lib = ctypes.CDLL(dll_path)

# Tell Python about the C function
lib.process.argtypes = [
    ctypes.POINTER(ctypes.c_int),
    ctypes.POINTER(ctypes.c_int),
    ctypes.c_int
]

lib.process.restype = None

# Array size
size = 5

# Input array
input_data = (ctypes.c_int * size)(1, 2, 3, 4, 5)

# Empty output array
output_data = (ctypes.c_int * size)()

# Call C function
lib.process(
    input_data,
    output_data,
    size
)

print("Input :", list(input_data))
print("Output:", list(output_data))