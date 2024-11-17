import java.util.Scanner;

public class Queue {
    private int capacity;
    private int[] array;
    private int rear;
    private int front;

    public Queue(int capacity){
        this.capacity = capacity;
        this.array = new int[capacity];
        this.rear = 0;
        this.front = 0;
    }

    public boolean isEmpty(){
        return front == rear;
    }
    
    public boolean isFull(){
        return front == (rear + 1) % capacity;
    }

    public void enqueue(int value){
        if (!isFull()){
            rear = (rear + 1) % capacity;
            array[rear] = value;
        }else{
            System.out.println("Overflow");
        }
    }
    
    public int dequeue(){
        if (!isEmpty()){
            front = (front + 1) % capacity;
            return array[front];
        }else{
            System.out.println("Underflow");
            return -1;
        }
    }

    public int size(){
        return (rear - front + capacity) % capacity;
    }

    public void display(){
        for(int i = front + 1; i < front + 1 + size(); i++ ){
            System.out.print(array[i % capacity] + " ");
        }
    }

    public static int josephus(int n, int k){
            Queue q1 = new Queue(n + 1);
    
            for(int i = 1; i < n + 1; i++){
                q1.enqueue(i);
            }
    
            while (q1.size() > 1){
                for(int i = 0; i < k -1; i++){
                    int j = q1.dequeue();
                    q1.enqueue(j);
                }
                q1.dequeue();
            }
            return q1.dequeue();
        }
    
    
        public static void main(String[] args){
            Queue q = new Queue(10);
    
            q.enqueue(10);
            q.enqueue(20);
            q.enqueue(30);
            q.enqueue(40);
            q.enqueue(50);
            q.enqueue(60);
            q.enqueue(70);
            q.enqueue(80);
            q.enqueue(90);
    
            q.display();
            System.out.println();
    
            System.out.println(q.dequeue());
            q.display();
            System.out.println();
            System.out.println(q.size());
    
            q.enqueue(100);
            q.display();
            System.out.println();
            System.out.println(q.size());
    
            Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();
            int k = sc.nextInt();
            System.out.println(josephus(n,k));
    }

}