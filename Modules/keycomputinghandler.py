import random
import sys
from Crypto.Util.number import getPrime
from Crypto.Random import get_random_bytes
from colorama import Fore, Style, init

def keycomputing_menu():
    p = 997
    g = 3
    t = 5

    try:
        keycomputing = input(f"{Fore.RED}[KeyComputing] > ")

        if keycomputing == "keygen":
            primebits = int(input(f"{Fore.BLUE}[+] Bits [+] > "))

            msg = str(input(f"{Fore.BLUE}[+] String [+] > "))

            if (len(sys.argv) > 1):
                primebits = int(sys.argv[1])

            if primebits > 512: primebits = 512

            p = getPrime(primebits, randfunc=get_random_bytes)

            z = [0] * t
            X = [0] * t
            r = [0] * t
            K = [0] * t

            for i in range(0, t):
                r[i] = random.randint(0, p)
                z[i] = pow(g, r[i], p)

            for i in range(0, t):
                X[i] = pow(g, r[(i + 1) % t] * r[i] - r[i] * r[(i - 1) % t], p)

            for i in range(0, t):
                K[i] = pow(z[(i - 1) % t], (t) * r[i], p)

                for j in range(i + 1, i + 1 + t):
                    if (i == j):
                        continue

                    K[i] = (K[i] * pow(X[(j - 1) % t], (t - j), p)) % p

            res = r[0] * r[1] + r[1] * r[2] + r[2] * r[3] + r[3] * r[4] + r[4] * r[0]

            print(f"{Fore.YELLOW}[+] Computed key [+]\n", pow(g, res, p))
            keycomputing_menu()

        elif keycomputing == "help":
            a = f"""{Fore.BLUE}
        [+] Usage [+]
                
    [Generate Key] > keygen     
    [Exit]         > exit
            """
            print(a)
            keycomputing_menu()

        elif keycomputing == "exit":
            print(f"{Fore.YELLOW}[+] Exit [+]")

        else:
            keycomputing_menu()

    except ValueError():
        keycomputing_menu()

    except SyntaxError():
        keycomputing_menu()