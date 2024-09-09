import java.io.*;
import java.util.*;

public class Test {
    public static void main(String[] args) throws IOException {

        // 1번 구구단
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        System.out.println("구구단을 입력하세요: ");
//        String input = br.readLine();
//
//        int[] result = gugudan(Integer.parseInt(input));
//
//        for (int i : result) {
//            System.out.println(i);
//        }

        // 2번
        // 10 미만의 자연수에서 3과 5의 배수를 구하면 3, 5, 6, 9이다. 이들의 총합은 23이다. 그렇다면 1000 미만의 자연수에서 3과 5의 배수의 총합을 구하라.
        int sum = 0;
        for(int n = 1; n < 1000; n++){
            if(n % 3 == 0 || n % 5 == 0){
                sum += n;
            }
        }
//        System.out.println(sum);

        String a = "점프 투 자바";

        System.out.println( a.replace(" ", "").length());
a.charAt(0);
    }

    public static int[] gugudan(int dan) {
        int[] result = new int[9];

        for (int i = 1; i <= result.length; i++) {
            result[i - 1] = dan * i;
        }

        return result;
    }

}
