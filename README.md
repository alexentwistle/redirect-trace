# Redirect Checker

This Redirect Checker uses the Python Requests library to analyse redirect chains on a given URL.

## How it works

1. Run user-input.py
2. Enter your URL (remembering to specify http or https)
3. The script will list out each step in the redirect chain, alongside a response code for each step. 



### Usage notes
To inspect the returned status code:
- print(r.status_code)

To inspect the returned URL:
- print(r.url)

To inspect the redirect history:
- print(r.history)



### Example - Analysing redirect chain for http://wikipedia.org:
Run `user-input.py`  
Prompt: `Please enter your URL (including http or https):`  
Input: `http://wikipedia.org`  


Output:  
`1 http://wikipedia.org/ 301`  
`2 https://wikipedia.org/ 301`  
`Complete:  https://www.wikipedia.org/ 200`


Conclusion:
There were two 'hops' in this redirect chain. Both redirects were 301s (permanent redirects).