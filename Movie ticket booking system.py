try:
    import sys
    import pygame
    import pickle
    from io import BytesIO
    import base64
    import time
    pygame.init()
    pygame.font.init()
    tkt = 0
    mov = ''
    phon = 0
    passwd = 0
    tme = ''
    fh1=open('display.dat','rb')
    c = pickle.load(fh1)
    c = base64.b64decode(c)
    c = BytesIO(c)
    c = pygame.image.load(c)
    DIS_ = pygame.display.set_mode((1020,500))
    global f
    f = 0
    font = pygame.font.SysFont('Arial',40)
    def bill():                                          
        pygame.init()
        DIS_ = pygame.display.set_mode((1020, 500))
        pygame.font.init()
        font = pygame.font.SysFont('Arial', 30)
        global price
        global price_1
        global tkt
        ticket_price=price
        food_price=price_1
        total_cost=ticket_price+food_price
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    a=input("Enter your feedback: ")
                    fb=open('story.txt','a+')
                    fb.write(a)
                    fb.close()
                    break
            DIS_.blit(c,(0,-100))
            text = font.render(f"Tickets: {tkt}", True, (252, 244, 3))
            DIS_.blit(text, (20, 20))
            text = font.render(f"Total Cost: Rupees{total_cost}", True, (252, 244, 3))
            DIS_.blit(text, (20, 60))
            bill_button = pygame.Rect(20, 200, 800, 50)
            pygame.draw.rect(DIS_, (0, 0, 255), bill_button)
            text = font.render("Total tickets booked and Total price. Thank you! Visit Again", True, (255, 255, 255))
            DIS_.blit(text, (80, 210))
            pygame.display.update()
    def login():                                             
      DIS_.blit(c,(0,-100))
      pygame.font.init()
      font = pygame.font.SysFont('Arial',30)
      password='123'
      txt = font.render('Enter password',True,(255,255,255))
      DIS_.blit(txt,(0,0))
      pygame.display.update()
      TypTxt = 0
      s=''
      p = True
      while p:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                p = False
                return 0
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_RETURN and 99 < TypTxt < 999:
                  s= TypTxt
                  p=False
                  if s!=123:
                    city()
                  elif s==123:
                    admin()
                  else:
                    DIS_.blit(c,(0,-100))
                    txt = font.render("wrong password",True,(255,255,255))
                    DIS_.blit(txt,(0,0))
                    pygame.display.update()
                    TypTxt = ''
                    p = True
                    while p:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                p = False
                                break
              elif event.unicode.isdigit() and TypTxt <= 1000:
                  TypTxt = (TypTxt * 10) + int(event.unicode)
                  DIS_.blit(c,(0,-100))
                  DIS_.blit(txt,(0,0))
                  Txt = font.render(f'{TypTxt}', True, (240, 32, 32))
                  DIS_.blit(Txt, (30, 450))
                  pygame.display.update()
              elif event.key == pygame.K_BACKSPACE:
                  TypTxt = TypTxt//10
                  DIS_.blit(c,(0,-100))
                  DIS_.blit(txt1,(0,0))
                  Txt = font.render(f'{TypTxt}', True, (240, 32, 32))
                  DIS_.blit(Txt, (30, 450))
                  pygame.display.update()
    def admin():
        import mysql.connector as sql
        con = sql.connect(host = "localhost" , user = "root" , password = "123" , database = "_Cinema_")
        if con.is_connected:   
            cur = con.cursor()
            cur.execute('select * from Movies;')
            w_ = cur.fetchall()
            o = []
            for i in range(0,len(w_)):
                o.append(w_[i][0])
        DIS_.blit(c,(0,-100))
        pygame.font.init()
        font = pygame.font.SysFont('Arial',30)
        DIS_.blit(c,(0,-100))
        txt = font.render('1) Update movie',True,(255,255,255))
        DIS_.blit(txt,(0,0))
        pygame.display.update()
        txt2 = font.render('2) Delete movie',True,(255,255,255))
        DIS_.blit(txt2,(0,50))
        pygame.display.update()
        txt3 = font.render('3) Update ticket',True,(255,255,255))
        DIS_.blit(txt3,(0,100))
        pygame.display.update()
        TXT = font.render("choose your option:",True,(255,255,255))
        DIS_.blit(TXT,(0,300))
        pygame.display.update()
        TypTxt = 0
        s=''
        pygame.display.update()
        p = True
        while p:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    p = False    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        s = TypTxt
                        p = False
                    elif event.unicode.isdigit() and TypTxt < 9:
                        TypTxt = int(event.unicode)
                        DIS_.blit(c,(0,-100))
                        DIS_.blit(txt,(0,0))
                        DIS_.blit(txt2,(0,50))
                        DIS_.blit(txt3,(0,100))
                        DIS_.blit(TXT,(0,300))
                        Txt = font.render(f'{TypTxt}', True, (100, 100, 100))
                        DIS_.blit(Txt, (30, 450))
                        pygame.display.update()
                    elif event.key == pygame.K_BACKSPACE:                      
                       TypTxt = TypTxt[:-1]
                       DIS_.blit(c,(0,-100))
                       DIS_.blit(txt,(0,0))
                       DIS_.blit(txt2,(0,50))
                       DIS_.blit(txt3,(0,100))
                       Txt = font.render(TypTxt, True, (240,32,32))
                       DIS_.blit(TXT,(0,300))
                       DIS_.blit(Txt, (30, 450))
                       pygame.display.update()
        pygame.display.update()
        if s > 3:
            city()
        elif s == 1:
            update()
        elif s == 2:
            delete()
        elif s == 3:
            update_tickets()
    import mysql.connector as sql
    def update_tickets():
        con = sql.connect(host="localhost", user="root", password="123", database="_Cinema_")
        if con.is_connected():
            cur = con.cursor()
            cur.execute("SELECT * FROM Tickets;")
            p = cur.fetchall()
            con.commit()
            b = p[0][0]  
            yt = b
            if yt <= 1:
                cur.execute(f"UPDATE Tickets SET No_of_Tickets = {180} WHERE No_of_Tickets = {yt};")
                con.commit()
                txt1 = "Successfully Updated"
                print(txt1)
                city()
            elif 2 <= yt <= 180:
                txt = "Sufficient tickets available"
                print(txt)
                city()
            else:
                city()
    def update():
        import mysql.connector as sql
        con = sql.connect(host = "localhost" , user = "root" , password = "123" , database = "_Cinema_")
        if con.is_connected:   
            cur = con.cursor()
            cur.execute('select * from Movies;')
            w_ = cur.fetchall()
            o = []
            for i in range(0,len(w_)):
                o.append(w_[i][0])
        DIS_.blit(c,(0,-100))
        pygame.display.update()
        txt1 = font.render("Which movie do you want to update?",True,(255,255,255))
        DIS_.blit(txt1,(0,0))
        pygame.display.update()
        txt2 = font.render(f"1,{o[0]}",True,(255,255,255))
        DIS_.blit(txt2,(0,50))
        pygame.display.update()
        txt3 = font.render(f"2,{o[1]}",True,(255,255,255))
        DIS_.blit(txt3,(0,100))
        pygame.display.update()
        txt4 = font.render(f"3,{o[2]}",True,(255,255,255))
        DIS_.blit(txt4,(0,150))
        pygame.display.update()
        txt5 = font.render(f"4,{o[3]}",True,(255,255,255))
        DIS_.blit(txt5,(0,200))
        pygame.display.update()
        txt6 = font.render(f"5,{o[4]}",True,(255,255,255))
        DIS_.blit(txt6,(0,250))
        pygame.display.update()
        txt7 = font.render(f"6,{o[5]}",True,(255,255,255))
        DIS_.blit(txt7,(0,300))
        pygame.display.update()
        TXT = font.render("choose your option:",True,(255,255,255))
        TypTxt = 0
        p = True
        while p:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    p = False    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        movie = o[TypTxt - 1]
                        p = False
                    elif event.unicode.isdigit() and TypTxt < 9:
                        TypTxt = int(event.unicode)
                        DIS_.blit(c,(0,-100))
                        DIS_.blit(txt1,(0,0))
                        DIS_.blit(txt2,(0,50))
                        DIS_.blit(txt3,(0,100))
                        DIS_.blit(txt4,(0,150))
                        DIS_.blit(txt5,(0,200))
                        DIS_.blit(txt6,(0,250))
                        DIS_.blit(txt7,(0,300))
                        DIS_.blit(TXT,(0,400))
                        Txt = font.render(f'{TypTxt}', True, (100, 100, 100))
                        DIS_.blit(Txt, (30, 450))
                        pygame.display.update()
                    elif event.key == pygame.K_BACKSPACE:
                        TypTxt = 0
                        DIS_.blit(c,(0,-100))
                        DIS_.blit(txt1,(0,0))
                        DIS_.blit(txt2,(0,50))
                        DIS_.blit(txt3,(0,100))
                        DIS_.blit(txt4,(0,150))
                        DIS_.blit(txt5,(0,200))
                        DIS_.blit(txt6,(0,100))
                        DIS_.blit(txt7,(0,150))
                        DIS_.blit(TXT,(0,400))
                        Txt = font.render('', True, (100,100,100))
                        DIS_.blit(TXT,(0,400))
                        DIS_.blit(Txt, (30, 450))
                        pygame.display.update()
        DIS_.blit(c,(0,-100))
        pygame.display.update()
        txt=font.render('Movie to add: ',True,(255,255,255))
        DIS_.blit(txt,(0,0))
        pygame.display.update()
        TypTxt1 = ''
        pygame.display.update()
        p = True
        while p:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    p = False    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        m=TypTxt1
                        import mysql.connector as sql
                        con = sql.connect(host = "localhost" , user = "root" , password = "123" , database = "_Cinema_")
                        if con.is_connected:
                            cur = con.cursor()
                            cur.execute(f"UPDATE Movies SET Movie_Name = '{TypTxt1}' WHERE Movie_Name = '{movie}';")
                            con.commit()
                            cur.execute('select * from Movies;')
                            w_ = cur.fetchall()
                            print(w_)
                        city()
                    elif event.unicode.isalpha() or event.unicode.isspace():
                        TypTxt1 += event.unicode
                        DIS_.blit(c,(0,-100))
                        DIS_.blit(txt,(0,0))
                        Txt = font.render(f'{TypTxt1}', True, (240, 32, 32))
                        DIS_.blit(Txt, (30, 450))
                        pygame.display.update()
                    elif event.key == pygame.K_BACKSPACE:
                        TypTxt1 = TypTxt1[:-1]
                        DIS_.blit(c,(0,-100))
                        DIS_.blit(txt,(0,0))
                        Txt = font.render(TypTxt1, True, (240,32,32))
                        DIS_.blit(Txt, (30, 450))
                        pygame.display.update()
        pygame.display.update()
    def delete():
        import mysql.connector as sql
        con = sql.connect(host = "localhost" , user = "root" , password = "123" , database = "_Cinema_")
        if con.is_connected:   
            cur = con.cursor()
            cur.execute('select * from Movies;')
            w_ = cur.fetchall()
            o = []
            for i in range(0,len(w_)):
                o.append(w_[i][0])
        DIS_.blit(c,(0,-100))
        pygame.display.update()
        txt1 = font.render("Which movie do you want to delete?",True,(255,255,255))
        DIS_.blit(txt1,(0,0))
        pygame.display.update()
        txt2 = font.render(f"1,{o[0]}",True,(255,255,255))
        DIS_.blit(txt2,(0,50))
        pygame.display.update()
        txt3 = font.render(f"2,{o[1]}",True,(255,255,255))
        DIS_.blit(txt3,(0,100))
        pygame.display.update()
        txt4 = font.render(f"3,{o[2]}",True,(255,255,255))
        DIS_.blit(txt4,(0,150))
        pygame.display.update()
        txt5 = font.render(f"4,{o[3]}",True,(255,255,255))
        DIS_.blit(txt5,(0,200))
        pygame.display.update()
        txt6 = font.render(f"5,{o[4]}",True,(255,255,255))
        DIS_.blit(txt6,(0,250))
        pygame.display.update()
        txt7 = font.render(f"6,{o[5]}",True,(255,255,255))
        DIS_.blit(txt7,(0,300))
        pygame.display.update()
        TXT = font.render("choose your option:",True,(255,255,255))
        TypTxt = 0
        p = True
        while p:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    p = False    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        movie = o[TypTxt - 1]
                        import mysql.connector as sql
                        con = sql.connect(host = "localhost" , user = "root" , password = "123" , database = "_Cinema_")
                        if con.is_connected:
                            cur = con.cursor()
                            cur.execute(f"UPDATE Movies SET Movie_Name = '' WHERE Movie_Name = '{movie}';")
                            con.commit()
                            cur.execute('select * from Movies;')
                            w_ = cur.fetchall()
                            print(w_)
                        city()
                        p = False
                    elif event.unicode.isdigit() and TypTxt < 9:
                        TypTxt = int(event.unicode)
                        DIS_.blit(c,(0,-100))
                        DIS_.blit(txt1,(0,0))
                        DIS_.blit(txt2,(0,50))
                        DIS_.blit(txt3,(0,100))
                        DIS_.blit(txt4,(0,150))
                        DIS_.blit(txt5,(0,200))
                        DIS_.blit(txt6,(0,250))
                        DIS_.blit(txt7,(0,300))
                        DIS_.blit(TXT,(0,400))
                        Txt = font.render(f'{TypTxt}', True, (100, 100, 100))
                        DIS_.blit(Txt, (30, 450))
                        pygame.display.update()
                    elif event.key == pygame.K_BACKSPACE:
                        TypTxt = 0
                        DIS_.blit(c,(0,-100))
                        DIS_.blit(txt1,(0,0))
                        DIS_.blit(txt2,(0,50))
                        DIS_.blit(txt3,(0,100))
                        DIS_.blit(txt4,(0,150))
                        DIS_.blit(txt5,(0,200))
                        DIS_.blit(txt6,(0,100))
                        DIS_.blit(txt7,(0,150))
                        DIS_.blit(TXT,(0,400))
                        Txt = font.render('', True, (100,100,100))
                        DIS_.blit(TXT,(0,400))
                        DIS_.blit(Txt, (30, 450))
                        pygame.display.update()
    pygame.display.update()
    def t_movie():
        global f
        f = f + 1
        import mysql.connector as sql
        con = sql.connect(host = "localhost" , user = "root" , password = "123" , database = "_Cinema_")
        if con.is_connected:   
            cur = con.cursor()
            cur.execute('select * from Movies;')
            w_ = cur.fetchall()
            o = []
            for i in range(0,len(w_)):
                o.append(w_[i][0])
        DIS_.blit(c,(0,-100))
        pygame.display.update()
        txt1 = font.render("Which movie do you want to watch?",True,(255,255,255))
        DIS_.blit(txt1,(0,0))
        pygame.display.update()
        txt2 = font.render(f"1,{o[0]}",True,(255,255,255))
        DIS_.blit(txt2,(0,50))
        pygame.display.update()
        txt3 = font.render(f"2,{o[1]}",True,(255,255,255))
        DIS_.blit(txt3,(0,100))
        pygame.display.update()
        txt4 = font.render(f"3,{o[2]}",True,(255,255,255))
        DIS_.blit(txt4,(0,150))
        pygame.display.update()
        txt5 = font.render(f"4,{o[3]}",True,(255,255,255))
        DIS_.blit(txt5,(0,200))
        pygame.display.update()
        txt6 = font.render(f"5,{o[4]}",True,(255,255,255))
        DIS_.blit(txt6,(0,250))
        pygame.display.update()
        txt7 = font.render(f"6,{o[5]}",True,(255,255,255))
        DIS_.blit(txt7,(0,300))
        pygame.display.update()
        txt8 = font.render("7, back",True,(255,255,255))
        DIS_.blit(txt8,(0,350))
        pygame.display.update()
        TXT = font.render("choose your option:",True,(255,255,255))
        TypTxt = 0
        p = True
        while p:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    p = False    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        movie = TypTxt
                        p = False
                    elif event.unicode.isdigit() and TypTxt < 9:
                        TypTxt = int(event.unicode)
                        DIS_.blit(c,(0,-100))
                        DIS_.blit(txt1,(0,0))
                        DIS_.blit(txt2,(0,50))
                        DIS_.blit(txt3,(0,100))
                        DIS_.blit(txt4,(0,150))
                        DIS_.blit(txt5,(0,200))
                        DIS_.blit(txt6,(0,250))
                        DIS_.blit(txt7,(0,300))
                        DIS_.blit(txt8,(0,350))
                        DIS_.blit(TXT,(0,400))
                        Txt = font.render(f'{TypTxt}', True, (100, 100, 100))
                        DIS_.blit(Txt, (30, 450))
                        pygame.display.update()
                    elif event.key == pygame.K_BACKSPACE:
                        TypTxt = 0
                        DIS_.blit(c,(0,-100))
                        DIS_.blit(txt1,(0,0))
                        DIS_.blit(txt2,(0,50))
                        DIS_.blit(txt3,(0,100))
                        DIS_.blit(txt4,(0,150))
                        DIS_.blit(txt5,(0,200))
                        DIS_.blit(txt6,(0,100))
                        DIS_.blit(txt7,(0,150))
                        DIS_.blit(txt8,(0,200))
                        DIS_.blit(TXT,(0,400))
                        Txt = font.render('', True, (100,100,100))
                        DIS_.blit(TXT,(0,400))
                        DIS_.blit(Txt, (30, 450))
                        pygame.display.update()
        if movie == 7:
            center()
        elif movie <7:
            a = o
            b = a[movie-1]
            try:
                global mov
            except:
                pass
            mov = b
            ticket()
        else:
            DIS_.blit(c,(0,-100))
            txt = font.render("wrong choice",True,(255,255,255))
            DIS_.blit(txt,(0,0))
            pygame.display.update()
            txt2 = font.render("back (Y/N)",True,(255,255,255))
            DIS_.blit(txt2,(0,50))
            pygame.display.update()
            TypTxt = ''
            s = ''
            p = True
            while p:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        p = False
                        break
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            s = TypTxt
                            p = False
                        elif event.unicode.isalpha() and len(TypTxt) < 1:
                            TypTxt = event.unicode
                            DIS_.blit(c,(0,-100))
                            DIS_.blit(txt,(0,0))
                            DIS_.blit(txt2,(0,50))
                            DIS_.blit(TXT,(0,400))
                            Txt = font.render(TypTxt, True, (100, 100, 100))
                            DIS_.blit(Txt, (30, 450))
                            pygame.display.update()
                        elif event.key == pygame.K_BACKSPACE:
                            TypTxt = ''
                            DIS_.blit(c,(0,-100))
                            DIS_.blit(txt1,(0,0))
                            DIS_.blit(txt2,(0,50))
                            DIS_.blit(TXT,(0,400))
                            Txt = font.render('', True, (100,100,100))
                            DIS_.blit(TXT,(0,400))
                            DIS_.blit(Txt, (30, 450))
                            pygame.display.update()
            if s.lower() == 'y':
                t_movie()
            else:
                pygame.quit()
    def food():
        fc1 = open('image.dat','rb')
        fz = pickle.load(fc1)
        fz = base64.b64decode(fz)
        fz = BytesIO(fz)
        fz = pygame.image.load(fz)
        global price_1
        price_1 = 0
        counter1 = 0
        counter2 = 0
        counter3 = 0
        counter4 = 0
        r = True
        while r:
            DIS_.blit(c,(0,-100))
            txt1 = font.render(f"1)Popcorn 100         x {counter1}",True,(255,255,255))
            DIS_.blit(txt1,(0,0))
            pygame.display.update()
            txt2 = font.render(f"2)Puffs 100              x {counter2}",True,(255,255,255))
            DIS_.blit(txt2,(0,50))
            pygame.display.update()
            txt3 = font.render(f"3)Soft drinks 100     x {counter3}",True,(255,255,255))
            DIS_.blit(txt3,(0,100))
            pygame.display.update()
            txt4 = font.render(f"4)French Fries 100  x {counter4}",True,(255,255,255))
            DIS_.blit(txt4,(0,150))
            pygame.display.update()
            txt5 = font.render(f"5)Back",True,(255,255,255))
            DIS_.blit(txt5,(0,200))
            pygame.display.update()
            txt6 = font.render(f"FOOD PRICE          = {price_1 }",True,(255,255,255))
            DIS_.blit(txt6,(0,300))
            pygame.display.update()
            TXT = font.render("choose your option:",True,(255,255,255))
            DIS_.blit(TXT,(0,400))
            DIS_.blit(fz,(700,300))
            pygame.display.update()
            x = 0
            TypTxt = 0
            p = True
            while p:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        p = False
                        break
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x,y =  pygame.mouse.get_pos()
                        if 700<= x <= 900 and 300 <= y <= 450:
                            x = 6
                            p = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            x = TypTxt
                            p = False
                        elif event.unicode.isdigit() and TypTxt < 9:
                            print(event.unicode)
                            TypTxt = int(event.unicode)
                            DIS_.blit(c,(0,-100))
                            DIS_.blit(txt1,(0,0))
                            DIS_.blit(txt2,(0,50))
                            DIS_.blit(txt3,(0,100))
                            DIS_.blit(txt4,(0,150))
                            DIS_.blit(txt5,(0,200))
                            DIS_.blit(txt6,(0,300))
                            DIS_.blit(TXT,(0,400))
                            DIS_.blit(fz,(700,300))
                            Txt = font.render(f'{TypTxt}', True, (100, 100, 100))
                            DIS_.blit(Txt, (30, 450))
                            pygame.display.update()
                        elif event.key == pygame.K_BACKSPACE:
                            TypTxt = 0
                            DIS_.blit(c,(0,-100))
                            DIS_.blit(txt1,(0,0))
                            DIS_.blit(txt2,(0,50))
                            DIS_.blit(txt3,(0,100))
                            DIS_.blit(txt4,(0,150))
                            DIS_.blit(txt5,(0,200))
                            DIS_.blit(txt6,(0,300))
                            DIS_.blit(TXT,(0,400))
                            DIS_.blit(fz,(700,300))
                            Txt = font.render('', True, (100,100,100))
                            DIS_.blit(TXT,(0,400))
                            DIS_.blit(Txt, (30, 450))
                            pygame.display.update()
            if x == 1:
                counter1 += 1
                price_1 += 100
            elif x == 2:
                counter2 += 1
                price_1 += 100
            elif x == 3:
                counter3 += 1
                price_1 += 100
            elif x == 4:
                counter4 += 1
                price_1 += 100
            elif x == 5:
                theater()
            elif x == 6:
                DIS_.blit(c,(0,-100))
                pygame.display.update()
                txt1 = font.render(f"TOTAL MONEY FOR FOOD = {price_1}",True,(255,255,255))
                print(price_1)
                DIS_.blit(txt1,(0,0))
                pygame.display.update()
                txt2 = font.render("press ENTER to continue",True,(255,255,255))
                DIS_.blit(txt2,(0,50))
                pygame.display.update()
                p = True
                while p:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            break
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                detail1()   
                                global food_price
                                food_price=price_1
    def detail1():
        DIS_.blit(c,(0,-100))
        pygame.display.update()
        txt1 = font.render(" Enter your phone number ",True,(255,255,255))
        DIS_.blit(txt1,(0,0))
        pygame.display.update()
        TypTxt = 0
        p = True
        while p:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    p = False
                    return 0
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and 999999999 < TypTxt < 10000000000:
                        try:
                            global phon
                        except:
                            pass
                        phon = TypTxt
                        print(phon)
                        timing()
                        return phon
                    elif event.unicode.isdigit() and TypTxt <= 1000000000:
                        TypTxt = (TypTxt * 10) + int(event.unicode)
                        DIS_.blit(c,(0,-100))
                        DIS_.blit(txt1,(0,0))
                        Txt = font.render(f'{TypTxt}', True, (100, 100, 100))
                        DIS_.blit(Txt, (30, 450))
                        pygame.display.update()
                    elif event.key == pygame.K_BACKSPACE:
                        TypTxt = TypTxt//10
                        DIS_.blit(c,(0,-100))
                        DIS_.blit(txt1,(0,0))
                        Txt = font.render(f'{TypTxt}', True, (100,100,100))
                        DIS_.blit(Txt, (30, 450))
                        pygame.display.update()
    def ticket():
        DIS_.blit(c,(0,-100))
        import mysql.connector as sql
        con = sql.connect(host = "localhost" , user = "root" , password = "123", database = "_Cinema_")
        if con.is_connected:
            cur = con.cursor()
            cur.execute("select * from tickets;")
            p = cur.fetchall()
            con.commit()
        b = p[0][0]
        yt = b
        w = True
        while w:
            TXT = font.render("Number of ticket(s) in need: ",True,(255,255,255))
            DIS_.blit(TXT,(0,400))
            pygame.display.update()
            TypTxt = 0
            p = True
            q = 0
            while p:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        p = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            global tkt
                            tkt = TypTxt
                            p = False
                        elif event.unicode.isdigit() and q != 3:
                            q += 1
                            TypTxt = (TypTxt * 10) + int(event.unicode)
                            DIS_.blit(c,(0,-100))
                            DIS_.blit(TXT,(0,400))
                            Txt = font.render(f'{TypTxt}', True, (100, 100, 100))
                            DIS_.blit(Txt, (30, 450))
                            pygame.display.update()
                        elif event.key == pygame.K_BACKSPACE:
                            q -= 1
                            if TypTxt > 9:
                                TypTxt = int(str(TypTxt)[:-1])
                            else:
                                TypTxt = 0
                            print(TypTxt)
                            DIS_.blit(c,(0,-100))
                            DIS_.blit(TXT,(0,400))
                            Txt = font.render(f'{TypTxt}', True, (100,100,100))
                            DIS_.blit(TXT,(0,400))
                            DIS_.blit(Txt, (30, 450))
                            pygame.display.update()
            if tkt > b:
                DIS_.blit(c,(0,-100))
                txt = font.render(f"Error:Enough tickets not available, tickets available = {b}",True,(255,255,255))
                DIS_.blit(txt,(0,0))
                pygame.display.update()
                DIS_.blit(c,(0,-100))
                txt = font.render("No sufficient tickets",True,(255,255,255))
                DIS_.blit(txt,(0,50))
                pygame.display.update()
                txt2 = font.render("back (Y/N)",True,(255,255,255))
                DIS_.blit(txt2,(0,100))
                pygame.display.update()
                TypTxt = ''
                s = ''
                p = True
                while p:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            p = False
                            break
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                s = TypTxt
                                p = False
                            elif event.unicode.isalpha() and len(TypTxt) < 1:
                                TypTxt = event.unicode
                                DIS_.blit(c,(0,-100))
                                DIS_.blit(txt,(0,50))
                                DIS_.blit(txt2,(0,100))
                                DIS_.blit(TXT,(0,400))
                                Txt = font.render(TypTxt, True, (100, 100, 100))
                                DIS_.blit(Txt, (30, 450))
                                pygame.display.update()
                            elif event.key == pygame.K_BACKSPACE:
                                TypTxt = ''
                                DIS_.blit(c,(0,-100))
                                DIS_.blit(txt,(0,50))
                                DIS_.blit(txt2,(0,100))
                                DIS_.blit(TXT,(0,400))
                                Txt = font.render('', True, (100,100,100))
                                DIS_.blit(TXT,(0,400))
                                DIS_.blit(Txt, (30,450))
                                pygame.display.update()
                if s.lower() == 'y':
                    ticket()
                else:
                    pygame.quit()
                    break
            else:
                DIS_.blit(c,(0,-100))
                b = b - tkt
                cur.execute(f"UPDATE Tickets SET No_of_Tickets = {b} WHERE No_of_Tickets = '{yt}';")
                con.commit()
                print(b)
                global price
                price = tkt * 200
                txt = font.render(f"Ticket(s) confirmed total price =  {price}",True,(255,255,255))
                DIS_.blit(txt,(0,0))
                print(price)
                txt = font.render("press 'Enter' to continue",True,(255,255,255))
                DIS_.blit(txt,(0,50))
                pygame.display.update()
                t = True
                while t:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                t = False
                global ticket_price
                ticket_price=price
            w = False
            food()    
    def timing():
         print("TIME")
         time1 = {
              "1": ["5:30:00","am"],
              "2": ["10:00:00","am"],
              "3": ["1:10:00","pm"],
              "4": ["4:20:00","pm"],
              "5": ["7:30:00","pm"],
              "6": ["11:40:00","pm"]
         }
         global phon
         global mov
         global tkt
         global tme
         DIS_.blit(c,(0,-100))
         pygame.display.update()
         txt1 = font.render("choose your time:",True,(255,255,255))
         DIS_.blit(txt1,(0,0))
         pygame.display.update()
         for i in time1:
           j = int(i)
           txt = font.render(f'{j}) {time1[i][0]}'   f'{time1[i][1]}',True,(255,255,255)) 
           DIS_.blit(txt,(0,(j)*50))
           pygame.display.update()
         TXT = font.render("choose your option:",True,(255,255,255))
         TypTxt = 0
         p = True
         while p:
           for event in pygame.event.get():
              if event.type == pygame.QUIT:
                   p = False
                   break
              if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_RETURN:
                       t = TypTxt
                       p = False
                   elif event.unicode.isdigit() and TypTxt < 6:
                       print(event.unicode)
                       TypTxt = int(event.unicode)
                       DIS_.blit(c,(0,-100))
                       DIS_.blit(txt1,(0,0))
                       for i in time1:
                           j = int(i)
                           txt = font.render(f'{j}) {time1[i][0]}'   f'{time1[i][1]}',True,(255,255,255)) 
                           DIS_.blit(txt,(0,(j)*50))
                           pygame.display.update()
                       DIS_.blit(TXT,(0,400))
                       Txt = font.render(f'{TypTxt}', True, (100, 100, 100))
                       DIS_.blit(Txt, (30, 450))
                       pygame.display.update()
                   elif event.key == pygame.K_BACKSPACE:
                       TypTxt = 0
                       DIS_.blit(c,(0,-100))
                       DIS_.blit(txt1,(0,0))
                       DIS_.blit(txt2,(0,50))
                       DIS_.blit(TXT,(0,400))
                       Txt = font.render('', True, (100,100,100))
                       DIS_.blit(TXT,(0,400))
                       DIS_.blit(Txt, (30, 450))
                       pygame.display.update()
         tme = time1[str(t)]
         DIS_.blit(c,(0,-100))
         txt = font.render("Successfully booked!, Enjoy watching",True,(255,255,255))
         txt3 = font.render(f"{mov} in STS Cinemas",True,(255,255,255))
         txt2 = font.render(f"at {tme[0]} {tme[1]}, in Royce Screen Nandri Vanakam",True,(255,255,255))
         DIS_.blit(txt,(0,100))
         DIS_.blit(txt3,(0,140))
         DIS_.blit(txt2,(0,180))
         txt = font.render("press enter to close",True,(255,255,255))
         DIS_.blit(txt,(0,230))
         pygame.display.update()
         r = True
         while r:
           for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_RETURN:
                       r = False
                       pygame.quit()
         bill()
         save()
         import csv
         global tkt
         import os
         Y = os.path.exists('ticket.csv')
         with open('ticket.csv', mode='a+', newline='') as file:
               writer = csv.writer(file)
               if not Y:
                    writer.writerow(['Movie','Ticket','Phone_no','Timing'])
                    writer.writerow([mov,tkt,phon,tme])
               else:
                   print([mov,tkt,phon,tme])
                   writer.writerow([mov,tkt,phon,tme])
    def save():
        import mysql.connector as sql
        con = sql.connect(host = "localhost" , user = "root" , password = "123", database = "_Cinema_")
        if con.is_connected:
            cur = con.cursor()
            cur.execute("CREATE TABLE if not exists Cinema (Movie text,Ticket int,Phone_no varchar(10));")
            sql = "INSERT INTO Cinema (Movie,Ticket,Phone_no) VALUES ('%s', %s, '%s')"
            values = (mov,tkt,phon)
            print(values)
            cur.execute(sql%values)
            con.commit()
    def movie(theater):
        if theater == 1:
            t_movie()
        elif theater == 2:
            t_movie()
        elif theater == 3:
            t_movie()
        elif theater == 4:
            t_movie()
        elif theater == 5:
            city()
        else:
            DIS_.fill((0,0,0))
            txt = font.render("wrong choice",True,(255,255,255))
            DIS_.blit(txt,(0,0))
            pygame.display.update()
    def center():
        DIS_.blit(c,(0,-100))
        txt1 = font.render("Which theater do you wish to see movie? ",True,(255,255,255))
        DIS_.blit(txt1,(0,0))
        pygame.display.update()
        txt2 = font.render("1) Inox",True,(255,255,255))
        DIS_.blit(txt2,(0,50))
        pygame.display.update()
        txt3 = font.render("2) Imax",True,(255,255,255))
        DIS_.blit(txt3,(0,100))
        pygame.display.update()
        txt4 = font.render("3) Pvr",True,(255,255,255))
        DIS_.blit(txt4,(0,150))
        pygame.display.update()
        txt5 = font.render("4) back",True,(255,255,255))
        DIS_.blit(txt5,(0,200))
        pygame.display.update()
        TXT = font.render("choose your option:",True,(255,255,255))
        TypTxt = 0
        p = True
        while p:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    p = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        a = TypTxt
                        p = False
                    elif event.unicode.isdigit() and TypTxt < 5:
                        print(event.unicode)
                        TypTxt = int(event.unicode)
                        DIS_.blit(c,(0,-100))
                        DIS_.blit(txt1,(0,0))
                        DIS_.blit(txt2,(0,50))
                        DIS_.blit(txt3,(0,100))
                        DIS_.blit(txt4,(0,150))
                        DIS_.blit(txt5,(0,200))
                        DIS_.blit(TXT,(0,400))
                        Txt = font.render(f'{TypTxt}', True, (100, 100, 100))
                        DIS_.blit(Txt, (30, 450))
                        pygame.display.update()
                    elif event.key == pygame.K_BACKSPACE:
                        TypTxt = 0
                        DIS_.blit(c,(0,-100))
                        DIS_.blit(txt1,(0,0))
                        DIS_.blit(txt2,(0,50))
                        DIS_.blit(txt3,(0,100))
                        DIS_.blit(txt4,(0,150))
                        DIS_.blit(txt5,(0,200))
                        DIS_.blit(TXT,(0,400))
                        Txt = font.render('', True, (100,100,100))
                        DIS_.blit(TXT,(0,400))
                        DIS_.blit(Txt, (30, 450))
                        pygame.display.update()
        if a == 4:
            city()
        elif a < 4:
            movie(a)
        else:
            DIS_.blit(c,(0,-100))
            txt = font.render("wrong choice",True,(255,255,255))
            DIS_.blit(txt,(0,0))
            pygame.display.update()
            txt2 = font.render("back (Y/N)",True,(255,255,255))
            DIS_.blit(txt2,(0,50))
            pygame.display.update()
            TypTxt = ''
            s = ''
            p = True
            while p:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        p = False
                        break
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            s = TypTxt
                            p = False
                        elif event.unicode.isalpha() and len(TypTxt) < 1:
                            TypTxt = event.unicode
                            DIS_.blit(c,(0,-100))
                            DIS_.blit(txt,(0,0))
                            DIS_.blit(txt2,(0,50))
                            DIS_.blit(TXT,(0,400))
                            Txt = font.render(TypTxt, True, (100, 100, 100))
                            DIS_.blit(Txt, (30, 450))
                            pygame.display.update()
                        elif event.key == pygame.K_BACKSPACE:
                            TypTxt = ''
                            DIS_.blit(c,(0,-100))
                            DIS_.blit(txt1,(0,0))
                            DIS_.blit(txt2,(0,50))
                            DIS_.blit(TXT,(0,400))
                            Txt = font.render('', True, (100,100,100))
                            DIS_.blit(TXT,(0,400))
                            DIS_.blit(Txt, (30, 450))
                            pygame.display.update()
            if s.lower() == 'y':
                t_movie()
            else:
                pygame.quit()
        return 0
    def city():
        adm=open("Adm.dat","rb")
        u2=pickle.load(adm)
        u2 = base64.b64decode(u2)
        u2 = BytesIO(u2)
        u2 = pygame.image.load(u2)
        DIS_ = pygame.display.set_mode((1020,500))
        DIS_.blit(c,(0,-100))
        DIS_.blit(u2,(800,10))
        pygame.display.update()
        txt1 = font.render("Hi welcome to STS cinema ticket booking: ",True,(255,255,255))
        DIS_.blit(txt1,(0,0))
        txt2 = font.render("Where you want to watch movie?:",True,(255,255,255))
        DIS_.blit(txt2,(0,50))
        txt3 = font.render("1,Adyar",True,(255,255,255))
        DIS_.blit(txt3,(0,100))
        txt4 = font.render("2,Koyambedu",True,(255,255,255))
        DIS_.blit(txt4,(0,150))
        txt5 = font.render("3,Nungumbakkam",True,(255,255,255))
        DIS_.blit(txt5,(0,200))
        pygame.display.update()
        TXT = font.render("choose your option:",True,(255,255,255))
        DIS_.blit(TXT,(0,400))
        pygame.display.update()
        place = ''
        TypTxt = 0
        p = True
        while p:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    p = False
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        place = TypTxt
                        p = False
                    elif event.unicode.isdigit() and TypTxt < 5:
                        print(event.unicode)
                        TypTxt = int(event.unicode)
                        DIS_.blit(c,(0,-100))
                        DIS_.blit(txt1,(0,0))
                        DIS_.blit(txt2,(0,50))
                        DIS_.blit(txt3,(0,100))
                        DIS_.blit(txt4,(0,150))
                        DIS_.blit(txt5,(0,200))
                        DIS_.blit(TXT,(0,400))
                        Txt = font.render(f'{TypTxt}', True, (100, 100, 100))
                        DIS_.blit(Txt, (30, 450))
                        pygame.display.update()
                    elif event.key == pygame.K_BACKSPACE:
                        TypTxt = 0
                        DIS_.blit(c,(0,-100))
                        DIS_.blit(txt1,(0,0))
                        DIS_.blit(txt2,(0,50))
                        DIS_.blit(txt3,(0,100))
                        DIS_.blit(txt4,(0,150))
                        DIS_.blit(txt5,(0,200))
                        DIS_.blit(TXT,(0,400))
                        Txt = font.render('', True, (100,100,100))
                        DIS_.blit(TXT,(0,400))
                        DIS_.blit(Txt, (30, 450))
                        pygame.display.update()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x,y =  pygame.mouse.get_pos()
                    if 800<= x <= 900 and 10 <= y <= 74:
                        p = False
                        login()
        if place == 1:
          center()
        elif place == 2:
          center()
        elif place == 3:
          center()
        else:
            DIS_.blit(c,(0,-100))
            txt = font.render("wrong choice",True,(255,255,255))
            DIS_.blit(txt,(0,0))
            pygame.display.update()
            txt2 = font.render("back (Y/N)",True,(255,255,255))
            DIS_.blit(txt2,(0,50))
            pygame.display.update()
            TypTxt = ''
            s = ''
            p = True
            while p:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        p = False
                        break
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            s = TypTxt
                            p = False
                        elif event.unicode.isalpha() and len(TypTxt) < 1:
                            TypTxt = event.unicode
                            DIS_.blit(c,(0,-100))
                            DIS_.blit(txt,(0,0))
                            DIS_.blit(txt2,(0,50))
                            DIS_.blit(TXT,(0,400))
                            Txt = font.render(TypTxt, True, (100, 100, 100))
                            DIS_.blit(Txt, (30, 450))
                            pygame.display.update()
                        elif event.key == pygame.K_BACKSPACE:
                            TypTxt = ''
                            DIS_.blit(c,(0,-100))
                            DIS_.blit(txt1,(0,0))
                            DIS_.blit(txt2,(0,50))
                            DIS_.blit(TXT,(0,400))
                            Txt = font.render('', True, (100,100,100))
                            DIS_.blit(TXT,(0,400))
                            DIS_.blit(Txt, (30, 450))
                            pygame.display.update()
            if s.lower() == 'y':
                city()
            else:
                pygame.quit()
    city()
except:
    pass
