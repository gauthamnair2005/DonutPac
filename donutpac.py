import os
import argparse
from tqdm import tqdm
import time
import requests
import json
import subprocess

def download_packages():
    url = "https://raw.githubusercontent.com/gauthamnair2005/DonutPac/main/packages.json"
    response = requests.get(url)
    return response.json()

def is_connected():
    try:
        print(f"Connecting to the Server...")
        requests.get('http://sites.google.com/view/donutlinux', timeout=5)
        return True
    except requests.exceptions.RequestException:
        return False


def install_package(package, packages):
    if package in packages:
        if is_connected():
            print("Loading Repository Data....")
            print(f"The following package(s) are going to be installed: ")
            print(f"\t {package}-{packages[package]['version']}")
            confirm = input("Are you sure you want to install it? (y/n) : ")
            if confirm.lower() in ["y", "yes"]:
                print(f"Downloading {package}-{packages[package]['version']}")
                try:
                    response = requests.get(packages[package]['link'], stream=True)
                    total_size = int(response.headers.get('content-length', 0))
                    block_size = 1024  # 1 Kibibyte
                    progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
                    with open(f'{package}.tar.gz', 'wb') as file:
                        for data in response.iter_content(block_size):
                            progress_bar.update(len(data))
                            file.write(data)
                    progress_bar.close()
                    if total_size != 0 and progress_bar.n != total_size:
                        print("ERROR, something went wrong")
                    print(f"Downloaded {package}-{packages[package]['version']}")

                    print(f"Extracting {package}.tar.gz")
                    subprocess.run(['tar', '-xf', f'{package}.tar.gz'])

                    print(f"Configuring {package}")
                    subprocess.run(['./configure'], cwd=package, check=True)

                    print(f"Making {package}")
                    subprocess.run(['make', '-j4'], cwd=package, check=True)

                    print(f"Installing {package}")
                    subprocess.run(['make', 'install'], cwd=package, check=True)

                    print(f"Cleaning up")
                    subprocess.run(['rm', '-rf', package])
                    subprocess.run(['rm', f'{package}.tar.gz'])

                except Exception as e:
                    print(f"An error occurred while installing {package}: {e}")
        else:
            print("No internet connection. Please check your network settings.")
    else:
        print(f"Package {package} not found.")

def main():
    parser = argparse.ArgumentParser(description='DonutPac - Package Manager for DonutOS')
    parser.add_argument('command', help='Command to execute (install)')
    parser.add_argument('package', help='Package to install')

    args = parser.parse_args()

    if args.command.lower() == "install":
        packages = download_packages()
        install_package(args.package.lower(), packages)
    else:
        print(f"Invalid command: {args.command}")

if __name__ == "__main__":
    main()