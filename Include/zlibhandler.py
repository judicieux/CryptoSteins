import zlib
from colorama import Fore, Style, init

def zlib_menu():
    try:
        file = input(f"{Fore.RED}[Zlib] > ")

        if file == 'help':
            a = f"""{Fore.BLUE}
         [+] Usage [+]
                    
    [Compress]   > zlibcompress
    [Decompress] > zlibdecompress
    [Exit]       > exit
            """
            print(a)
            zlib_menu()

        elif file == 'zlibcompress':
            filetocompress = input(f"{Fore.BLUE}[+] File to compress [+] > ")
            initialfile = open(filetocompress, 'rb').read()
            compressedfile = zlib.compress(initialfile, 9)
            f = open(filetocompress + '_compressed', 'wb')
            f.write(compressedfile)
            f.close()
            print(f"{Fore.BLUE}[+] Saved [+]\n{Fore.YELLOW}" + filetocompress.replace(' ', '-') + '_compressed')
            zlib_menu()

        elif file == 'zlibdecompress':
            filetodecompress = input(f"{Fore.BLUE}[+] File to decompress [+] > ")
            compressedfile = open(filetodecompress, 'rb').read()
            decompressedfile = zlib.decompress(compressedfile)
            f = open(filetodecompress.replace('_compressed', '_decompressed'), 'wb')
            f.write(decompressedfile)
            f.close()
            print(f"{Fore.BLUE}[+] Saved [+]\n{Fore.YELLOW}" + filetodecompress.replace('_compressed', '_decompressed'))
            zlib_menu()

        elif file == "exit":
            print(f"{Fore.YELLOW}[+] Exit [+]")

        else:
            zlib_menu()

    except FileNotFoundError:
        zlib_menu()

    except SyntaxError:
        print("[+] Error [+]")

    except ValueError:
        print("[+] Error [+]")
