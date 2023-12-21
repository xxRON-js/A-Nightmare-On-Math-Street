## A Nightmare On Math Street - HTB Challenge

## Description
This repository contains Python scripts designed for solving math questions received from a remote server. The scripts utilize the [Pwntools](https://docs.pwntools.com/) library for interaction with the server.

## Scripts

### pymare.py

The original script that interacts with a remote server, solves math questions, and prints the flag.

### pymare_v2.py

An improved version of the original script that prints less output, focusing only on the final flag.

### pymare_v3.py

Enhanced version that not only prints less but also asks for the IP address and port interactively instead of being hardcoded.

### pymare_v4.py

Further refinement of the script that includes the improvements from v3 and additionally prompts the user for the server's IP address and port number.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/pymare-scripts.git
    cd pymare-scripts
    ```

2. Run the desired script:

    ```bash
    python3 pymare.py
    ```

    or

    ```bash
    python3 pymare_v4.py
    ```

3. Follow the on-screen instructions for providing the server's IP address and port number.

4. The script will interact with the server, solve math questions, and print the flag.

## Disclaimer

These scripts are provided for educational purposes only. Use them responsibly and only on systems for which you have explicit permission.

