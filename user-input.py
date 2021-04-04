import requests
url = input("Please enter your URL (including http or https): ")

# Request the above URL
r = requests.get(url)

# To inspect the returned status code:
# print(r.status_code)

# To inspect the returned URL:
# print(r.url)

# Inspect the history
# print(r.history)

for i, response in enumerate(r.history, 1): 
	print(i,response.url,response.status_code)

print("Complete: ",r.url,r.status_code)

