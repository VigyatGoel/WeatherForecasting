import requests
import os
import json


def mac():
    while True:
        try:
            city = input("Enter the name of the city or press q to quit : ")
            if city == "q":
                print("Thanks for using this application.")
                os.system("say 'Thanks for using this application'")
                break

            url = ""

            r = requests.get(url)

            wdic = json.loads(r.text)
            w = wdic["current"]["temp_c"]

            print(f"currently it is {w} degree celcius in {city}.")

            os.system(f"say 'currently it is {w} degree celcius in {city}'")
        except:
            print("City not found.")
            print("Please retry.")

def win():
    while True:
        try:
            city = input("Enter the name of the city or press q to quit : ")
            if city == "q":
                print("Thanks for using this application.")
                break

            url = f"https://api.weatherapi.com/v1/current.json?key=bb77e16095744709bba171327230807&q={city}"

            r = requests.get(url)

            wdic = json.loads(r.text)
            w = wdic["current"]["temp_c"]

            print(f"currently it is {w} degree celcius in {city}.")
        except:
            print("City not found.")
            print("Please retry.")

print("Welcome to Weather Forecasting app created by Vigyat Goel.")
print("Please select which Operating system you are currently using.")
while True:
    print("Please select 'W' for Windows or 'M' for Mac.")
    print("Select 'Q' to exit")
    x = input("Enter your choice -> ")
    x = x.upper()
    if x == "W":
        win()

    elif x == "M":
        mac()

    elif x == "Q":
        break

    else:
        print("Invalid choice")
