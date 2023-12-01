import requests

print("DonutPac Updater ")
print("-"*20)
print()
print("Obtaining the Latest Version of DonutPAC")

try:
    response = requests.get('https://raw.githubusercontent.com/gauthamnair2005/DonutPac/main/donutpac.py')
    response.raise_for_status()  # Raise an exception if the request was unsuccessful
    with open('donutpac.py', 'w') as file:
        file.write(response.text)
    print("DonutPac Updated successfully...")
except requests.RequestException as e:
    print(f"An error occurred: {e}")