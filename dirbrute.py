import requests
import random
import time
import sys

url = input('URL:' )
wordlist = input('Wordlist: ')



def write(word):
    f1 = open("write1.txt", "a")
    f1.write(word + "\n")


fo = open(wordlist, "r+")
for i in range(2000):
    word = fo.readline(10).strip()
    surl = url + word
    # print (surl)

    response = requests.get(surl)
    # print (response)
    if (response.status_code == 200):
        print("[+] found :- ", surl)
        write(word)
    else:
        print("[-] Not found :- ", surl)
        pass
