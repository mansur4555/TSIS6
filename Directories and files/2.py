# import os Library 
import os 

# Check access with os.F_OK 
path1 = os.access("C:\PP", os.F_OK) 
print("Does the path exists:", path1) 

# Check access with os.R_OK 
path2 = os.access("C:\PP", os.R_OK) 
print("Access to read the file:", path2) 

# Check access with os.W_OK 
path3 = os.access("C:\PP", os.W_OK) 
print("Access to write to file:", path3) 

# Check access with os.X_OK 
path4 = os.access("C:\PP", os.X_OK) 
print("Can path be executed:", path4)