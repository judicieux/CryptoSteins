from colorama import Fore, Style, init

def text2hex():
    text = input(f"{Fore.RED}[Text2Hex] > ")
    try:
        if text == "help":
            a = f"""{Fore.BLUE}
        [+] Usage [+]

    [Encrypt] > textencrypt 
    [Decrypt] > hexdecrypt      
    [Exit]    > exit
            """
            print(a)

        if text == "textencrypt":
            textencrypt = input(f"{Fore.BLUE}[+] String [+] > ")
            textencryptoutput = textencrypt.encode().hex()
            print(f"{Fore.YELLOW}" + textencryptoutput)
            text2hex()

        if text == "hexdecrypt":
            hexdecrypt = input(f"{Fore.BLUE}[+] Hex String [+] > ")
            hexdecryptoutput = bytearray.fromhex(hexdecrypt).decode()
            print(f"{Fore.YELLOW}" + hexdecryptoutput)

        if text == "exit":
            print(f"{Fore.YELLOW}[+] Exit [+]")

        else:
            text2hex()

    except ValueError:
        text2hex()

    except SyntaxError:
        text2hex()
