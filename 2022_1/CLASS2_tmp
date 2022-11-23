import sys
input = sys.stdin.readline


#================================================================================================================================================================


"""  2839번 - 설탕 배달  """

def _2839():
    N = int(input())
    cnt = 0
    
    while True:
        if N % 5 == 0:
            cnt += N // 5
            print(cnt)
            break
        else: 
            N -= 3
            cnt += 1

        if N < 0:
            print(-1)
            break


#================================================================================================================================================================


"""  4949번 - 균형잡힌 세상  """

def _4949():
    while True:
        sentence = input().rstrip() # ...? rstrip 안 쓰면 출력 초과
        if sentence == '.': break
    
        stack = []
        for s in sentence:
            if s in '[(':
                stack.append(s)
            elif s == ']':
                if len(stack) != 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(s)
                    break
            elif s == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s)
                    break
        
        if len(stack) == 0: print("yes")
        else: print("no")
    

#================================================================================================================================================================


"""  9012번 - 괄호  """

def _9012():
    T = int(input())
    
    for _ in range(T):
        PS = list(input().rstrip())
        stack = []
        for s in PS:
            if s == '(':
                stack.append(s)
            elif s == ')':
                if len(stack) != 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s)
                    break

    if len(stack) == 0: print("YES")
    else: print("NO")


#================================================================================================================================================================


"""  10773번 - 제로  """

def _10773():
    K = int(input())
    num_list = []
    
    for _ in range(K):
        num = int(input())
        if num == 0:
        # if num == 0 and len(num_list) != 0: 어차피 이때 스택은 안 비어있음이 보장된다고 했으니까
            num_list.pop()
        else:
            num_list.append(num)

    print(sum(num_list))


#================================================================================================================================================================


"""  10816번 - 숫자 카드 2
; [6, 3, 10, 10, 10, -10, -10, 3] -> {6: 1, 3: 2, 10: 3, -10: 2} -> if 숫자(키) in 딕셔너리 then 값을 출력  """

def _10816():
    N = int(input())
    card_list = list(map(int, input().split()))
    M = int(sys.stdin.readline())
    num_list = list(map(int, input().split()))

    card_dict = {}
    for i in card_list:
        if i not in card_dict: 
            card_dict[i] = 1
        else: 
            card_dict[i] += 1

    for i in num_list:
        if i in card_dict: 
            print(card_dict[i], end=' ')
        else: 
            print(0, end=' ')


#================================================================================================================================================================


"""  10828번 - 스택  """

def _10828():
    N = int(input())
    stack = []
    
    for _ in range(N):
        order = input().split()
        if order[0] == 'push':
            stack.append(order[1])
        elif order[0] == 'pop':
            if len(stack) == 0: print(-1)
            else: print(stack.pop())
        elif order[0] == 'size':
            print(len(stack))
        elif order[0] == 'empty':
            if len(stack) == 0: print(1)
            else: print(0)
        elif order[0] == 'top':
            if len(stack) == 0: print(-1)
            else: print(stack[-1])


#================================================================================================================================================================


"""  10845번 - 큐  """

def _10845():
    N = int(input())
    queue = []
    
    for _ in range(N):
        order = input().split()
        if order[0] == 'push':
            queue.append(order[1])
        elif order[0] == 'pop':
            if len(queue) == 0: print(-1)
            else: print(queue.pop(0))
        elif order[0] == 'size':
            print(len(queue))
        elif order[0] == 'empty':
            if len(queue) == 0: print(1)
            else: print(0)
        elif order[0] == 'front':
            if len(queue) == 0: print(-1)
            else: print(queue[0])
        elif order[0] == 'back':
            if len(queue) == 0: print(-1)
            else: print(queue[-1])


#================================================================================================================================================================


"""  10866번 - 덱  """

def _10866():
    N = int(input())
    deque = []
    
    for _ in range(N):
        order = input().split()
        if order[0] == 'push_front':
            deque.insert(0, order[1])
        elif order[0] == 'push_back':
            deque.append(order[1])
        elif order[0] == 'pop_front':
            if len(deque) == 0: print(-1)
            else: print(deque.pop(0))
        elif order[0] == 'pop_back':
            if len(deque) == 0: print(-1)
            else: print(deque.pop(-1))
        elif order[0] == 'size':
            print(len(deque))
        elif order[0] == 'empty':
            if len(deque) == 0: print(1)
            else: print(0)
        elif order[0] == 'front':
            if len(deque) == 0: print(-1)
            else: print(deque[0])
        elif order[0] == 'back':
            if len(deque) == 0: print(-1)
            else: print(deque[-1])


#================================================================================================================================================================


"""  1929번 - 소수 구하기
; while-else처럼 for-else문...?이라는 것도 존재함 근데 원래대로 check 변수 추가로 이용하면 됨

"""

def _1929():
    M, N = map(int, input().split())

    for i in range(M, N+1):
        if i == 1: continue
        check = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                check = False
                break
        if check == True:
            print(i)


#================================================================================================================================================================


"""  1966번 - 프린터 큐  """

def _1966():
    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())
        importance_list = list(map(int, input().split()))
        document_list = list(range(0, N))
        document_list[M] = 'here'
        order = 0
        
        while len(importance_list) != 0:
            if importance_list[0] == max(importance_list):
                order += 1
                if document_list[0] == 'here':
                    print(order)
                    break
                else:
                    document_list.pop(0)
                    importance_list.pop(0)
            else:
                document_list.append(document_list.pop(0))
                importance_list.append(importance_list.pop(0))
