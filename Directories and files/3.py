import os 

path = "C:\PP" 
print("Does the path exists:", os.path.exists(path)) 

print(os.path.basename(path))
print(os.path.dirname(path))