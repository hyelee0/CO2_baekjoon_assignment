import sys
input = sys.stdin.readline


#===============================================================================================================


"""  11399번 - ATM
; N은 사람의 수 , Pi는 i번째 사람의 인출 시간(분) -> N = 5, P1 = 3, 총 5명 중 첫번째 사람이 인출하는 데 걸리는 시간 3분
; 앞 사람이 인출중 뒷 사람은 대기 -> 뒷 사람이 걸리는 시간은 사실상 Pi + Pi-1 + ... + P1
N = 3, P1 = 3, P2 = 1, P3 = 4 -> 3번째 사람의 실질적인 인출 시간 = 4 + 1 + 3 = 8
; 목표는 그래서 모든 사람이 인출하려면 총 몇분이 걸리는지, 걸리는 시간의 최솟값은?
앞 사람의 인출 시간↓ 뒷 사람의 대기 시간↓ 시간의 총합↓
인출 시간들을 오름차순으로 정렬 -> 그 순서대로 서서 인출하면 최소로 걸림 -> 각 사람당 실질적인 인출 시간을 구함 -> 모두 더해서 출력  """

def _11399():
    N = int(input()) # 첫째줄: 줄 서있는 사람의 수
    time = list(map(int, input().split())) # 둘째줄: 한 사람당 돈을 인출하는 데 걸리는 시간
    time.sort() # 오름차순으로 정렬
    
    actual_time = 0 # 한 사람당 실질적으로 걸리는 시간 (인출 시간 + 대기 시간)
    total_time = 0 # 출력: 걸리는 시간의 총합
    
    for i in range(N):
        actual_time += time[i]
        total_time += actual_time
    
    print(total_time)

    
#===============================================================================================================


""" 11047번 - 동전 0
; N은 갖고있는 동전의 종류 (각각의 동전은 多), K는 만들려는 총액
Ai는 각 동전의 금액 (1 5 10 50 100 500 1000 5000 ... 의 규칙으로 주어짐)
; 목표는 총액을 만들기 위해 몇개의 동전이 필요한지, 그 개수의 최솟값은?
각 동전을 중복 사용 O -> 1000원 만들고자 1원짜리 1000개 사용 O (물론 최솟값은 아님)
금액은 오름차순으로 주어짐 -> K보다 작으면서 가장 큰 값을 찾음 (같은 금액 있으면 그 동전 하나로 끝임)
K//찾은 값 -> 이만큼 동전이 필요 / K%찾은 값 -> 이걸로 K를 갱신  """

def _11047():
    N, K = map(int, input().split()) # 첫째줄: 갖고있는 동전의 종류, 만들려는 총액
    wallet = [int(input()) for _ in range(N)] # 둘째줄부터: 각 동전의 금액

    cnt_coin = 0 # 출력: 필요한 동전의 개수

    i = N - 1 # K보다 작으면서 가장 큰 값을 찾음 -> 그래서 맨뒤의 금액부터 비교
    while True:
        if wallet[i] <= K:
            cnt_coin += K // wallet[i] # 동전의 개수를 증가
            K = K % wallet[i] # 남은 금액을 계산
            if K == 0: break # 남은 금액이 0원이 되면 완료
        i -= 1
    
    print(cnt_coin)


#===============================================================================================================


"""  1541번 - 잃어버린 괄호
; 주어지는 식에서 피연산자는 양수만 -> 0~9로 표현, 0으로 시작 O, 5자리 이하
주어지는 식에서 연산자는 +, -만 -> 연속해서 등장 X, 첫번째와 마지막 자리에 X
주어지는 식의 길이는 50 이하
; 목표는 여기서 적절한 괄호를 쳐서 식의 최솟값을 구하는 것, 어떻게?
가장 많이 더해서 빼주면 됨 -> 부호만 봤을 때 - + 가 보이면 + 양옆을 묶음
10 + 10 - 10 + 10 - 10 - 10 + 10 - 10 -> 10 + 10 - (10 + 10) - 10 - (10 + 10) - 10  """

def _1541():
    # split 함수의 반환값은 리스트
    first_split = input().split('-') # 먼저 -를 기준으로 자름 -> 현재 ['10+10', '10+10', '10', '10+10', '10\n']
    second_split = [] # 그 다음 +를 기준으로 자름 -> 아래 for문이 끝나면 [20, 20, 10, 20, 10]
    min = 0 # 출력: 만들 수 있는 최솟값

    first_split[-1] = first_split[-1][:-1] # input 함수의 특성 상 마지막 요소에 \n가 붙음
    
    for first in first_split:        
        second = first.split('+')
        buf = 0        
        for s in second: 
            buf += int(s) # + 양옆의 양수들을 더해줌
        second_split.append(buf)
    
    min = second_split[0]
    for i in range(1, len(second_split)):
        min = min - second_split[i] # - 뒤에서 더해준 값들을 빼줌

    print(min)
    

