#Exercício Problema 1
#João Pedro Marques e Rafael Madarás
import random

fichas = 1000

ComeOut = True

while ComeOut and fichas > 0:
    print("__________________________________________________")
    print("Bem-vindo ao jogo Craps Insper!!")
    print("Instruções: Utilize letra maiúscula para responder!")
    print("Modo de escrita: Sim, Não, Apostar, Sair do jogo,")
    print("Twelve, Pass Line Bet, Any Bet, Field.")
    um = input("Quer apostar ou sair do jogo?\n")

    if um == "Sair do jogo":
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
            print("Você tem {0} fichas".format(fichas))
            apostac = int(input("Quantas fichas quer apostar?\n"))
            dc1 = random.randint(1,6)
            dc2 = random.randint(1,6)
            sc = dc1 + dc2

            if sc == 2:
                print("A soma deu {0}" .format(sc))
                fichas = fichas + (7)*(apostac)
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True
            if sc == 3:
                print("A soma deu {0}" .format(sc))
                fichas = fichas + (7)*(apostac)
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True
            if sc == 12:
                print("A soma deu {0}" .format(sc))
                fichas = fichas + (7)*(apostac)
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True
            if (sc == 4 or sc == 5 or sc == 6 or sc == 7 or sc == 8 or sc == 9 or sc == 10 or sc == 11):
                print("A soma deu {0}".format(sc))
                fichas = fichas - apostac
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True

        if x == 'Field':           
            print("Você tem {0} fichas".format(fichas))
            apostaf = int(input("Quantas fichas quer apostar?\n"))
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
            

            d1 = random.randint(1,6)
            d2 = random.randint(1,6)

            soma = d1 + d2
            print("Você tem {0} fichas".format(fichas))   
            aposta = int (input("Quantas fichas quer apostar?\n"))
            XP=[7,11]

            if soma in XP :
                print("A soma deu {0} ".format(soma))
                fichas = fichas + aposta
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True
            NP = [2,3,12]
            if soma in NP:
                print("A soma deu {0} ".format(soma))
                fichas = fichas - aposta
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True
            
            banana = [4,5,6,8,9,10,11]
            if soma in banana:
                print("A soma deu {0}".format(soma))                
                print("_________________________________________________")
                print("_________________________________________________")
                print("Você está na fase do Point!")
                                              
                p2 = input("Você quer mudar o tipo de aposta? Se sim, qual?\n")
                point = True
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
                    morango = [5,6,7,8]
                    if soma in morango:
                        print("A soma deu {0} ".format(soma))
                        fichas = fichas - aposta
                        print("Você tem {0} fichas".format(fichas))
                        ComeOut = True
                    abacaxi = [3,4,9,10,11]
                    if soma in abacaxi:
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
                    lista = [2,3,12]   
                    if somap in lista:
                        print("A soma deu {0} ".format(somap))
                        fichas = fichas + 7*aposta
                        print("Você tem {0} fichas".format(fichas))                    
                        ComeOut = True
                    if somap not in lista:
                        print("A soma deu {0} ".format(soma))
                        fichas = fichas - aposta
                        print("Você tem {0} fichas".format(fichas))
                        ComeOut = True            

                else:                                   
                    point = True
                    while point:
                        if somap == 7:
                            point = False
                            print("A soma deu {0}".format(somap))
                            fichas = fichas - aposta
                            print("Você tem {0} fichas".format(fichas))
                            
                            ComeOut = True
                        if somap == soma:
                            point = False
                            print("A soma deu {0}".format(somap))
                            fichas = fichas + aposta
                            print("Você tem {0} fichas".format(fichas))
                            
                            ComeOut = True
                        else:
                            point = True