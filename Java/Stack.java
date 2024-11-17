public class Stack {
    private int capacity; // 스택의 최대 크기
    private int[] array; // 스택 데이터를 저장할 배열
    private int top; // 스택의 최상단을 나타내는 인덱스

    public Stack(int capacity){
        this.capacity = capacity;
        this.array = new int[capacity];
        this.top = -1; // 초기 상태: 스택이 비어있음
    }
    
    public boolean isEmpty(){
        return top == -1;
    }

    public boolean isFull(){
        return capacity -1 == top;
    }

    public void push(int value){
        if(!isFull()){
            top++;
            array[top] = value;
        }else{
            System.out.println("Stack Overflow");
        }
    }

    public int pop(){
        if(!isEmpty()){
            int value = array[top];
            top--;
            return value;
        }else{
            System.out.println("Stack Underflow");
            return -1;
        }
    }

    public int size(){
        return top + 1;
    }

    public void display(){
        for(int i = 0; i <= top; i++){
            System.out.println(array[i] + " ");
        }
        System.out.println();
    }


    public static void main(String[] args){
        Stack stack = new Stack(5);

        stack.push(10);
        stack.push(20);
        stack.push(30);

        System.out.println(" 스택 내용 : ");
        stack.display();

        System.err.println(stack.pop());
        System.out.println();
        stack.display();
        
        System.out.println( stack.size());
       
    }
}