#===============================================================================================================


"""  2210번 - 숫자판 점프
; 5x5 숫자판, 각각의 칸은 0~9의 숫자 -> 어떤 칸에서 시작해서 상하좌우로 5번 이동, 재방문 가능
-> 그렇게 거쳐간 총 6개의 숫자를 이어붙여서 어떤 수를 만듦 -> 만들 수 있는 서로 다른 수의 개수는?
; 첫줄부터 바로 5행 5열의 숫자판을 구성 (0~9의 숫자 총 25개를 입력) -> 구한 개수를 출력
; 숫자판의 구현 = 5개의 숫자를 하나의 리스트에 저장, 그런 행이 5개가 있는 이차원 리스트
25개의 칸에 좌표를 부여하면 왼쪽 위 (0, 0) 오른쪽 아래 (4, 4) -> 상하좌우로의 이동을 나타내보면 (-1, 0) (+1, 0) (0, -1) (0, +1)
; 수 만들기 = 총 25개의 모든 좌표에 대해 DFS를 진행 -> 그렇게 만든 수들을 중복없이 기록 -> 개수를 출력  """
    
def _2210():
    board_5x5 = [list(map(str, input().split())) for _ in range(5)] # 숫자판의 구현 -> 0~9의 int는 모두 str으로 다룸 (+로 이어붙이기 쉽게)
    number_list = set() # 중복된 수를 제거하기 위함
    
    def DFS(cur_x, cur_y, cur_num): # 현재 x좌표, 현재 y좌표, 현재 이어붙인 수
        if len(cur_num) == 6: # 길이 6의 문자열이 됐으면 추가시키고 종료
            number_list.add(cur_num)
            return

        # 상하좌우로의 이동을 위한 정보
        move_x = [-1, 1, 0, 0] 
        move_y = [0, 0, -1, 1]
        
        for i in range(4): # 상하좌우로 이동해서 다음 좌표를 설정
            next_x = cur_x + move_x[i]
            next_y = cur_y + move_y[i]
            
            if (0 <= next_x <= 4) and (0<= next_y <= 4): # 좌표는 최소 (0, 0) 최대 (4, 4)
                DFS(next_x, next_y, cur_num + board_5x5[next_x][next_y]) # 길이 6의 문자열이 될 때까지 반복
    
    # 총 25개의 모든 좌표에 대해 검사
    for cur_x in range(5): 
        for cur_y in range(5):
            DFS(cur_x, cur_y, board_5x5[cur_x][cur_y])
    
    print(len(number_list))


#===============================================================================================================


##### 실패 - 161줄 Name Error.....(?)
"""  3187번 - 양치기 꿍
; RxC 목장, 빈 공간은 ., 울타리는 #, 양은 k, 늑대는 v
양과 늑대는 대각선으로 이동 X, 울타리로 나뉜 각각의 공간에서 k > v 양들만 살아남음 (k <= v 늑대만 살아남음) -> 양과 늑대 각각 몇 마리 살아남음?
; 첫줄에 R과 C를 입력, 둘째줄부터 바로 R행 C열의 목장을 구성 (총 RxC개의 문자를 입력) -> 구한 마리 수를 출력
; 목장의 구현 = C개의 문자를 하나의 리스트에 저장, 그런 행이 R개가 있는 이차원 리스트
RxC개의 칸에 좌표를 부여하면 왼쪽 위 (0, 0) 오른쪽 아래 (R-1, C-1) -> 상하좌우로의 이동을 나타내보면 (-1, 0) (+1, 0) (0, -1) (0, +1)  """    

