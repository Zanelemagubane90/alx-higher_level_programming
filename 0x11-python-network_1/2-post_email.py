#!/usr/bin/python3
"""Write a Python script that takes in a URL and ..."""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    my_url = sys.argv[1]
    myvalue = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(myvalue).encode("ascii")

    the_request = urllib.request.Request(my_url, data)
    with urllib.request.urlopen(the_request) as results:
        print(results.read().decode("utf-8"))
