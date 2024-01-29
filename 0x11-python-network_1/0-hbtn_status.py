#!/usr/bin/python3
"""A python script that fetches data"""
import urllib.request


if __name__ == "__main__":
    the_request = urllib.request.Request("https://intranet.hbtn.io/status")
    with urllib.request.urlopen(the_request) as results:
        body_data = results.read()
        print("Body response:")
        print("\t- type: {}".format(type(body_data)))
        print("\t- content: {}".format(body_data))
        print("\t- utf8 content: {}".format(body_data.decode("utf-8")))
