# 선형 큐
class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.rear = -1
        self.front = -1
    
    def isEmpty(self):
        return self.front == self.rear
        
    def isFull(self):
        return self.capacity - 1 == self.rear
    
    def enqueue(self, value):
        if not self.isFull():
            self.rear += 1
            self.array[self.rear] = value
        else:
            print("Overflow");
            
    def dequeue(self):
        if not self.isEmpty():
            self.front += 1
            return self.array[self.front]
        else:
            print("Underflow")   
    
    def size(self):
        return self.rear - self.front
    
    def display(self):
        for i in range(self.front + 1, self.rear + 1):
            print(self.array[i], " ", end="")
            
     
# 원형 큐
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * self.capacity
        self.rear = 0
        self.front = 0
        
        
    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity
        
    def enqueue(self, value):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = value 
            
        else:
            print("Overflow")
            
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else:
            print("Underflow")
            
    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity
    
    def display(self):
        for i in range(self.front + 1 , self.front + 1 + self.size()):
            print(self.array[i % self.capacity], " ", end=" ")



            
"""
q1 = Queue(10)

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
q1.enqueue(60)
q1.enqueue(70)
q1.enqueue(80)
q1.enqueue(90)
q1.enqueue(100)

print(q1.size())
q1.display()

print(q1.dequeue())
print(q1.size())

print(q1.dequeue())
print(q1.size())

q1.enqueue(110)

q1.display()


q2 = CircularQueue(10)

q2.enqueue(10)
q2.enqueue(20)
q2.enqueue(30)
q2.enqueue(40)
q2.enqueue(50)
q2.enqueue(60)
q2.enqueue(70)
q2.enqueue(80)
q2.enqueue(90)

print(q2.size())

q2.enqueue(100)

"""


# Josephus Problem
def josephus(n, k):
    
    # 1. 입력받은 n보다 1 큰 수의 용량을 갖는 큐 생성
    q = CircularQueue(n + 1)
    
    # 2. 1~n까지 정수를 큐에 인큐
    for i in range(1, n + 1):
        q.enqueue(i)
    
    print("초기 값 입력 : ", end=" ")
    q.display()
    
    # 3. 이제 큐의 원소가 하나 남을 때까지 아래 동작 반복
    while q.size() > 1:
        
        # 3.1. 큐의 맨 앞에 있는 원소 x를 디큐하고, 다시 x를 큐에 인큐하는 동작은 k-1번 반복
        for i in range(k - 1):
            j = q.dequeue()
            q.enqueue(j)
        print(f"제외 : {q.dequeue()}")  # 제거된 원소 출력
        print("현재 상태 : ", end="")
        q.display()


    return q.dequeue()



n = int(input("사람 수 입력 : "))
k = int(input("제외될 번호 입력 : "))
print("남은 사람의 번호는 : ", josephus(n, k))





