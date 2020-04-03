import random
ComeOut = True
fichas = 100

while ComeOut and fichas > 0:
    print("__________________________________________________")
    print("Bem-vindo ao jogo Craps Insper!!")
    print("Instrução: Utilize letra maiúscula para responder! ")
    
    um = input("Quer apostar ou sair do jogo?")

    if um == "sair do jogo":
        break
    else:
        print("Você está na fase Come Out.")
        
        x = input("Você quer qual tipo de aposta?")
        
        if x == 'Twelve':
            print("Você tem {0} fichas".format(fichas))
            aposta = int(input("Quantas fichas quer apostar?"))
            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            soma = d1 + d2
            
            if soma == 12:
                print("A soma deu {0} ".format(soma))                   
                fichas = fichas + 30*aposta
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True
                
            else:
                print("A soma deu {0} ".format(soma))
                fichas = fichas - aposta                    
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True
        
        if x == 'Any Craps':
            
            aposta = int (input("Quantas fichas quer apostar?"))
            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            soma = d1 + d2
                
            if soma == 2 or soma == 3 or soma == 12:
                print("A soma deu {0} ".format(soma))
                fichas = fichas + 7*aposta
                print("Você tem {0} fichas".format(fichas))                    
                ComeOut = True
            else:
                print("A soma deu {0} ".format(soma))
                fichas = fichas - aposta
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True
        
        if x == 'Field':           
            print("Você tem {0} fichas".format(fichas))
            aposta = int (input("Quantas fichas quer apostar?"))

            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            soma = d1 + d2
            if soma == 5 or 6 or 7 or 8:
                print("A soma deu {0} ".format(soma))
                fichas = fichas - aposta
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True
            
            if soma == 3 or 4 or 9 or 10 or 11:
                print("A soma deu {0} ".format(soma))
                fichas = fichas + aposta
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True
            if soma == 2:
                print("A soma deu {0} ".format(soma))
                fichas = fichas + 2*aposta
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True
            if soma == 12:
                print("A soma deu {0} ".format(soma))
                fichas = fichas + 3*aposta
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True

        if x == 'Pass Line Bet':       
            aposta = int (input("Quantas fichas quer apostar?"))

            d1 = random.randint(1,6)
            d2 = random.randint(1,6)

            soma = d1 + d2

            if soma == 7 or soma == 11:
                print("A soma deu {0} ".format(soma))
                fichas = fichas + aposta
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True
            if soma == 2 or soma == 3 or soma == 12:
                print("A soma deu {0} ".format(soma))
                fichas = fichas - aposta
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True
            else:
                print("A soma deu {0}".format(soma))
                point = True
                print("__________________________________________________")
                print("Você está na fase do Point")
                print("Você tem {0} fichas".format(fichas))                
                p2 = input("Você quer mudar o tipo de aposta? Se sim, qual?")
                dp1 = random.randint(1,6)
                dp2 = random.randint(1,6)
                somap = dp1 + dp2
                
                if p2 == 'Twelve':
                    print("Você tem {0} fichas".format(fichas))
                    aposta = int(input("Quantas fichas quer apostar?"))
                    d1 = random.randint(1,6)
                    d2 = random.randint(1,6)
                    soma = d1 + d2
            
                    if soma == 12:
                        print("A soma deu {0} ".format(soma))                   
                        fichas = fichas + 30*aposta
                        print("Você tem {0} fichas".format(fichas))
                        ComeOut = True
                        
                    else:
                        print("A soma deu {0} ".format(soma))
                        fichas = fichas - aposta                    
                        print("Você tem {0} fichas".format(fichas))
                        ComeOut = True
                
                if p2 == "Field":
                    aposta = int (input("Quantas fichas quer apostar?"))
                    d1 = random.randint(1,6)
                    d2 = random.randint(1,6)
                    soma = d1 + d2
                    if soma == 5 or 6 or 7 or 8:
                        print("A soma deu {0} ".format(soma))
                        fichas = fichas - aposta
                        print("Você tem {0} fichas".format(fichas))
                        ComeOut = True
                    if soma == 3 or 4 or 9 or 10 or 11:
                        print("A soma deu {0} ".format(soma))
                        fichas = fichas + aposta
                        print("Você tem {0} fichas".format(fichas))
                        ComeOut = True
                    if soma == 2:
                        print("A soma deu {0} ".format(soma))
                        fichas = fichas + 2*aposta
                        print("Você tem {0} fichas".format(fichas))
                        ComeOut = True
                    if soma == 12:
                        print("A soma deu {0} ".format(soma))
                        fichas = fichas + 3*aposta
                        print("Você tem {0} fichas".format(fichas))
                        ComeOut = True

                if p2 == "Any Craps":
                    aposta = int (input("Quantas fichas quer apostar?"))
                    d1 = random.randint(1,6)
                    d2 = random.randint(1,6)
                    soma = d1 + d2
                        
                    if soma == 2 or soma == 3 or soma == 12:
                        print("A soma deu {0} ".format(soma))
                        fichas = fichas + 7*aposta
                        print("Você tem {0} fichas".format(fichas))                    
                        ComeOut = True
                    else:
                        print("A soma deu {0} ".format(soma))
                        fichas = fichas - aposta
                        print("Você tem {0} fichas".format(fichas))
                        ComeOut = True            

                else:                                   
                    while point:
                        if somap == 7:
                            print("A soma deu {0}".format(somap))
                            fichas = fichas - aposta
                            print("Você tem {0} fichas".format(fichas))
                            ComeOut = True
                        if somap == soma:
                            print("A soma deu {0}".format(somap))
                            fichas = fichas + aposta
                            print("Você tem {0} fichas".format(fichas))
                            ComeOut = True
                        else:
                            point = True