from colorama import Fore, Style, init

def rot47_convert(s):
    x = []

    for i in range(len(s)):
        j = ord(s[i])

        if j >= 33 and j <= 126:
            x.append(chr(33 + ((j + 14) % 94)))

        else:
            x.append(s[i])

    return ''.join(x)

def rot47_menu():
    try:
        string = input(f"{Fore.RED}[Rot47] > ")

        if string == 'help':
            a = f"""{Fore.BLUE}
         [+] Usage [+]

    [Encrypt] > rot47encrypt 
    [Decrypt] > rot47decrypt      
    [Exit]    > exit
             """
            print(a)
            rot47_menu()

        elif string == "rot47encrypt":
            rot47encrypt = input(f"{Fore.BLUE}[+] String [+] > ")
            res = rot47_convert(rot47encrypt)
            print(f"{Fore.YELLOW}" + "{}".format(res))
            rot47_menu()

        elif string == "rot47decrypt":
            rot47decrypt = input(f"{Fore.BLUE}[+] String [+] > ")
            res = rot47_convert(rot47decrypt)
            print(f"{Fore.YELLOW}" + "{}".format(res))
            rot47_menu()

        elif string == "exit":
            print(f"{Fore.YELLOW}[+] Exit [+]")

        else:
            rot47_menu()

    except SyntaxError:
        print("Error")