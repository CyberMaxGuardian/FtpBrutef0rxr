# FtpBrutef0rxr

A Python script for FTP bruteforcing with asyncio.

## Introduction

This script is designed to perform FTP bruteforcing attacks using asyncio. It concurrently attempts to log in to an FTP server using a provided username and a wordlist of passwords.

## Disclaimer

This tool is intended for educational and ethical use only. Unauthorized access to computer systems is illegal and strictly prohibited. Use this script at your own risk, and ensure you have proper authorization before attempting any brute-force attacks.

## Features

- Asynchronous FTP bruteforcing for improved performance.
- Adjustable concurrency limit to control the number of simultaneous login attempts.
- Progress display during the brute force process.
- User-friendly command-line interface.

## Prerequisites

Before using this script, ensure you have the following installed:

- Python 3.7 or higher
- aioftp library (`pip install aioftp`)
- termcolor library (`pip install termcolor`)

## Installation

1. Clone the repository:
   
   ```bash
   git clone https://github.com/CyberMaxGuardian/FtpBrutef0rxr.git
   
3. Change Directory:
   
   ```bash
   cd FtpBrutef0rxr
   
5. Install Requirements
   
    ```bash
   pip install -r requirements.txt

## Example
![testcase](https://github.com/CyberMaxGuardian/FtpBrutef0rxr/assets/143591496/1cb918e5-7507-4ec3-8327-c13d06e9258f)

    
## Options
- target: Host to attack, e.g., 192.168.1.1.
- -w or --wordlist: Path to the wordlist file.
- -u or --username: Username with which to perform the bruteforce.
- -p or --port (optional): Port to attack on, default is 21.
- -c or --concurrency (optional): Concurrency limit, default is 10.

## Usage
   ```bash
   python FtpBrutef0rxr.py <target> -w <wordlist> -u <username> [-p <port>] [-c <concurrency>]

