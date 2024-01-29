#!/usr/bin/python3
"""Write a Python script that takes in a letters"""
import sys
import requests


if __name__ == "__main__":
    mylttr = "" if len(sys.argv) == 1 else sys.argv[1]
    dt_pyld = {"q": mylttr}

    results = requests.post("http://0.0.0.0:5000/search_user", data=dt_pyld)
    try:
        rspn = results.json()
        if rspn == {}:
            print("No result")
        else:
            print("[{}] {}".format(rspn.get("id"), rspn.get("name")))
    except ValueError:
        print("Not a valid JSON")
