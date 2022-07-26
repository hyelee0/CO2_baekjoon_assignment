import sys, math
input = sys.stdin.readline


#================================================================================================================================================================


"""  24416번 - 피보나치 수 1
; n번째 피노나치 수를 구해야 함 -> 재귀호출로 구할 때의 실행 횟수를 출력, 동적 계획법으로 구할 때의 실행 횟수를 출력  """

def _24416():
    def fibo_recursive(n):
        if n == 1 or n == 2:
            return 1
        else:
            return fibo_recursive(n - 1) + fibo_recursive(n - 2);
    
    def fibo_dynamic(n):
        f = [0 for _ in range(n+1)] # f = [0, 1, 1] 이렇게만 저장해두고 후에 f.append(fn)로 매번 추가하면 시간초과 -> 미리 공간을 모두 만들어둔 후 덮어쓰기 -> 또 시간초과...?
        f[1], f[2] = 1, 1
        count = 0
        for i in range(3, n+1):
            f[i] = f[i-1] + f[i-2]
            count += 1
        return count
    
    n = int(input())
    print(fibo_recursive(n), fibo_dynamic(n))


#================================================================================================================================================================


# need to retry
"""  9184번 - 신나는 함수 실행
; 문제에 제시된 대로 재귀함수를 작성하면 됨 -> 그대로 작성하면 시간 초과
; a, b, c 중 하나라도 0 이하이면 1을 반환 / a, b, c 중 하나라도 20 초과면 w(20, 20, 20)을 호출 -> 그냥 작성하면 됨
a < b < c 이면 w(.)+w(.)-w(.)을 반환 / 전부 아니면 w(.)+w(.)+w(.)-w(.)을 반환 -> how to......?  """

