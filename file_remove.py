#create a code to create 100 folder in folder name data 
import os 

for i in range(0,100):
	os.remove(f"Data/datas{i+1}.py")

print("folder creadted sucessfully")