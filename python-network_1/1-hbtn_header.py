#!/usr/bin/python3
"""
Bu modul verilmis URL-e sorgu gonderir ve
cavab basligindaki X-Request-Id deyerini gosterir.
"""
import urllib.request
import sys


if __name__ == "__main__":
    # Skript yalniz birbasa ise salindiqda bura icra olunur
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