def _9184():
    my_list = []
    
    def w(a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            return 1
        elif a > 20 or b > 20 or c > 20:
            return w(20, 20, 20)
        pass
        pass
        pass
    
    while True:
        a, b, c = map(int, input().split()) # 입력 조건
        if a == -1 and b == -1 and c == -1: # 종료 조건
            break
        print("w(%d, %d, %d) = %d" %(a, b, c, w(a, b, c))) # 출력 조건


#================================================================================================================================================================


"""  1904번 - 01타일
; 타일 하나에는 0 또는 1이 쓰여있음 -> 여러 타일을 이어붙일 때는 00 또는 1로만 가능
00 1 11 0011 1111 이런 타일들은 가능 / 01 10 0001 110 이런 타일들은 불가능
; 어떤 수 N이 주어질 것 -> 길이 N의 모든 타일을 만드는 경우의 수는? 
그니까 현재 타일은 무수히 많이 있고, 이들을 00 또는 1로만 이어붙여서, 총 N개의 타일로 이루어진 일종의 수열을 만들어내는 가짓수는?
N이 1이면 1 / N이 2이면 00 11 / N이 3이면 001 100 111 / N이 4이면 0011 0000 1001 1100 1111 머 이런 식으로...
;    N | 1  2  3  4  5  6  7  8
가짓수 | 1  2  3  5  8 ... 이거 피보나치?  """

def _1904():
    N = int(input()) # 가짓수를 구할 타일 수열의 길이
    
    num_list = [0 for _ in range(N+2)] # 가짓수를 기록해둘 배열 (편의상 배열의 0번째 자리는 사용 X)
    num_list[1], num_list[2] = 1, 2
    
    for i in range(3, N+1): # n번째 피보나치 수를 구할 때처럼 계속해서 앞의 두 수를 더해나감
        num_list[i] = (num_list[i-1] + num_list[i-2]) % 15746 # 이거를 마지막에 한번만 나누면 메모리 초과...
    
    print(num_list[N])


#================================================================================================================================================================


"""  9461번 - 파도반 수열
; 정삼각형을 계속해서 붙여나감 -> 가장 긴 변의 길이가 업데이트 되면 그 변에 그 길이의 새로운 정삼각형을 추가함 -> 또 계속해서 붙여나가며 반복
길이 1의 tri 1개 -> 길이 1의 tri 3개가 모여서 한 변이 길이 2가 됨 -> 길이 2의 tri 1개 -> 길이 1의 tri 1개와 길이 2의 tri 2개가 모여서 한 변이 길이 3이 됨 -> 뭐 이런 식으로...
; 파도반 수열 P(N)은 나선에 있는 N번째 tri의 변의 길이 -> P(10) = 1 1 1 2 2 3 4 5 7 9 
여기서 규칙성이... P(N) = P(N-2)+P(N-3) !!!
; 주어진 테스트 케이스의 횟수만큼 P(N)을 구하면 됨 -> 전체적인 과정은 위 문제와 동일하게...  """

def _9461():
    T = int(input()) # 테스트 케이스의 횟수

    for _ in range(T): # 테스트 케이스만큼 반복해서 P(N)을 구함
        N = int(input())
        num_list = [0 for _ in range(101)] # 각 차례의 파도반 수를 기록해둘 배열 (편의상 배열의 0번째 자리는 사용 X)
        num_list[1], num_list[2], num_list[3] = 1, 1, 1
    
        for i in range(4, N+1):
            num_list[i] = num_list[i-2] + num_list[i-3] # F(N)을 구할 때처럼 계속해서 이전 두 수를 더해나감
        
        print(num_list[N])


#================================================================================================================================================================


"""  1912번 - 연속합
; n개의 정수로 이루어진 어떤 수열이 주어짐 -> 연속된 몇 개의 정수를 택해서 구할 수 있는 가장 큰 합은? (정수는 1개 이상 택해야 함)
num_list = [10 -4 3 1 5 6 -35 12 21 -1] -> 연속된 2개의 정수 12와 21을 택했을 때의 33이 정답
; 일단 최대합에 max(num_list) 넣어두고 시작 (뭐 예를 들어 하나 빼고 전부 음수면 이게 정답)
현재 정수까지의 합을 저장할 배열이 필요 (0번째 자리 사용 X) -> 그니까 arr[i]는 i+1번째 정수까지 모두 더한 합 (위의 예로 보면 arr[0]은 10, arr[1]는 6, arr[2]는 9)
이전 정수까지의 합에 새로운 정수를 더한 것 vs 새로운 정수  """

def _1912():
    n = int(input()) # 수열의 길이
    num_list = list(map(int, input().split())) # 수열의 각 원소
    record_list = [0 for _ in range(n)] # 현재 정수까지의 합 (만약 이번 차례의 정수가 더 크면 이 정수가 저장됨)
    record_list[0] = num_list[0]
    
    max_sum = max(num_list) # 가장 큰 정수를 넣어두고 시작
    for i in range(1, len(num_list)):
        record_list[i] = max(record_list[i-1]+num_list[i], num_list[i])
        # max_sum = record_list[i]
        max_sum = max(record_list[i], max_sum)
        # print(record_list, max_sum)
    
    print(max_sum)


#================================================================================================================================================================


# need to re-try
"""  1149번 - RGB 거리
; 1번부터 N번까지 총 N개의 집이 있음 -> 각 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 함 -> 각 색을 칠할 때마다 비용이 듬
조건은... 1번과 2번은 서로 다른 색, N번과 N-1번은 서로 다른 색, 2번~N-1번은 하나 작은 번호와 하나 큰 번호 둘 다와 서로 다른 색
"""

def _1149():
    N = int(input()) # 집의 개수
    cost_list = [list(map(int, input().split())) for _ in range(N)]
    
    pass
    pass
    pass


#================================================================================================================================================================


"""  1932번 - 정수 삼각형  """

def _1932():
    n = int(input())
    num_list = [list(map(int, input().split())) for _ in range(n)]
    # num_list = [
    #   [7],                    [0][0]
    #   [3, 8],                 [1][0] [1][1]
    #   [8, 1, 0],              [2][0] [2][1] [2][2]
    #   [2, 7, 4, 4],           [3][0] ... [3][3]
    #   [4, 5, 2, 6, 5]         [4][0] ... [4][4]
    #   ]
    
    record_list = []
    for i in range(n):
        record_list.append([num_list[0][0] for _ in range(len(num_list[i]))])
    # record_list = [
    #   [7], 
    #   [7, 7],
    #   [7, 7, 7],
    #   [7, 7, 7, 7],
    #   [7, 7, 7, 7, 7]
    #   ]

    for i in range(1, n):
        for j in range(i+1):
            if j == 0: # 각 층의 첫번째 수
                record_list[i][j] = record_list[i-1][j] + num_list[i][j]
            elif i == j: # 각 층의 마지막 수
                record_list[i][j] = record_list[i-1][j-1] + num_list[i][j]
            else: # 각 층의 가운데 수
                record_list[i][j] = max(record_list[i-1][j-1], record_list[i-1][j]) + num_list[i][j]
    
    print(max(record_list[n-1]))


#================================================================================================================================================================


"""  2579번 - 계단 오르기
; 1번부터 N번까지 총 N개의 계단이 있음 -> 각 계단에는 점수가 적혀 있음 -> 조건에 따라 계단을 밟아가며 점수를 얻을 때 얻을 수 있 점수의 최댓값은?
조건은... 한번에 한 계단 또는 두 계단, 연속된 세 계단 X, 마지막 계단은 반드시 O
(쉽게 말해 1번에서 2번 또는 3번은 되지만 4번은 안됨, 1번 2번 3번 연속으로 안됨, N번은 무조건 밟기)
; score = [10 20 15 25 10 20], 추가로 현재까지 얻은 점수의 합을 기록할 배열이 필요 (0번째 자리는 사용 X)
계단이 하나면 score[1]이 정답, 계단이 두개면 score[1]+score[2], 계단이 세개 이상부터는...
현재 계단 밟았을 때 그 전 계단도 밟았던 경우 (그 전 전 계단은 밟으면 안됨) -> score[i] + score[i-1] + arr[i-3]
현재 계단 밟았을 때 그 전 계단은 안 밟았던 경우 -> score[i] + arr[i-2]  """

def _2579():
    N = int(input()) # 계단의 개수
    score_list = [0] + [int(input()) for _ in range(N)] # 각 계단의 점수
    record_list = [0 for _ in range(N+1)] # 현재까지 밟은 계단으로부터 얻은 점수의 합    

    for i in range(1, N+1):
        if i == 1: # 계단이 1개일 때
            record_list[1] = score_list[1]
        elif i == 2: # 계단이 2개일 때
            record_list[2] = score_list[1] + score_list[2]
        else: # 계단이 3개 이상일 때 (이때부터는 경우가 나뉨)
            record_list[i] = max(score_list[i]+score_list[i-1]+record_list[i-3], score_list[i]+record_list[i-2])
    
    print(record_list[N])


#================================================================================================================================================================


# need to comprehension
"""  1463번 - 1로 만들기
; 정수 N이 하나 주어질 것 -> 가능한 연산은 다음 세 가지 뿐 -> N을 1로 만들기 위해 필요한 최소한의 연산 수는?
if N % 3 == 0 then N <- int(N/3) / if N % 2 == 0 then N <- int(N/2) / just N - 1 -> 대체 뭔 아이디어로...
"""

def _1463():
    N = int(input()) # 1로 만들 정수
    record_list = [0 for _ in range(N+1)] # 해당 수가 되기까지 필요한 최소한의 연산 횟수

    for i in range(1, N+1):
        result_list = []
        if i % 3 == 0:
            result_list.append(record_list[i // 3])
        if i % 2 == 0:
            result_list.append(record_list[i // 2])
        result_list.append(record_list[i - 1])
        record_list[i] = min(result_list) + 1

    print(record_list[N])


#================================================================================================================================================================


"""  10844번 - 쉬운 계단 수
; 45656처럼 모든 인접한 두 숫자의 차가 1인 수를 계단 수라고 함 -> 자릿수가 N인 양수 중 계단 수는 몇개?
일단 0 뒤에는 1만, 9 뒤에는 8만, 1~8 뒤에는 0~i-1 또는 i+1~9가 오게 됨
; 각 계단 수는 0
; 어떤 이차원 리스트를 갖고 와서... 일단 뒤의 인덱스는 앞에 오는 숫자...
[자리수][0] <- [자리수-1][1] / [자리수][9] <- [자리수-1][8] / [자리수][1~8] <- [자리수][1~8-1] + [자리수][1~8+1]
"""

def _10844():
    N = int(input()) # 자릿수
    record_list = [[0 for _ in range(10)] for __ in range(101)]
    
    for i in range(1, N+1):
        if i == 1:
            record_list[1][i] = 1
        for j in range(10):
            if j == 0:
                record_list[i][j] = record_list[i-1][1]
            elif j == 9:
                record_list[i][j] = record_list[i-1][8]
            else:
                record_list[i][j] = record_list[i-1][j-1] + record_list[i-1][j+1]
    
    print(sum(record_list[N]) % 1000000000)


#================================================================================================================================================================


"""  2156번 - 포도주 시식
; 1번부터 N번까지 총 N개의 포도주잔이 있음 -> 각 포도주잔마다 양이 주어짐 -> 선택한 잔은 모두 비움, 연속된 세 잔은 선택 X -> 최대로 마실 수 있는 포도주의 양은?
위의 2579번이랑 동일하게...?  """

def _2156():
    n = int(input()) # 포도주잔의 개수
    mL_list =  [0] + [int(input()) for _ in range(n)] # 각 포도주의 양
    record_list = [0 for _ in range(n+1)] # 현재까지 마신 포도주의 총량
    
    for i in range(1, n+1):
        if i == 1: # 계단이 1개일 때
            record_list[1] = mL_list[1]
        elif i == 2: # 계단이 2개일 때
            record_list[2] = mL_list[1] + mL_list[2]
        else: # 계단이 3개 이상일 때 (이때부터는 경우가 나뉨)
            record_list[i] = max(mL_list[i]+mL_list[i-1]+record_list[i-3], mL_list[i]+record_list[i-2])
            record_list[i] = max(record_list[i], record_list[i-1]) # .......???? 추가하면 정답
    
    print(record_list[n])


#================================================================================================================================================================


"""  11053번 - 가장 긴 증가하는 부분 수열  """

def _11053():
    N = int(input()) # 수열의 길이
    num_list = list(map(int, input().split())) # 수열의 각 원소
    record_list = [1 for _ in range(N)] # 부분 수열의 최소 길이는 1 (모든 원소가 같은 경우)
    
    for i in range(N):
        max_value = 1
        for j in range(i):
            if num_list[i] > num_list[j]:
                max_value = max(record_list[i], record_list[j]+1)
            record_list[i] = max_value

    print(max(record_list))


#================================================================================================================================================================


# need to retry
"""  11054번 - 가장 긴 바이토닉 부분 수열  """

def _11054():
    N = int(input())
    num_list = list(map(int, input().split()))
    reverse_num_list = list(reversed(num_list))
    length_record1 = [1 for _ in range(N)]
    length_record2 = [1 for _ in range(N)]
    
    for i in range(N): # 위의 max_value 변수 꼭 필요...?
        for j in range(i):
            if num_list[i] > num_list[j]:
                length_record1[i] = max(length_record1[i], length_record1[j]+1)
            if reverse_num_list[i] > reverse_num_list[j]:
                length_record2[i] = max(length_record2[i], length_record2[j]+1)
    pass
    pass
    pass


#================================================================================================================================================================


"""  2565번 - 전깃줄
; 두 전봇대 사이에 N개의 전깃줄이 연결되어 있음 -> 1 8이면 1번과 8번 사이, 4 1이면 4번과 1번 사이... -> 마구잡이로 교차하고 있음
여기서 모든 전깃줄이 하나도 교차하지 않도록 하려면 몇 개의 전깃줄을 끊어야 할까?
; 교차하지 않는다는 건... 시작 번호에 대응되는 도착 번호가 오름차순이어야 한다는 것... 예시처럼 8번 도착했다가 2번 도착하면 교차하게 됨...
따라서 위의 11053번처럼 가장 긴 증가하는 부분 수열을 찾음 -> 전체 전깃줄의 개수에서 해당 부분 수열의 길이를 빼주면 됨  """

def _2565():
    N = int(input())
    wire_list = [list(map(int, input().split())) for _ in range(N)]
    wire_list.sort(key=lambda x: x[0])
    # [[1, 8], [3, 9], [2, 2], [4, 1], [6, 4], [10, 10], [9, 7], [7, 6]]
    # [[1, 8], [2, 2], [3, 9], [4, 1], [6, 4], [7, 6], [9, 7], [10, 10]]
    
    arrive_num_list = [b for a, b in wire_list]
    record_list = [1 for _ in range(N)]
    
    for i in range(N):
        max_value = 1
        for j in range(i):
            if arrive_num_list[i] > arrive_num_list[j]:
                max_value = max(record_list[i], record_list[j]+1)
            record_list[i] = max_value

    print(N - max(record_list))


#================================================================================================================================================================


"""  9251번 - LCS  
\  -  C  A  P  C  A  K  ; 각 문자열 앞의 하이픈은 배열의 0번째 자리를 건너뛰기 위함
-  0  0  0  0  0  0  0  ; 일단 문자가 일치하면 초깃값 0에서 그 위의 값+1로 갱신
A  0  0  1  1  1  1  1  ; 문자가 일치하지 않을 때는... 어쩔 땐 그 위의 값... 어쩔 땐 바로 이전 값...
C  0  1  1  1  2  2  2  여기서 CC는 일치하니까 위의 0+1, CA와 CP는 일치 안하니까 이전?위?의 1, 다시 CC는 일치하니까 위의 1+1, CA는 일치 안하니까 이전 2...
A  0  1  2  2  2  3  3
Y  0  1  2  2  2  3  3
K  0  1  2  2  2  3  4
P  0  1  2  2  2  3  4  """

def _9251():
    str1 = '-' + input()
    str2 = '-' + input()
    
    record_list = [[0 for _ in range(len(str2))] for _ in range(len(str1))]
    for i in range(1, len(str1)):
        for j in range(1, len(str2)):
            if str1[i] == str2[j]:
                record_list[i][j] = record_list[i-1][j-1] + 1
            else:
                if record_list[i][j-1] > record_list[i-1][j]:
                    record_list[i][j] = record_list[i][j-1]
                else:
                    record_list[i][j] = record_list[i-1][j]
    
    print(record_list[len(str1)-2][len(str2)-2])

    
#================================================================================================================================================================


# need to retry
"""  12865번 - 평범한 배낭
; 주어진 물건의 개수는 N, 각 물건의 무게는 W, 각 물건의 가치는 V -> 상한 무게는 K
그러니까 총 무게가 K를 넘지 않도록 N개를 잘 챙길건데 이때 가능한 가치의 최댓값은?
"""

def _12865():
    N, K = map(int, input().split()) # 물건의 개수와 상한 무게
    weight_list, value_list = [0], [0] # 각 물건의 무게와 가치
    record_list = [[0 for _ in range(K+1)] for _ in range(N+1)] # 현재까지 챙긴 물건으로부터 계산된 가치의 최댓값
    
    for _ in range(N):
        W, V = map(int, input().split())
        weight_list.append(W)
        value_list.append(V)
    
    for i in range(1, N+1):
            pass
            pass
            pass

    print(record_list[N][K])

