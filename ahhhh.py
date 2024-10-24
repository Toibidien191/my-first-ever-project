import time
import random
import os

def nhetbitcoin():
    global bal, bitcointrgbank
    try:
        monicannhet = int(input(f"bao nhiêu? (bạn đang có {bal}) "))
        if monicannhet > bal:
            print("ngu à?")
            return 0
        elif monicannhet <= 0:
            print("ngu à?")
            return 0
        else:
            bal -= monicannhet
            bitcointrgbank += monicannhet
            print(f"Bạn đã nạp {monicannhet} vào ngân hàng Bitcoin.")
    except ValueError:
        print("Vui lòng nhập một số hợp lệ.")

def rutbitcoin():
    global bal, bitcointrgbank
    try:
        monicanrut = int(input(f"bao nhiêu? (bạn đang có {bitcointrgbank} trong ngân hàng) "))
        if monicanrut > bitcointrgbank:
            print("ngu à?")
            return 0
        elif monicanrut <= 0:
            print("ngu à?")
            return 0
        else:
            bitcointrgbank -= monicanrut
            bal += monicanrut
            print(f"Bạn đã rút {monicanrut} từ ngân hàng Bitcoin.")
    except ValueError:
        print("Vui lòng nhập một số hợp lệ.")

def checkbitcoin():
    print(f"Bạn có {bal} Bitcoin và {bitcointrgbank} trong ngân hàng.")

def choicobac():
    global bitcointrgbank
    try:
        tiencuoc = int(input(f"chọn số tiền mà bạn muốn cược (bạn đang có {bitcointrgbank}): "))
        if tiencuoc > bitcointrgbank or tiencuoc <= 0:
            print("bị ngu à?")
            return
        
        luckynum = int(input("chọn số yêu thích của bạn (1-6): "))
        if luckynum < 1 or luckynum > 6:
            print("số ko hợp lệ:/")
            return
        
        print("Đang quay số...")
        time.sleep(2)
        
        batngochua = random.randint(1, 6)
        print(f"Kết quả là: {batngochua}")
        
        if luckynum == batngochua:
            print("Chúc mừng! Bạn đã thắng!")
            bitcointrgbank += tiencuoc
        else:
            print("Rất tiếc, bạn đã thua.")
            bitcointrgbank -= tiencuoc
        
        print(f"Bạn hiện có {bitcointrgbank} trong ngân hàng.")
    except ValueError:
        print("Vui lòng nhập một số hợp lệ.")

bal = 1000
bitcointrgbank = 0
dangnghien = True

while dangnghien:
    print("xin chào thằng nghiện, mày lại cá độ à:v")
    print("1. chơi game")
    print("2. check moni")
    print("3. cho tao moni")
    print("4. rút bitcoin")
    print("5. cút")
    cacbe = input("chọn đi thg ngu: ")
    if cacbe == "1":
        choicobac()
    elif cacbe == "2":
        checkbitcoin()
    elif cacbe == "3":
        nhetbitcoin()
    elif cacbe == "4":
        rutbitcoin()
    elif cacbe == "5":
        dangnghien = False
    else:
        print("Lựa chọn không hợp lệ.")
