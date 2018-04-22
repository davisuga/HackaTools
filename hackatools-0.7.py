import os
import socket

confiaveis = ['www.google.com', 'www.yahoo.com', 'www.fb.com']
app = []
c = ['forensic', 'mobile', 'firmware', 'keylogger', 'webapp', 'crypto', 'reversing', 'database',
         'threat-model', 'fuzzer', 'backdoor', 'sniffer', 'bluetooth', 'packer', 'scanner', 'binary', 'social',
         'code-audit', 'drone', 'proxy', 'networking', 'recon', 'tunnel', 'nfc', 'windows', 'misc', 'hardware',
         'networking', 'anti-forensic', 'dos', 'exploitation', 'automation', 'ids', 'cracker', 'defensive',
         'fingerprint', 'decompiler', 'cryptography', 'voip', 'wireless', 'honeypot', 'radio', 'gpu', 'spoof',
         'malware', 'debugger', 'unpacker']

def iniciar():
    if os.geteuid() != 0:
        exit("You need to have root privileges to run HackaTools.\nPlease try again, this time using 'sudo'. Exiting.")
    if check_host() == True:
        a = input('Have you installed the dependencies? (Y/n)')
        if a == 'Y' or a == 'y':
            menu()
        elif a == 'N' or a == 'n':
            submenu0()
            menu()
        else:
            print('Type a valid option!!!')
            iniciar()
    else:
        print('No internet conection.')
        exit()


def check_host():
    global confiaveis
    for host in confiaveis:
        a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a.settimeout(.5)
        try:
            b = a.connect_ex((host, 80))
            if b == 0:
                return True
        except:
            pass
        a.close()
    return False


def menu():
    a = input('''\033[33m
    /  |                          /  |                  /  |                        /  |          
    $$ |____    ______    _______ $$ |   __   ______   _$$ |_     ______    ______  $$ |  _______ 
    $$      \  /      \  /       |$$ |  /  | /      \ / $$   |   /      \  /      \ $$ | /       |
    $$$$$$$  | $$$$$$  |/$$$$$$$/ $$ |_/$$/  $$$$$$  |$$$$$$/   /$$$$$$  |/$$$$$$  |$$ |/$$$$$$$/ 
    $$ |  $$ | /    $$ |$$ |      $$   $$<   /    $$ |  $$ | __ $$ |  $$ |$$ |  $$ |$$ |$$      \ 
    $$ |  $$ |/$$$$$$$ |$$ \_____ $$$$$$  \ /$$$$$$$ |  $$ |/  |$$ \__$$ |$$ \__$$ |$$ | $$$$$$  |
    $$ |  $$ |$$    $$ |$$       |$$ | $$  |$$    $$ |  $$  $$/ $$    $$/ $$    $$/ $$ |/     $$/ 
    $$/   $$/  $$$$$$$/  $$$$$$$/ $$/   $$/  $$$$$$$/    $$$$/   $$$$$$/   $$$$$$/  $$/ $$$$$$$/  V 0.7

     \033[36mA nice hacking tools installer :)                                                                   

    \033[37mDevelopers: (RootSec.net)
        \033[36mPedro Cleto     -> cleto@rootsec.net
        \033[35mDavi William    -> davi@rootsec.net
\033[32m
    To install the tools you need to install dependencies.

    1) Install only one tool.
    2) Install a list of tools.
    3) Exit.

     ┌─[H4ck4t00ls]:~
     └──> ''')
    if a == '1':
        submenu1()
    elif a == '2':
        submenu2()
    elif a == '3':
        exit()
    else:
        print("Type a valid option!!!")
        menu()


def submenu0():
    a = input('''
    Are going to be installed:
        - jshon
        - expac
        - packer
        - strap
        - blackman

    All ok? (Y/n)

     ┌─[H4ck4t00ls]:~
     └──> ''')
    if a == 'Y' or a == 'y':
        os.system('sudo pacman -S jshon; S')
        os.system('sudo pacman -S expac; S')
        os.system('cd /home/')
        os.system('git clone https://aur.archlinux.org/packer.git')
        os.system('cd packer')
        os.system('makepkg')
        os.system('sudo pacman -Syyu')
        os.system('curl -O https://blackarch.org/strap.sh')
        os.system('sudo chmod +x strap.sh')
        os.system('sudo ./strap.sh')
        os.system('sudo pacman -S blackman')
    if a == 'N' or a == 'n':
        menu()
    else:
        print('Type a valid option!!!')
        submenu0()


def submenu1():
    a = input('''
    Select the tool category to install now.

    - back         - forensic     - mobile      - firmware       - keylogger
    - webapp       - crypto       - reversing   - database       - threat-model
    - fuzzer       - backdoor     - sniffer     - bluetooth      - packer
    - scanner      - binary       - social      - code-audit     - drone
    - proxy        - networking   - recon       - tunnel         - nfc
    - windows      - misc         - hardware    - networking     - anti-forensic
    - dos          - exploitation - automation  - exploitation   - ids
    - cracker      - defensive    - fingerprint - decompiler     - cryptography
    - voip         - wireless     - honeypot    - radio          - gpu
    - spoof        - malware      - debugger    - unpacker       


    ┌─[H4ck4t00ls]:~
    └──> ''')
    if a in c:
        print('\033[34mSystem is downloading the list... ')
        tools = str(os.system('blackman -p blackarch-{}'.format(a)))
        b = input('''type the tool you want to install:
    ┌─[H4ck4t00ls]:~
    └──>''')
        if tools.find(b):
            os.system('sudo pacman -S {}'.format(b))
            submenu1()
        elif b == 'back':
            submenu1()
        else:
            print('Type a valid option!!!')
            submenu1()
    elif a == 'back':
        menu()
    else:
        print('Type a valid option!!!')
        submenu1()


def submenu2():
    a = input('''
    Select the tool category to add to the list.

    - back         - forensic     - mobile      - firmware       - keylogger        
    - webapp       - crypto       - reversing   - database       - threat-model     
    - fuzzer       - backdoor     - sniffer     - bluetooth      - packer           
    - scanner      - binary       - social      - code-audit     - drone            
    - proxy        - networking   - recon       - tunnel         - nfc              
    - windows      - misc         - hardware    - networking     - anti-forensic    
    - dos          - exploitation - automation  - ids            - cryptography 
    - cracker      - defensive    - fingerprint - decompiler     - gpu     
    - voip         - wireless     - honeypot    - radio          - all              
    - spoof        - malware      - debugger    - unpacker                    

    List: {}
    Type 'install' to install all your list. :)

    ┌─[H4ck4t00ls]:~
    └──> '''.format(app))
    if a in c:
        print('System is downloading the list...')
        tools = str(os.system('blackman -p blackarch-{}'.format(a)))
        b = input('''type the tool you want to add to the list:
    ┌─[H4ck4t00ls]:~
    └──>''')
        if b == 'back':
            submenu2()
        elif tools.find(b):
            app.append('{}'.format(b))
            submenu2()
        else:
            print('Type a valid option!!!')
            submenu2()
    elif a == 'back':
        menu()
    elif a == 'install':
        for i in range(0, len(app)):
            os.system('sudo pacman -S {}'.format(app[i]))
    else:
        print('Type a valid option!!!')

iniciar()
