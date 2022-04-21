import os
import sys

n = (sys.argv)
args = n
if args == n:
    print("DonutPac takes no argument..!")
    os.system('exit')
else:
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
                    os.system('wget https://raw.githubusercontent.com/gauthamnair2005/DonutLinux/main/zlib_ci.sh')
                    os.system('bash zlib_ci.sh')
                    os.system('sudo rm -Rf zlib-1.2.12')
                    os.system('sudo rm zlib_ci.sh')
                    print("Zlib v1.2.12 .... Installed")
                    print()
                else:
                    print()
                    print("Zlib Not Installed")
                    print()
            elif "grub" in donut:
                print()
                print("Connecting to the Server...")
                print("Loading Repository Data....")
                print()
                print("The following package(s) are going to be installed: ")
                print("\t GRUB-1.99")
                confirm = input("Are you sure you want to install it? (y/n) : ")
                if confirm == "y" or confirm == "yes":
                    print("Downloading GRUB-1.99")
                    os.system('wget https://ftp.gnu.org/gnu/grub/grub-1.99.tar.xz')
                    print("Downloaded GRUB-1.99")
                    print()
                    print("Please wait... Preparing to Configure and Install GRUB...")
                    print("Downloading Configuration Script and Installing GRUB...")
                    os.system('wget https://raw.githubusercontent.com/gauthamnair2005/DonutLinux/main/grub_ci.sh')
                    os.system('bash grub_ci.sh')
                    os.system('sudo rm -Rf grub-1.99')
                    os.system('sudo rm grub_ci.sh')
                    print("GRUB v1.99 .... Installed")
                    print()
                else:
                    print()
                    print("GRUB Not Installed")
                    print()
            elif donut == "developer":
                PRINT()
                print("Gautham Nair")
                print()
                print("DonutPac for DonutOS/DonutLinux")
                print()
            else:
                print()
                print("Connecting to the Server...")
                print("Loading Repository Data....")
                print()
                print("The package ", donut , " couldn't be located in DonutPac's Index")
                print()