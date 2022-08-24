import random
O = 0  #당첨횟수, 실패횟수 0으로 설정
X = 0

def calc(count):

    global O
    global X

    success = random.randint(1,count) #success: 당첨 번호
    select = random.randint(1,count) #select: 선택한 번호
    nlist = [] #nlist: 선택지 목록
    remain = []
    for i in range(1, count+1):
        nlist.append(i)
        remain.append(i)
    
    if success == select:
        nlist.remove(success)
        notselected = random.choice(nlist) #notselected: 당첨, 선택이 아닌 번호
    else:
        nlist.remove(success)
        nlist.remove(select)
        notselected = random.choice(nlist) #notselected: 당첨, 선택이 아닌 번호
        
    remain.remove(notselected)
    remain.remove(select) #remain: 선택하지 않은 번호들
    result = random.choice(remain) #result: 선택하지 않은 번호중 당첨이 아닌 것을 제외한 것 중 하나
    
    if result == success:
        O += 1
        print("당첨숫자: ", success, "  선택: ", select, "  결과: O  |  시도 횟수: ", O+X, "  당첨확률: ", round(100*(O/(O+X)),3),"%")
    else:
        X += 1
        print("당첨숫자: ", success, "  선택: ", select, "  결과: X  |  시도 횟수: ", O+X, "  당첨확률: ", round(100*(O/(O+X)),3),"%")

        
def repeat(repeat, listcount):

    for i in range(repeat):
        calc(listcount)
    global O
    global X
    print(f"당첨: {O} | 실패: {X}")
    print("당첨확률:" , round(100*(O/(O+X)),3),"%")

    O = 0
    X = 0 #결과 초기화

while True:
    runcount = int(input("\n실행할 횟수를 설정해 주십시오. : "))
    listcount = int(input("\n선택지의 수를 설정해 주십시오. : "))
    if listcount >= 3:
        repeat(runcount,listcount) 
    else:
        print("\n선택지의 수는 최소 3개입니다.")