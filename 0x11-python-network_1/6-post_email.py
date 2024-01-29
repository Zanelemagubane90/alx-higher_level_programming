#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email address..."""
import sys
import requests


if __name__ == "__main__":
    myurl = sys.argv[1]
    myv = {"email": sys.argv[2]}

    results = requests.post(myurl, data=myv)
    print(results.text)
