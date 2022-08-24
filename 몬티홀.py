import random
O = 0
X = 0

def calc():
    a = random.randint(1,3) #a: 당첨 번호
    b = random.randint(1,3) #b: 선택한 번호
    c = [1,2,3] #c: 1, 2, 3
    
    if a == b:
        c.remove(a)
        d = random.choice(c) #d: 당첨, 선택이 아닌 번호
    else:
        c.remove(a)
        c.remove(b)
        d = random.choice(c) #d: 당첨, 선택이 아닌 번호
        
    # e = [1,2,3]
    # e.remove(d)
    # e.remove(b)
    # e = int(str(e)[1]) #e: 선택하지 않은 두 번호중 당첨이 아닌 것을 제외한 나머지 하나
    
    if d == a:
        global O
        O += 1
    else:
        global X
        X += 1
        
def repeat(repeat):
    for i in range(0,repeat):
        calc()
    global O
    global X
    print(f"성공: {O} | 실패: {X}")
    print("성공확률:" , round(100*(O/(O+X)),3),"%")

while True:
    count = int(input("\n실행할 횟수를 설정해 주십시오. : "))
    repeat(count)
