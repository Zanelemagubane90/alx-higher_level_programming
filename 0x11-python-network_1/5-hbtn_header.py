#!/usr/bin/python3
"""displays the value of the variable X-Request-Id in the response header"""
import sys
import requests


if __name__ == "__main__":
    my_url = sys.argv[1]

    results = requests.get(my_url)
    print(results.headers.get("X-Request-Id"))
