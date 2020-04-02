import random

ComeOut = True

fichas = 1000

while ComeOut and fichas > 0:
    
    um = input("Quer apostar ou sair do jogo?")

    if um == "sair do jogo":
        break
    
    else:
        print("Você está na fase Come Out.")
        x = input("Você quer qual tipo de aposta?")
        
        if x == 'Twelve':
            print("Você tem {0} fichas".format(fichas))
            aposta = int (input("Quantas fichas quer apostar?"))
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
                fichas = fichas - aposta
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True
        
        if x == 'Field':           
            aposta = int (input("Quantas fichas quer apostar?"))
            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            soma = d1 + d2
            if soma == 5 or 6 or 7 or 8:
                print("A soma deu {0} ".format(soma))
                fichas = fichas - aposta
                print("Você tem {0} fichas".format(fichas))
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
                print("Você está na fase do Point")
                dp1 = random.randint(1,6)
                dp2 = random.randint(1,6)

                somap = dp1 + dp2

                point = True
                while point:
                    if somap == 7:
                        fichas = fichas - aposta
                        print("Você tem {0} fichas".format(fichas))
                        ComeOut = True
                    else:
                        y  = input("Você quer alguma nova aposta ou apenas seguir?")
                        if y == 'Twelve':                  
                            if soma == 12:
                                fichas = fichas + 30*aposta
                                print("Você tem {0} fichas".format(fichas))
                                ComeOut = True
                            else:
                                fichas = fichas - aposta
                                print("Você tem {0} fichas".format(fichas))
                                ComeOut = True
                
                if y == 'Any Craps':                                     
                    if soma == 2 or soma == 3 or soma == 12:
                        fichas = fichas + 7*aposta
                        print("Você tem {0} fichas".format(fichas))
                        ComeOut = True
                    else:
                        fichas = fichas - aposta
                        print("Você tem {0} fichas".format(fichas))
                        ComeOut = True
                
                if y == 'Field':
                    if soma == 5 or 6 or 7 or 8:
                        fichas = fichas - aposta
                        print("Você tem {0} fichas".format(fichas))

                    if soma == 3 or 4 or 9 or 10 or 11:
                        fichas = fichas + aposta
                        print("Você tem {0} fichas".format(fichas))
                        ComeOut = True
                    if soma == 2:
                        fichas = fichas + 2*aposta
                        print("Você tem {0} fichas".format(fichas))
                        ComeOut = True
                    if soma == 12:
                        fichas = fichas + 3*aposta
                        print("Você tem {0} fichas".format(fichas))
                        ComeOut = True
                
                if y == 'Seguir':   
                    print("O valor da soma era de {0}".format(soma))                
                    point = True
                    while point == True:
                        dp1 = random.randint(1,6)
                        dp2 = random.randint(1,6)
                        somap = dp1 + dp2
                        if somap == 7:
                            fichas = fichas - aposta
                            ComeOut = True                            

                        if somap == soma:
                            fichas = fichas + aposta
                            ComeOut = True
                        else:
                            point = True