def _3187():
    R, C = map(int, input().split())

    ranch = [list(input().strip()) for _ in range(R)] # 목장의 구현 -> 행의 개수만큼 반복하면서 열의 개수만큼 문자를 입력
    check = [[0] * C for _ in range(R)] # 방문한 좌표는 1로 갱신
    total_sheep, total_wolf = 0, 0 # 각각 몇 마리 살아남았는지 -> 얘네를 출력하면 완료
    part_sheep, part_wolf = 0, 0 # 한번의 탐색에서, 즉 #으로 나뉘어진 영역 중 한곳에서의 양과 늑대의 마리 수

    def DFS(cur_x, cur_y):
        global part_sheep
        global part_wolf
        
        check[cur_x][cur_y] = 1 # 방문했으니 갱신

        # 양과 늑대가 있으면 기록
        if ranch[cur_x][cur_y] == 'k':
            part_sheep += 1
        elif ranch[cur_x][cur_y] == 'v':
            part_wolf += 1
        
        # 상하좌우로의 이동을 위한 정보
        move_x = [-1, 1, 0, 0] 
        move_y = [0, 0, -1, 1]
        
        for i in range(4): # 상하좌우로 이동해서 다음 좌표를 설정
            next_x = cur_x + move_x[i]
            next_y = cur_y + move_y[i]
            
            if (0 <= next_x <= R-1) and (0<= next_y <= C-1): # 좌표는 최소 (0, 0) 최대 (R-1, C-1)
                if (ranch[next_x][next_y] != '#') and (check[next_x][next_y] == 0): # 이동한 좌표 역시 양이나 늑대가 있으면서 방문한 적이 없으면
                    DFS(next_x, next_y) # 조건을 만족하는 동안은 계속해서 탐색

    # 총 RxC개의 모든 좌표에 대해 검사
    for cur_x in range(R):
        for cur_y in range(C):
            if ranch[cur_x][cur_y] != '#': 
                if check[cur_x][cur_y] == 0: # 양이나 늑대가 있으면서 방문한 적이 없으면
                    part_sheep, part_wolf = 0, 0
                    DFS(cur_x, cur_y) # 그 영역에 각각 몇 마리가 있는지 탐색
                    if part_sheep > part_wolf: part_wolf = 0 # 양이 더 많으면 늑대가 모두 사라짐
                    elif part_sheep <= part_wolf: part_sheep = 0 # 그렇지 않으면 양이 모두 사라짐
                    total_sheep += part_sheep
                    total_wolf += part_wolf
                
    print(total_sheep, total_wolf)


#===============================================================================================================


"""  14248번 - 점프 점프
; N은 돌의 개수, S는 점프 시작하는 돌의 번호 (맨 왼쪽이 1번), 점프는 왼쪽 또는 오른쪽
Ai는 돌에 적혀있는 숫자 (중복 O) -> 한번에 점프 가능한 거리 (돌다리 밖으로 나감 X)
; 목표는 그렇게 점프 점프해서 방문할 수 있는 돌의 개수는? (점프 시작하는 돌도 포함 O)  
현재 위치하는 돌에서 오른쪽과 왼쪽 두 영역을 BFS로 탐색
돌에 적힌 거리만큼 점프했을 때 범위를 안 벗어나면서 방문한 적이 없으면 카운트  """

def _14248():
    N = int(input()) # 첫째줄: 돌다리에 놓여있는 돌의 개수
    distance_list = list(map(int, input().split())) # 둘째줄: 각 돌마다 점프 가능한 거리
    start_stone_num = int(input()) # 셋째줄: 점프 시작하는 돌의 번호
    
    queue = [] # BFS 탐색 시 이용할 큐
    check = [0 for _ in range(N)] # 각 돌의 방문 여부를 체크
    count = 0 # 출력: 방문 가능한 돌의 개수
    
    queue.append(start_stone_num) # 첫번째 원소를 큐에 삽입
    check[start_stone_num - 1] = 1 # 방문 처리
    count += 1 # 돌의 개수를 증가
    
    while len(queue) != 0: # 큐가 공백상태가 될 때까지 반복 
        cur_stone_num = queue.pop(0) # 큐에서 반환 후 삭제

        # 왼쪽 또는 오른쪽으로만 점프함
        next_stone_num = cur_stone_num + distance_list[cur_stone_num - 1] # 오른쪽으로 점프해서 도착하는 돌의 번호
        if (next_stone_num <= N) and (check[next_stone_num - 1] == 0): # 현재 위치하는 돌의 번호가 N 이하이면서 방문한 적이 없으면
            queue.append(next_stone_num) # 큐에 새로 삽입
            check[next_stone_num - 1] = 1 # 방문 처리
            count +=1 # 돌의 개수를 증가
            
        next_stone_num = cur_stone_num - distance_list[cur_stone_num - 1] # 왼쪽으로 점프해서 도착하는 돌의 번호
        if (1<= next_stone_num) and (check[next_stone_num - 1] == 0): # 현재 위치하는 돌의 번호가 1 이상이면서 방문한 적이 없으면
            queue.append(next_stone_num)
            check[next_stone_num - 1] = 1
            count +=1
    
    print(count)
        

#===============================================================================================================


