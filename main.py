from colorama import Fore, Style, init
import os
import socket
import Include.rot47handler
import Include.zlibhandler

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def logo():
    logo = f"""{Fore.RED}
 ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗ ███████╗████████╗███████╗██╗███╗   ██╗███████╗
██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝╚══██╔══╝██╔════╝██║████╗  ██║██╔════╝
██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║███████╗   ██║   █████╗  ██║██╔██╗ ██║███████╗
██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║╚════██║   ██║   ██╔══╝  ██║██║╚██╗██║╚════██║
╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝███████║   ██║   ███████╗██║██║ ╚████║███████║
 ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝╚═╝  ╚═══╝╚══════╝                                                                                                                                                                                                                                                       

            [+] By goosebumps 4 Steins [+]
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
            Include.rot47handler.rot47_menu()

        elif menu_handler == "2":
            Include.zlibhandler.zlib_menu()

        elif menu_handler == "3":
            print("\n Student Record Found")

        elif menu_handler == 'help':
            a = f"""{Fore.BLUE}
        [+] Usage [+]

         [Rot47] > 1 
         [zlib] > 2      
         [Exit] > exit
             """
            print(a)

        elif menu_handler == "4":
            print("\n Goodbye")

        elif menu_handler == "clear":
            clear()

        elif menu_handler == "exit":
            exit()

        elif menu_handler != "":
            handler()

        else:
            handler()
handler()







