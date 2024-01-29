#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.
"""
import sys
import requests


if __name__ == "__main__":
    my_url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    rspn = requests.get(my_url)
    my_commits = rspn.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                my_commits[i].get("sha"),
                my_commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