##### 미해결
"""  14217번 - 그래프 탐색
; N은 남규나라의 도시의 개수, M은 정비 전 도로의 개수, Q는 정비할 도로의 개수
Q개의 a i j에 대해 차례대로 정비 -> a가 1이면 i j 잇는 도로를 만듬, a가 2면 i j 잇는 도로를 없앰
; 수도는 1번 도시, 각각의 도시마다 수도를 방문하기 위해 거쳐가야하는 최소 도시의 개수를, 한번의 정비가 끝났을 때마다 출력 (참고로 한번에 수도로 가면 시작 도시 하나만 카운트해서 1을 출력)
전체적으로 N개의 열(최소 도시의 개수)과 Q개의 행(도로 정비 횟수)을 갖는 데이터가 출력되게 됨
; 남규나라는 그래프로 표현 -> 이차원 리스트의 요소 하나하나가 도시를 의미 -> 그 요소 역시 일차원 리스트로 해당 도시에 연결된 다른 도시들이 저장되어 있음
; 참고로 list.pop(인덱스) ≠ list.remove(값)
"""

def _14217():
    N, M = map(int, input().split()) # 첫째줄: 남규나라의 도시의 개수, 정비 전 도로의 개수
    city_list = [[] for _ in range(N)] # 각 도시마다 연결되어 있는 또 다른 도시들
    for _ in range(M):
        city1, city2 = map(int, input().split()) # 둘째줄부터: 현재 연결되어 있는 두 도시를 입력받음 -> 예를 들어 2 4면 두번쩨 요소에 4를 추가, 네번째 요소에도 2를 추가
        city_list[city1 - 1].append(city2)
        city_list[city2 - 1].append(city1)
        
    Q = int(input()) # M+2줄: 도로를 정비하는 횟수
    for _ in range(Q):
        bool, city1, city2 = map(int, input().split()) # M+3줄부터: 정비 유무, 한 도시, 다른 도시
        if bool == 1:
            city_list[city1 - 1].append(city2)
            city_list[city2 - 1].append(city1)
        elif bool == 2:
            city_list[city1 - 1].remove(city2)
            city_list[city2 - 1].remove(city1)

        # city_list[0]은 1번 도시에 연결되어 있는 다른 도시들 (근데 오름차순)

        res = [0]
        
        for i in range(1, N):
            queue = [] # BFS 탐색 시 이용할 큐
            check = [0 for _ in range(N)] # 각 도시의 방문 여부를 체크
            count = 0
            
            queue.append(i) # 2번 도시부터 탐색 (수도가 1번 도시기 때문에 1번 도시는 탐색할 필요 X)
            check[i] = 1
        
            while len(queue) != 0:
                data = queue.pop()
                for j in city_list[data]:
                    if j == 1:
                        check[j - 1] = 1
                        count +=1
                        break
                    elif check[j - 1] == 0:
                        pass
            if check[0] == 0:
                res.append(-1)
            else:
                res.append(count)
    
        for i in range(N):
            print(res[i], end=' ')
        print()

# _14217()


#===============================================================================================================


##### 미해결
"""  15989번 - 1, 2, 3 더하기 4
; N을 1, 2, 3의 합으로 나타내는 서로 다른 방법의 수는?
총 T개의 N에 대해 가짓수를 구함, 순서만 다른 것은 같은 것으로 봄
T = 1, N = 4 -> 1+1+1+1, 1+1+2 (1+2+1, 2+1+1), 1+3 (3+1), 2+2 -> 4를 출력 
; 맨 윗줄 저거를 S(N)이라고 두자, 사용가능한 숫자는 1, 2, 3 뿐 
수식을 오름차순으로만 나타낸다면 -> 수식이 1로 끝나면 뒤에 +1만 가능, 2로 끝나면 +1, +2 가능, 3으로 끝나면 +1, +2, +3 가능
S(N)(M)을 여전히 N을 1, 2, 3의 합으로 나타내는 가짓수인데 뒤에가 M으로 끝나는 그런 수식의 가짓수라고 하자
S(N) = S(N)(1) + S(N)(2) + S(N)(3) 
; 근데 생각해보면 S(N-1) 중 1로 끝나는 수식에 +1을 하면 N이 됨 -> S(N)(1) = S(N-1)(1) = 1 (오름차순으로만 더하기로 했으니 +1 뒤에 +1만 가능 그래서 1+1+1....+1 = 1가지)
S(N-2) 중 1, 2로 끝나는 수식에 +2를 하면 N이 됨 -> S(N)(2) = 1 + S(N-2)(2)
S(N-3) 중 1, 2, 3으로 끝나는 수식에 +3을 하면 N이 됨 -> S(N)(3) = 1 + S(N-3)(2) + S(N-3)(3)  
근데 S(N-1)(1)이나 S(N-2)(1)이나 S(N-3)(1)은 1+1+1...+1로 같으니까
S(N) = 1+ S(N-2)(2) + S(N-3)(3) ???
근데 또 S(N-2)(2)는 S(N-3)(1)에 +2 하나만 더한거... S(N-3)(2)에도 +2 더할 수 있고...
근데 S(N-3)(2)도 S(N-4)(1) 그러니까 1+1 그리고 S(N-4)(2)+2... 그렇게 가다보면 
S(1)(1) = 1, S(1)(2) = 0, S(1)(3) = 0
S(2)(1) = 1, S(2)(2) = 1, S(2)(3) = 0
S(3)(1) = 1, S(3)(2) = 1, S(3)(3) = 1
S(4)(1) = 1, S(4)(2) = 2, S(4)(3) = 1
S(5) = 1 +  """

