# list
a = []
b = list()
c = [3,7,2,6,9]

print(type(a))
print(type(b))
print(type(c))

print(a)
print(b)
print(c)

print(c[0])

gifts = ['장난감', '케이크', '동화책', '운동화', '가방']

for gift in gifts:
    print(gift)

for i in range(len(gifts)):
    print(f"{i+1} 번째 선물 = {gifts[i]}")
  
print(gifts[1:4])

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr[1:8:2])
print(arr[::-1])

# 파이썬에서는 인덱스도 필요하고, 리스트의 요소도 필요한 경우 enumerate 라는 함수를 사용
# enumerate는 인덱스와 데이터 둘 다 필요할 때 인덱스와 데이터를 튜플 형태로 리턴


# 선물 리스트 프로그램 만들기

# 1 입력시 선물의 총 갯수를 확인한다
# 2 입력시 선물의 전체 리스트를 확인한다
# 3 입력시 보고싶은 순서의 선물을 확인한다
# 리스트의 인덱스를 입력하면 해당 선물을 보여준다
# 4 입력시 선물의 부분 리스트를 확인한다
# 리스트의 시작과 끝을 입력하면 주어진 범위의 선물을 보여준다
# 0을 입력하면 끝낸다

def print_menu():
    print("*" * 20)
    print("레오의 선물 리스트!!")
    print("무엇을 할까요?")
    print("1. 선물 갯수 보기")
    print("2. 선물 전체 보기")
    print("3. 정해진 순서의 선물 보기")
    print("4. 정해진 범위의 선물 보기")
    print("0. 끝내기")

num = 0

while num != 0:
    print_menu()
    num = int(input())

    if num == 1:
        print(len(gifts))
    elif num == 2:
        print(gifts)
    elif num == 3:
        i = int(input("몇 번째 선물을 볼까요?"))
        print(gifts[i - 1])
    elif num == 4:
        i = int(input("몇 번째 선물부터 확인할까요?"))
        j = int(input("몇 번째 선물까지 볼까요?"))
        print(gifts[i - 1 : j])
    elif num == 0:
        break;


# 리스트 추가하기
gifts.append('게임기') # 기존 리스트의 마지막에 추가됨
gifts.insert(1, "색얀필") # insert(추가할 인덱스, 추가할 항목)
print(gifts)

gifts[1] = '수정'
print(gifts)

# 리스트 값 삭제
del gifts[1] # del 리스트[인덱스]
print(gifts)

gifts.remove("동화책") # 리스트.remove(삭제할 요소)
print(gifts)

# 요소 찾기
if "색연필" in gifts:
    print("색연필이 있습니다.")
else:
    print("색연필이 없습니다.")

# 요소 꺼내고 삭제하기
arr = [1, 2, 3, 4, 5]
temp = arr.pop()
print(temp)
print(arr)
temp = arr.pop(0)
print(temp)
print(arr)

# 리스트 더하기
a1 = [1,2,3,4]
a2 = [5,6,7,8]

all = a1 + a2
a1.extend(a2)
print(all)
print(a1)


# 리스트 곱하기
arr = [0] * 100
# 0으로 초기화 되어 있는 100개의 데이터가 들어있는 리스트. 특정 값으로 초기화할 때 많이 사용

print(a1.count(3))

my_list = [i * i for i in range(1, 11)]
print(my_list) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

## 이차원 배열
num = 5
my_list = [[num * i + j for j in range(num)] for i in range(num)]
print(my_list)
# [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]

num = 5
my_list = []
for i in range(num):
    row = []
    for j in range(num):
        row.append(num * i + j)
    my_list.append(row)
print(my_list)

# 리스트의 특징
# 리스트는 자료들의 모임입니다.
# 순서를 가지고 있어 순서를 가지고 항목에 접근할 수 있습니다.
# 어떠한 자료형도 넣을 수 있습니다.
# 자유롭게 변경이 가능하며 중복이 허용됩니다.