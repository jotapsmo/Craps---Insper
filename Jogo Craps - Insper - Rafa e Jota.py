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
            print("Você tem {0} fichas".format(fichas))
            apostac = int(input("Quantas fichas quer apostar?"))
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
            apostab = int(input("Quanto você quer apostar?"))
            db1 = random.randint(1,6)
            db2 = random.randint(1,6)
            sb = db1 + db2



            if sb == 7:
                print("A soma deu {0}".format(sb))
                fichas = fichas + apostab
                print("Você tem {0}".format(fichas))
                ComeOut = True




            if sb == 11:
                print("A soma deu {0}".format(sb))
                fichas = fichas + apostab
                print("Você tem {0}".format(fichas))
                ComeOut = True




            craps = [2, 3, 12]
            if sb in craps:
                print("A soma deu {0}".format(sb))
                fichas = fichas - apostab
                print("Você tem {0} fichas".format(fichas))
                ComeOut = True




            banana = [4, 5, 6, 8, 9, 10]
            if sb in banana:
                print("Você está na fase do Point!")
                print("O point é {0}".format(sb))
                jogo = input("Você quer mudar a aposta?")
                if jogo == "Twelve":
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
                    
                if jogo == "Field":
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

                if jogo == "Any Craps":

                    print("Você tem {0} fichas".format(fichas))
                    apostac = int(input("Quantas fichas quer apostar?"))
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
                else:                
                    Point = True
                    while Point:
                        n1 = random.randint(1, 6)
                        n2 = random.randint(1, 6)
                        snp = n1 + n2

                        if sb == snp:
                            print("A soma deu {0}".format(snp))
                            fichas = fichas + apostab
                            print("Você tem {0} fichas".format(fichas))
                            Point = False
                            ComeOut = True
                        if snp == 7:
                            print("A soma deu {0}".format(snp))
                            fichas = fichas - apostab
                            print("Você tem {0} fichas".format(fichas))
                            Point = False
                            ComeOut = True
                        else:
                            Point = True