from colorama import Fore, Style, init
import os
import socket
import Modules.rot47handler
import Modules.zlibhandler
import Modules.bytexorhandler
import Modules.text2hexhandler
import Modules.keycomputinghandler

def clear():
    cls = lambda: os.system('cls')
    cls()

def logo():
    logo = f"""{Fore.RED}
 ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗ ███████╗████████╗███████╗██╗███╗   ██╗███████╗
██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝╚══██╔══╝██╔════╝██║████╗  ██║██╔════╝
██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║███████╗   ██║   █████╗  ██║██╔██╗ ██║███████╗
██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║╚════██║   ██║   ██╔══╝  ██║██║╚██╗██║╚════██║
╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝███████║   ██║   ███████╗██║██║ ╚████║███████║
 ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝                                                                                                                                                                                                                                                       

            [+] By hypostat1c for SteinsGroup [+]
        [+] To see manual of commands do "help" [+]   
"""
    print(logo)
logo()

def handler():
    menu_handler = True
    hostname = socket.gethostname()
    while menu_handler:
        menu_handler = input(f"{Fore.RED}Steins@" + f"{hostname} > ")

        if menu_handler == "1":
            Modules.rot47handler.rot47_menu()

        elif menu_handler == "2":
            Modules.zlibhandler.zlib_menu()

        elif menu_handler == "3":
            Modules.bytexorhandler.bytexor_menu()

        elif menu_handler == "4":
            Modules.text2hexhandler.text2hex_menu()

        elif menu_handler == "5":
            Modules.keycomputinghandler.keycomputing_menu()

        elif menu_handler == "help":
            a = f"""{Fore.BLUE}
         [+] Usage [+]

        [Rot47]        > 1 
        [Zlib]         > 2      
        [ByteXor]      > 3
        [Text2Hex]     > 4
        [KeyComputing] > 5
        [Exit]    > exit
             """
            print(a)

        elif menu_handler == "clear":
            clear()

        elif menu_handler == "exit":
            print(f"{Fore.YELLOW}[+] Exit [+]")
            exit()

        elif menu_handler != "":
            handler()

        else:
            handler()
handler()
