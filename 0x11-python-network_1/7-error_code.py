#!/usr/bin/python3
"""Write a Python script that takes in a URL, .."""
import sys
import requests


if __name__ == "__main__":
    myurl = sys.argv[1]

    results = requests.get(myurl)
    if results.status_code >= 400:
        print("Error code: {}".format(results.status_code))
    else:
        print(results.text)
