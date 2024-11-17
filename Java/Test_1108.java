import java.util.Scanner;

public class Test_1108 {
    public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int m = sc.nextInt();
        int cook = sc.nextInt();
        
        h += cook / 60; 
        cook %= 60;
        m += cook;
        
        if(m >= 60){
            m -= 60;
            h++;
            if(h == 24){
                h = 0;
            }
            
        }
        System.out.println(h + " " + m);

    }
    
}
