import sys
input = sys.stdin.readline


#==================================================================================================================


"""  정렬 1: 2750번 - 수 정렬하기  """
def _2750():
    N = int(input()) # 첫째줄: 수의 개수
    arr = [int(input()) for _ in range(N)] # 둘째줄부터: 정렬할 수들 -> 리스트에 저장

    for i in range(N): # 버블정렬로 입력받은 수들을 정렬
        for j in range(N):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    for i in arr: # 하나씩 출력해주면 완료
        print(i)


#==================================================================================================================


"""  정렬 2: 2751번 - 수 정렬하기 2  """
def _2751():
    N = int(input()) # 첫째줄: 수의 개수
    arr = [int(input()) for _ in range(N)] # 둘째줄부터: 정렬할 수들 -> 리스트에 저장

    arr.sort() # 해당 문제에서 권장된 내장함수로 입력받은 수들을 정렬

    for i in arr: # 하나씩 출력해주면 완료 
        print(i)


#==================================================================================================================


"""  정렬 3: 10989번 - 수 정렬하기 3  """
def _10989():
    N = int(input()) # 첫째줄: 수의 개수
    arr = [0 for _ in range(10001)] # 계수정렬로 정렬하기 위한 리스트

    for _ in range(N): 
        n = int(input()) # 둘째줄부터: 정렬할 수들 -> 그 수에 해당하는 원소를 +1
        arr[n] += 1

    for i in range(10001):
        if arr[i] != 0: # 한번이라도 등장했으면
            for _ in range(arr[i]):# 기록한 계수만큼 출력하고 다음 줄로 넘어감
                print(str(i) + '\n')


#==================================================================================================================


