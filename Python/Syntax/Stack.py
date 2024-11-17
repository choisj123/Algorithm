# 클래스 선언
class Stack:
    def __init__(self, capacity): # 생성자 메서드
        self.capacity = capacity # 값 초기화
        self.array = [None] * self.capacity # 배열
        self.top = -1
        
    def isEmpty(self):
       return self.top == -1
   
    def isFull(self):
        return self.capacity - 1 == self.top
    
    def push(self, value):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = value
        else:
            print("Stack Overflow")
    
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top + 1]
        else:
            print("Stack Underflow")
            
            
    def size(self):
        return self.top + 1
    
    def display(self):
        for i in range(self.top + 1):
            print(self.array[i], " ", end="") 
            


# 객체 생성
s1 = Stack(10)
s2 = Stack(100)

s1.push(10)
s1.push(20)
s1.push(30)


print(s1.pop())
print(s1.size())
s1.display()




# 괄호 짝맞추기 체크 함수
def check_brackets(str, length):
    s1 = Stack(length)
    
    for ch in str:
        if ch == "(":
            s1.push(ch)
        elif ch == ")":
            if s1.isEmpty():
                return False
            else:
                s1.pop()
        else:
            pass
    return s1.isEmpty()
            
        

str = input("수식 입력 : ")
print("괄호 짝 맞추기 결과 :" , check_brackets(str, len(str)))
      
