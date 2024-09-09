# # range(시작값, 종료값, 증감값)
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f"{i} * {j} = {i * j}")
#     print("=" * 10)

# print(*range(10)) ## Unpacking

# # 거꾸로 출력 구구단
# for i in range(2, 10):
#     for j in range(9, 0, -1):
#         print(f"{i} * {j} = {i * j}")
#     print("=" * 10)

# # 짝수만 출력 구구단
# for i in range(0, 10):
#     for j in range(0, 10, 2):
#         print(f"{i} * {j} = {i * j}")
#     print("=" * 10)


# num = int(input("구구단의 몇 단을 출력할까요?"))
# print(type(num))
# for i in range(1, 10):
#     print(f"{num} * {i} = {num * i }")


# # 1~100 합 구하기
# num = 0
# for i in range(1, 101):
#     num += i
# print(num)

# 피보나치 수열 
# num = [1, 1]  
# for i in range(2, 10):
#     num.append(num[i-2] + num[i-1])  # append로 새로운 값 추가

# print(num)

# 별찍기
# num = int(input("숫자를 입력하세요"))

# for i in range(1, num+1):   # 별 찍기의 열을 나타냅니다.   
#     for j in range(1, i+1): # 별 찍기의 행을 나타냅니다.
#         print("*", end='')  # end=''는 라인 변경을 하지 않습니다.
#     print()                 # 행을 전부 찍고 나면 라인을 변경합니다.

# for i in range(1, 6):
#     print("*" * i)
# print()

# for i in range(6, 0, -1):
#     print("*" * i)
# print()

# for i in range(1, 6):
#     print(" " * (5 - i) + "*" * i)
# print()


## 문제 출제
print("문제~~ 입니다. 답은?")
answer = input("1번. 바보 2번. 멍청이")
if answer == "1번":
    print("정답")
else :
    print("오답")