"""  정렬 4: 2108번 - 통계학  """
def _2108():
    N = int(input())
    
    num_list = [int(input()) for _ in range(N)] # 입력받은 값들을 차례로 리스트에 저장
    num_list.sort() # 오름차순 정렬
    
    res1 = round(sum(num_list) / N) # 산술평균
    res2 = num_list[N // 2] # 중앙값
    res3 = 0 # 최빈값
    res4 = max(num_list) - min(num_list) # 범위
    
    import collections
    
    tmp_list = collections.Counter(num_list).most_common()
    # [(값: 몇 번), (값: 몇 번), .... 이거를 빈도수가 가장 높은 값부터 정렬해서 반환]
    
    if len(tmp_list) == 1:
        res3 = tmp_list[0][0]
    elif tmp_list[0][1] == tmp_list[1][1]: # 최빈값이 여러 개면 두번째로 작은 값을 출력하도록 제시됨
        res3 = tmp_list[1][0]
    else:
        res3 = tmp_list[0][0]
    
    print(res1)
    print(res2)
    print(res3)
    print(res4)
    

#==================================================================================================================


"""  정렬 5: 1427번 - 소트인사이드  """
def _1427():
    N = input().rstrip() # 맨 뒤에 붙는 '\n' 제거하기 -> 리스트를 반환
    N = sorted(N, reverse=True) # 내장함수를 통해 내림차순으로 정렬 -> 리스트를 반환
    print(''.join(N))
    

#==================================================================================================================


"""  정렬 6: 11650번 - 좌표 정렬하기  """
def _11650():
    N = int(input()) # 첫째줄: 좌표의 개수
    arr = [tuple(map(int, input().split())) for _ in range(N)] # 둘째줄부터: 좌표의 정보를 튜플의 형태로 리스트에 저장
    arr.sort() # x좌표를 기준으로 오름차순으로 정렬

    for i in range(N): # 각 튜플을 언패킹해서 출력해주면 완료
        print(*arr[i])


#==================================================================================================================


"""  정렬 7: 11651번 - 좌표 정렬하기 2  """
def _11651():
    N = int(input()) # 첫째줄: 좌표의 개수
    arr = [tuple(map(int, input().split())) for _ in range(N)] # 둘째줄부터: 좌표의 정보를 튜플의 형태로 리스트에 저장
    arr.sort(key=lambda x: (x[1], x[0])) # sort 함수는 key를 기준으로 정렬 -> 저렇게 넘겨주면 일단 y좌표를 기준으로 정렬한 후 x좌표를 비교하는 형태

    for i in range(N): # 각 튜플을 언패킹해서 출력해주면 완료
        print(*arr[i])


#==================================================================================================================


"""  정렬 8: 1181번 - 단어 정렬  """
def _1181():
    N = int(input()) # 첫째줄: 단어의 개수
    arr = list(set(input() for _ in range(N))) # 둘째줄부터: 중복을 제거한 단어들을 최종적으로 리스트에 저장
    arr.sort(key=lambda x: (len(x), x)) # sort 함수의 key 매개변수를 이용 -> 저렇게 넘겨주면 일단 len(x)를 기준으로 오름차순 정렬 -> x를 기준으로 오름차순 정렬 (앞에 - 붙이면 내림차순으로도 가능)
    
    for i in arr: # 문제에서 주어진 조건대로 정렬한 단어를 하나씩 출력해주면 완료
        print(i)


#==================================================================================================================


"""  정렬 9: 10814번 - 나이순 정렬  """
def _10814():
    N = int(input()) # 첫째줄: 회원의 수
    arr = [tuple(input().split()) for _ in range(N)] # 둘째줄부터: 회원의 정보를 튜플의 형태로 리스트에 저장
    arr.sort(key=lambda x: int(x[0])) # sort 함수의 key 매개변수를 이용 -> 저렇게 넘겨주면 나이를 기준으로 오름차순 정렬 (나이가 같으면 먼저 가입한 순서가 기준이므로 이건 따로 조정 X)

    for i in range(len(arr)): # 각 튜플을 언패킹해서 출력해주면 완료
        print(*arr[i])


#==================================================================================================================


"""  정렬 10: 18870번 - 좌표 압축  """
def _18870():
    N = int(input()) # 첫째줄: 좌표의 개수
    arr1 = [i for i in map(int, input()[:-1].split())] # 둘째줄: 압축할 좌표들 -> 한줄에 입력받으므로 일단 '\n' 제거해서 각각을 정수로 만들어서 리스트에 저장
    arr2 = list(set(arr1)) # 중복을 제거해서
    arr2.sort() # 오름차순으로 정렬

    dict = {arr2[i]: i for i in range(len(arr2))} # 첫번째 원소는 0을 출력, 두번째 원소는 1를 출력, ... (자기보다 큰 값의 개수를 세서 출력해야 함)
    for key in arr1:
        print(dict[key], end=' ')


#==================================================================================================================


"""  이분 1: 1920번 - 수 찾기  """
def _1920():
    # 있어? 없어? 있으면 1을 출력, 없으면 0을 출력
    def binary_search(target, arr, start=0, end=None):

        if end == None: end = len(arr) - 1
        
        while start <= end:
            
            middle = (start + end) // 2
            
            if arr[middle] > target:
                end = middle - 1
            elif arr[middle] < target:
                start = middle + 1
            else:
                return 1 # arr2의 해당 요소가 arr1에 존재하면 1을 출력
        
        return 0 # 존재하지 않으면 0을 출력

    N = int(sys.stdin.readline())
    arr1 = list(map(int, sys.stdin.readline().split()))
    arr1.sort() # 이진탐색을 진행하는 배열이므로 정렬

    M = int(sys.stdin.readline())
    arr2 = list(map(int, sys.stdin.readline().split()))

    for i in arr2:
        print(binary_search(i, arr1))


#==================================================================================================================


"""  이분 2: 2805번 - 나무 자르기  """
def _2805():
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))

    start = 0
    end = max(trees)

    total_height = 0
    max_height = 0

    while start <= end:
        
        mid = (start + end) // 2
        
        '''for tree in trees:
            if tree < mid:
                total_height += tree - mid'''
        total_height = sum([tree - mid if tree > mid else 0 for tree in trees])
        
        if total_height < M:
            end = mid - 1
        else:
            start = mid + 1
            max_height = mid
        
    print(max_height)


#==================================================================================================================


"""  이분 3: 1300번 - K번째 수  """
def _1300():
    N = int(input())
    K = int(input())

    start = 1
    end = K
    number = 1

    while start <= end:
        
        middle = (start + end) // 2
        
        less_count = 0
        for i in range(1, N):
            less_count += min(middle // i, N)
        
        if less_count <= K - 1:
            start = middle + 1
            number = middle
        else:        
            end = middle - 1

    print(number)
