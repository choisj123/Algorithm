package home.algorithm.problem.run;

import java.util.Scanner;

import home.algorithm.problem.Algorithm;

public class AlgorithmRun {

	public static void main(String[] args) {
		
		Algorithm a = new Algorithm();
		
//		System.out.println(a.solution(11,11));

		// 최대공배수 & 최소공배수 구하기
//		Scanner sc = new Scanner(System.in);
//		
//		System.out.print("숫자1 >>");
//		int num1 = sc.nextInt();
//		System.out.print("숫자2 >>");
//		int num2 = sc.nextInt();
//		
//		int max = 0; //최대 공약수
//		for(int i = 1; i <= num1 && i <= num2; i++) {
//			System.out.println("for문 : " + i);
//			if(num1 % i == 0 && num2 % i == 0) {
//				
//				max = i;
//				System.out.println("if문 : " + i);
//			}
//		}
//		int min = (num1 * num2)/max; // 최소 공배수
//		System.out.println("최대 공약수 : " + max);
//		System.out.println("최소 공배수 : " + min);
//		
//		
		//System.out.println(a.solution(9, 2, 1, 3));
		
		System.out.println(a.solution("3141592", "271"));
//		System.out.println(a.solution("500220839878", "7"));
//		System.out.println(a.solution("10203", "15"));
		
	}
	
	

}
