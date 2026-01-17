# Inicialização do portscan

import sys
import socket # <- Biblioteca responsável pelos comandos de criação de socket 
import time
import threading



if len(sys.argv) <= 1:


    print(r"   __        ______     ______     ______     __   __      ______   __  __    ")
    print(r"  /\ \      /\  ___\   /\  ___\   /\  __ \   /\ '-.\ \    /\  == \ /\ \_\ \   ")
    print(r" _\_\ \     \ \___  \  \ \ \____  \ \  __ \  \ \ \-.  \   \ \  _-/ \ \____ \  ")
    print(r"/\_____\     \/\_____\  \ \_____\  \ \_\ \_\  \ \_\\'\_\   \ \_\    \/\_____\ ")
    print(r"\/_____/_____ \/_____/   \/_____/   \/_/\/_/   \/_/ \/_/ o  \/_/     \/_____/ ")
    print(r"                                                                             ")


    def print_startup_message():
        message = f"""

        ========================================================
        ||                                                    ||
        || <Modo de uso objetivo>                             ||
        ||   script.py IP e Porta                             ||
        ||   script.py (digite: "DNS") o seusite.com e Porta  ||
        ||                                                    ||
        || <Modo de uso mapeado>                              ||
        ||   script.py (digite:"map") e o IP                  ||
        ||   script.py (digite: "DNS-map") e o seusite.com    ||
        ||                                                    ||
        ========================================================
        """
        print(message)
    if __name__ == "__main__":
        # Imprime a mensagem de inicialização
            print_startup_message()
            exit()
    

elif sys.argv[1] == "map":

    try:
        ip = sys.argv[2]

        partes =  ip.split('.')
        # Validação do IP
        if len(partes) != 4:
            raise ValueError("<Passe um endereço IP válido>")  
    
     # Verifica os intervalos do IP
    
        for intervalo in partes: 
            if not 0 <= int(intervalo) <= 254:
                raise ValueError("<Intervalo e IP inválido>")
    # Animação de carregamento
        char = ''
        p=0
        while True:
            print(f"{char}\r", end='')
            time.sleep(0.1)
            if p == 0:
                char = '\nLoading ⢿ |'
                p+=1
            elif p == 1:
                char = 'Loading ⣻ \\'
                p+=1
            elif p == 2:
                char = 'Loading ⣽ -'
                p+=1
            elif p == 3:
                char = 'Loading ⣾ /'
                p+=1
            elif p == 4:
                char = 'Loading ⣷ |'
                p+=1
            elif p == 5:
                char = 'Loading ⣯ \\'
                p+=1
            elif p == 6:
                char = 'Loading ⣟ -'
                p+=1
            elif p == 7:
                char = 'Loading ⡿ /'
                p+=1
            elif p == 8:
                char = 'Loading ⣿ |'
                p+=1
            elif p == 9:
                char = 'Loading ⣿ \\'
                p=0
                
     # Range de portas
                for prt in range(1,65535):   
                    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    if meusocket.connect_ex((ip,prt)) == 0:
                        print(f"Porta {prt} [ABERTA]")
                        #imprimir o Banner do servço na tela     
                        timeout = 3 # O Banner tem 3 segundos para responder.
                        meusocket.settimeout(timeout) 
                        try:
                            banner2 = meusocket.recv(1024)
                            print(f"{banner2.decode()}")            
                            
                        except socket.timeout:    
                                print(f"banner: (Port {prt}) tempo de resposta ecedido.") # Caso não responda, esta mensagem aparecerá

                meusocket.close()    
                       
    except ValueError as d:
        print(f"\n{d}\n")
        exit()

elif sys.argv[1] == "DNS-map":
    
    dns = sys.argv[2]

    char2 = ''
    p=0
    while True:
        print(f"{char2}\r", end='')
        time.sleep(0.1)
        if p == 0:
            char2 = '\nLoading ⢿ |'
            p+=1
        elif p == 1:
            char2 = 'Loading ⣻ \\'
            p+=1
        elif p == 2:
            char2 = 'Loading ⣽ -'
            p+=1
        elif p == 3:
            char2 = 'Loading ⣾ /'
            p+=1
        elif p == 4:
            char2 = 'Loading ⣷ |'
            p+=1
        elif p == 5:
            char2 = 'Loading ⣯ \\'
            p+=1
        elif p == 6:
            char2 = 'Loading ⣟ -'
            p+=1
        elif p == 7:
            char2 = 'Loading ⡿ /'
            p+=1
        elif p == 8:
            char2 = 'Loading ⣿ |'
            p+=1
        elif p == 9:
            char2 = 'Loading ⣿ \\'
            p=0
            socket.gethostbyname(dns)
            for prt2 in range(1,65535):   
               meusocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               if meusocket2.connect_ex((dns,prt2)) == 0:
                    print(f"Porta {prt2} [ABERTA]")
                # imprimir o Banner do servço na tela     
                    timeout = 3 # O Banner tem 3 segundos para responder.
                    meusocket2.settimeout(timeout) 
                    try:
                        banner3 = meusocket2.recv(1024)
                        print(f"{banner3.decode()}")
                    except socket.timeout:    
                            print(f"banner: (Pot {prt2}) tempo de resposta ecedido.") # Caso não responda, esta mensagem                             meusocket2.close()
    
