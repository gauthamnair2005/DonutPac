import os

print("DonutPac Updater ")
print("-"*20)
print()
print("Obtaining the Latest Version of DonutPAC")
try:
  os.system('wget https://raw.githubusercontent.com/gauthamnair2005/DonutPac/main/donutpac.py -O donutpac.py')
  print("DonutPac Updated successfully...")
except:
  print("An error ocurred")
