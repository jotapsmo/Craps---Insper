import random

fichas = 1000

ComeOut = True

while ComeOut and fichas > 0:
    print("__________________________________________________")
    print("Bem-vindo ao jogo Craps Insper!!")
    print("Instrução: Utilize letra maiúscula para responder! ")
    
    um = input("Quer apostar ou sair do jogo?\n")

    if um == "sair do jogo":
        break
    else:
        print("Você está na fase Come Out.")
        
        x = input("Você quer qual tipo de aposta?\n")
        
        if x == 'Twelve':
            print("Você tem {0} fichas".format(fichas))
            apostat = int(input("Quantas fichas quer apostar?\n"))
            dt1 = random.randint(1,6)
            dt2 = random.randint(1,6)
            somat = dt1 + dt2
            
            if somat == 12:
                print("A soma deu {0} ".format(somat))                   
                fichas = fichas + 30*apostat
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True
                
            else:
                print("A soma deu {0} ".format(somat))
                fichas = fichas - apostat                    
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True
        
        if x == 'Any Craps':

            d1 = random.randint(1,6)
            d2 = random.randint(1,6)
            soma = d1 + d2

            aposta = int (input("Quantas fichas quer apostar?\n"))

            print("A soma deu {0} ".format(soma))
            if soma != 2 or soma != 3 or soma != 12:
                fichas = (fichas) - (aposta)
                print("Você tem {0} fichas".format(fichas))

                ComeOut = True
            else:
                fichas = (fichas) + ((7)*(aposta))

                print("Você tem {0} fichas".format(fichas))

                ComeOut = True
        
        if x == 'Field':           
            print("Você tem {0} fichas".format(fichas))
            apostaf = int(input("Quantas fichas quer apostar?"))
            df1 = random.randint(1,6)
            df2 = random.randint(1,6)
            sf = df1 + df2
            
            if sf == 2:
                print("A soma deu {0} ".format(sf))
                fichas = fichas + (2)*(apostaf)
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True
            
            if sf == 12:
                print("A soma deu {0} ".format(sf))
                fichas = fichas + (3)*(apostaf)
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True

            if (sf == 5 or sf == 6 or sf == 7 or sf == 8):
                print("A soma deu {0} ".format(sf))
                fichas = fichas - apostaf
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True
            
            if (sf == 3 or sf == 4 or sf == 9 or sf == 10 or sf == 11):
                print("A soma deu {0} ".format(sf))
                fichas = fichas + apostaf
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True

        if x == 'Pass Line Bet':    
            print("Você tem {0} fichas".format(fichas))   
            aposta = int (input("Quantas fichas quer apostar?\n"))

            d1 = random.randint(1,6)
            d2 = random.randint(1,6)

            soma = d1 + d2

            if soma == 7 or 11:
                print("A soma deu {0} ".format(soma))
                fichas = fichas + aposta
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True
            
            if soma == 2 or 3 or 12:
                print("A soma deu {0} ".format(soma))
                fichas = fichas - aposta
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True
            
            else:
                print("A soma deu {0}".format(soma))
                point = True
                print("_________________________________________________")
                print("Você está na fase do Point")
                               
                p2 = input("Você quer mudar o tipo de aposta? Se sim, qual?\n")
                dp1 = random.randint(1,6)
                dp2 = random.randint(1,6)
                somap = dp1 + dp2
                
                if p2 == 'Twelve':
                    print("Você tem {0} fichas".format(fichas))
                    aposta = int(input("Quantas fichas quer apostar?\n"))
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
                    aposta = int (input("Quantas fichas quer apostar?\n"))
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
                    print("Você tem {0} fichas".format(fichas))
                    aposta = int (input("Quantas fichas quer apostar?\n"))
                    dp1 = random.randint(1,6)
                    dp2 = random.randint(1,6)
                    somap = dp1 + dp2
                        
                    if somap == 2 or 3 or 12:
                        print("A soma deu {0} ".format(somap))
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