elif sys.argv[1] == "DNS":
    try:
        dns2 = sys.argv[2]
        socket.gethostbyname(dns2)
        # Validação da porta
        porta2 = int(sys.argv[3])
        if not 0 <= int(porta2) <= 65535:
            raise ValueError ("<Nº da Porta inexistente>")
        
        meusocketdns = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        rst = meusocketdns.connect_ex((dns2,porta2))

        if (rst == 0):
        
            print("                            _____     ")
            print(r" _            _  _         |     |   ")    
            print(r"|_) _  _ |_  / \|_) _ __   |     |   ")
            print(r"|  (_)|  |_  \_/|  (/_| |  |     |   ")
            print(r"                            /   \    ")
            print(r"                           /     \   ")
            print(r"                          /       \  ")


            print("\n[Port OPEN]")
            
            #imprimir o Banner do servço na tela 
            timeout = 6 # O Banner tem 3 segundos para responder.
            meusocketdns.settimeout(timeout) 
            try:
                banner2 = meusocketdns.recv(1024)
                print(f"\n{banner2.decode()}\n")            
                exit()
            except socket.timeout:    
                    print(f"banner: (Port {porta2}) response time exceeded") # Caso não responda a tempo, esta mensagem aparecerá
                    meusocketdns.close()
                    exit()

        else:
            print()
            print("                            _____   ")        
            print(r" _            _            |     |")    
            print(r"|_) _  _ |_  | \ _    __   |o    |   ")
            print(r"|  (_)|  |_  |_/(_)\^/| |  |     |    ")
            
    
            print("\n[Port DOWN]\n")
    except ValueError as d:
        print(f"\n{d}\n")

try:
    ip2 = sys.argv[1]
    partes =  ip2.split('.')
    # Validação do IP
    if len(partes) != 4:
        raise ValueError("<Passe um endereço IP válido>")  
    
    # Verifica os intervalos do IP
    for intervalo in partes: 
        if not 0 <= int(intervalo) <= 254:
            raise ValueError("<Intervalo e IP inválido>")
        
    # Validação da porta
    porta = int(sys.argv[2])
    if not 0 <= int(porta) <= 65535:
        raise ValueError ("<Nº da Porta inexistente>")
        

    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # <socket.socket> qr dzr informar a biblioteca "socket" para usar o comando "socket"| (lib-> socket.socket <-command)

    # o resultado da conxão sairá na variável "rst".
    # "connect_ex" retorna um indicador de erro
    rst = meusocket.connect_ex((ip2,porta))
                
    if socket.AF_INET == None:
        print("\n<Alvo inexistente!!>\n")
  
    # Se o resultado da conxão for "0" (Verdadeiro), aparecerá a mensagem de porta aberta. Senão, porta fechada.
    elif (rst == 0):

        print("                            _____     ")
        print(r" _            _  _         |     |   ")    
        print(r"|_) _  _ |_  / \|_) _ __   |     |   ")
        print(r"|  (_)|  |_  \_/|  (/_| |  |     |   ")
        print(r"                            /   \    ")
        print(r"                           /     \   ")
        print(r"                          /       \  ")


        print("\n[Port OPEN]")
        
        #imprimir o Banner do servço na tela 
        timeout = 6 # O Banner tem 3 segundos para responder.
        meusocket.settimeout(timeout) 
        try:
            banner2 = meusocket.recv(1024)
            print(f"\n{banner2.decode()}\n")            
            exit()
        except socket.timeout:    
                print(f"banner: (Port {porta}) response time exceeded") # Caso não responda a tempo, esta mensagem aparecerá
                meusocket.close()
                exit()

    else:
        print()
        print("                            _____   ")        
        print(r" _            _            |     |")    
        print(r"|_) _  _ |_  | \ _    __   |o    |   ")
        print(r"|  (_)|  |_  |_/(_)\^/| |  |     |    ")
        
 
        print("\n[Port DOWN]\n")
except ValueError as e:
 print(f"\n{e}\n")