def _15989():
    T = int(input()) # 첫째줄: 테스트 케이스의 개수
    
    for _ in range(T):
        N = int(input()) # 둘째줄부터: 테스트 케이스를 입력
        arr = [1 for _ in range(N)] # S(N-1)(1)

        for i in range(1, N): # 배열을 모두 1로 초기화함으로써 S(N-2)(1)은 해결
            arr[i] += arr[i - 2] # S(N-2)(1) + S(N-2)(2) 
        pass
        print(arr[N-1])
    

#===============================================================================================================


"""  1010번 - 다리 놓기
; N은 서쪽에 있는 사이트의 개수, M은 동쪽에 있는 사이트의 개수
N ≤ M, 한 사이트에는 하나의 다리만 연결, 다리끼리 겹쳐질 수 없음, 총 N개의 다리를 짓는 경우의 수는?
; 사실상 서로 다른 M개에서 N개를 뽑는 조합의 수와 같음 -> M이 더 크니까 그 중 N개를 뽑기만 하면 알아서 다리들이 연결 
nCr = nPr/r! = n!/r!(n-r)! = n(n-1)...(n-r+1)/r! -> 여기서 두번째 수식으로 풀기?  """

def _1010():
    T = int(input()) # 첫째줄: 다리 놓기를 진행할 횟수
    
    def factorial(N): # 주어진 N에 대해 N!을 계산하는 함수
        res = 1
        for i in range(2, N+1): res *= i
        return res

    for _ in range(T):
        N, M = map(int, input().split()) # 둘째줄부터: 서쪽 사이트의 개수, 동쪽 사이트의 개수
        deno, numer = factorial(M), factorial(N) * factorial(M - N) # 분자는 M!, 분모는 N!(M-N)!
        res = deno // numer
        print(res)


#===============================================================================================================


# 최초에 heapq 모듈 없이 미해결 >>> 교재 코드 이용해서 해결
"""  5972번 - 택배 배송
; N은 노드의 개수 -> 1부터 모든 노드를 한번씩 거쳐서 N으로 가야 함
M은 간선의 개수 -> 간선은 N-1개를 거침 
한 노드가 여러 간선을 가질 수 있음, 어떤 두 노드는 끊어져 있을 수 있음
; C_i는 간선에 있는 소의 수 -> 소 한 마리당 하나의 여물을 주므로 여물의 수와 같음
A_i는 한쪽의 노드, B_i는 다른쪽의 노드, 이들은 간선으로 연결, 그 사이에 소가 있음, 하나씩 여물을 줌
1부터 N까지, 최소의 소를 만나서 최소의 여물을 주며 간다고 할 때, 줘야하는 여물의 총합은?  """

import sys
input = sys.stdin.readline

def _5972():
    N, M = map(int, input().split()) # 첫째줄: 노드의 개수, 간선의 개수
    shed_list = [[] for _ in range(N + 1)]
    # 예를 들어 shed_list[1]에 저장되어 있는 (4, 4)는 1번 헛간이 4번 헛간과 연결되어 있고 그 사이에는 4마리의 소가 있음을 의미
    
    for _ in range(M): # 둘째줄부터: 한쪽의 노드, 다른쪽의 노드, 그 사이 소의 수(여물의 수)를 입력받음 
        n1, n2, cow = map(int, input().split())    
        shed_list[n1].append((n2, cow))
        shed_list[n2].append((n1, cow))
    
    import heapq # 우선순위 큐를 이용하여 풀이
    
    q = []
    distance = [int(1e9)] * (N + 1) # 처음에는 거리를 모두 무한으로 초기화
    cost = 0 # 비용이 덜 든다 == 현재 노드를 거쳐서 다른 노드로 이동할 때의 거리가 더 짧다
    
    distance[1] = 0
    heapq.heappush(q, (0, 1))
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist: 
            continue
        
        for i in shed_list[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    print(distance[N])
