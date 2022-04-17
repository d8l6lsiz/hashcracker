import hashlib
import colorama
from colorama import Fore, Back, Style

colorama.init()


print(Fore.BLUE,"[1] MD5")
print(Fore.BLUE,"[2] SHA256")

sec = input("Choose: ")
if sec == "1":

    def tryOpen(wordlist):
        global pass_file
        try:
            pass_file = open(wordlist, "r")
        except:
            print(Fore.RED, "file location is wrong")
            quit()


    crackhash = input("Hash: ")
    wordlist = input("Wordlist: ")
    tryOpen(wordlist)
    for word in pass_file:
        print(Fore.CYAN, "[+] Trying: " + word.strip("\n"))
        enc_word = word.encode("utf-8")
        md5Digest = hashlib.md5(enc_word.strip()).hexdigest()
        if md5Digest == crackhash:
            print(Fore.GREEN, f"Hash cracked: {word} ")
            exit()
    print(Fore.YELLOW, "password not found on file")

if sec == "2":

    def tryOpen(wordlist):
        global pass_file
        try:
            pass_file = open(wordlist, "r")
        except:
            print(Fore.RED, "file location is wrong")
            quit()


    crackhash = input("Hash: ")
    wordlist = input("Wordlist: ")
    tryOpen(wordlist)
    for word in pass_file:
        print(Fore.CYAN, "[+] Trying: " + word.strip("\n"))
        enc_word = word.encode("utf-8")
        sha256Digest = hashlib.sha256(enc_word.strip()).hexdigest()
        if sha256Digest == crackhash:
            print(Fore.GREEN, f"Hash cracked: {word} ")
            exit()
    print(Fore.YELLOW, "password not found on file")

