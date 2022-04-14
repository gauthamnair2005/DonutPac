import os
import sys

os.system('clear')
print()
print("DonutPac - Package Manager for DonutOS")
print("-------------------------------------------")
print()
print("To install a package just type the package name in the prompt..")
print()
donut = ""
while donut != "exit" or donut != "quit":
    donut = input("DonutPac > ").lower()
    if donut == "exit" or donut == "quit":
        break
    else:
        if "zlib" in donut:
            print()
            print("Connecting to the Server...")
            print("Loading Repository Data....")
            print()
            print("The following package(s) are going to be installed: ")
            print("\t Zlib-1.2.12")
            confirm = input("Are you sure you want to install it? (y/n) : ")
            if confirm == "y" or confirm == "yes":
                print("Downloading Zlib-1.2.12")
                os.system('wget http://zlib.net/zlib-1.2.12.tar.gz')
                print("Downloaded Zlib-1.2.12")
                print()
                print("Please wait... Preparing to Configure and Install Zlib..")
                print("Downloading Configuration Script and Installing Zlib...")
                os.system('wget https://github.com/gauthamnair2005/DonutLinux/blob/main/zlib_ci.sh')
                os.system('bash zlib_ci.sh')
                print("Zlib v1.2.12 .... Installed")
                print()
            else:
                print("Package not in Repository")