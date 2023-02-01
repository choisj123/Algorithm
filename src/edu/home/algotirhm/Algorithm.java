package edu.home.algotirhm;

import java.util.Scanner;

public class Algorithm {

	Scanner sc = new Scanner(System.in);
	
	// 01.27
	public void Alram() {
		// 입력받은 시간보다 45분 일찍 알람 맞추기
		
		// 시간 입력
		System.out.print("시간을 입력하세요(H) : ");
		int h = sc.nextInt();
		
		System.out.print("분을 입력하세요(M) : ");
		int m = sc.nextInt();
		
		
		// 6시 --> 5시 15분 
		// h는 0 ~ 23 , m은 0 ~ 59 
		
		// 상근이가 입력한 시간
		System.out.println("상근이가 설정한 알람 : " + h + "시 " + m + "분");
		
		int output = ((h * 60) + m - 45);
		
		if (output < 0) {
			output += 60 * 24;
			
		}
		System.out.println("45분 전 알람 : " + output / 60 + "시 " + output % 60 + "분");
		System.out.println("github연동 테스트");

		
	}
	
	
	public void dice() {
		// 주사위를 2개 던져서 합계로 짝홀수 구하기
		// 합계가 짝수일 경우 짝!
		// 합계가 홀수일 경우 홀! 
		// 같은 값일 경우 더블! 출력
		
		int dice1 = (int)(Math.random() * 6 + 1);
		int dice2 = (int)(Math.random() * 6 + 1);
		
		int result = dice1 + dice2;
		
		System.out.println("첫번째 주사위 : " + dice1);
		System.out.println("두번째 주사위 : " + dice2);
		
		if (result % 2 == 0) {
			
			System.out.println();
			System.out.println("결과는 바로바로 ~ 짝!");
	
		} else if (result % 2 != 0) {
			System.out.println();
			System.out.println("결과는 바로바로 ~ 홀!");
			
		} else {
			System.out.println();
			System.out.println("결과는 바로바로 ~ 더블!");
			
		}
		
		
		
	}
	
	
	public boolean solution(String s) {	
		/*
		 * 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 
		 * 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 
		 * 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
			예를 들어 s가 "pPoooyY"면 true를 return하고 "Pyy"라면 false를 return합니다.
			
			제한사항
			문자열 s의 길이 : 50 이하의 자연수
			문자열 s는 알파벳으로만 이루어져 있습니다.
		 */
		
		boolean answer = true;
		        
		int p = 0;
		int y = 0;
		
		for(int i = 0; i < s.length(); i++) {
			if (s.charAt(i) == 'p' || s.charAt(i) == 'P') {
					p++;
			}
			if (s.charAt(i) == 'y' || s.charAt(i) == 'Y') {
					y++;
			}
		}
		
		if(p == y){
			
			return true;
			
		} else {
			
		    return false;
		}
		 
	}
	
	
	// 01.28
	public String solution2(String[] seoul) {
		String answer = "";
	    for(int x = 0; x < seoul.length; x++){
	    	if(seoul[x].equals("Kim")){
	    		answer = "김서방은 " + x + "에 있다";    
	        }
	    }
	    return answer;
	}
	
	
	public String solution3(String phone_number) {
		String answer = "";
	    char[] ch = phone_number.toCharArray();
	        
	    for(int i = 0; i < ch.length - 4; i++){
	    	ch[i] = '*';
	    }
	        
	    for(int i = 0; i < ch.length ; i++){
	    	answer += ch[i];
	    }
	    return answer;
	}
	//toCharArray() / substring() --> 공부하기
	
	
	public double solution(int[] arr) {
        double answer = 0;
        
        for(int i = 0; i < arr.length; i++){
            answer += arr[i];            
        }
        answer /= arr.length;
        return answer;
    }



	// 01.29
	
	public String solution(int num) {
        
        if (num % 2 == 0){
            return "Even";
        }else {
            return "Odd";
        }
        
        // return num % 2 == 0 ? "Even": "Odd";
    }
	
	
	public int solution2(int n) {
        int answer = 0;
        
        for(int i = 1; i <= n; i ++){
            if(n % i == 0){
                answer += i;
            }   
        }
        return answer;
    }
	
	//못풀겠다.. 자릿수더하기
	public int solution3(int n) {
		int answer = 0;
		String s = String.valueOf(n);
        int[] arr = new int[s.length()];
     
        
        for(int i = 0; i < s.length(); i++){
            arr[i] = (int)s.charAt(i);
            answer += arr[i];
        }
     return answer;
     
     // 연동 test

	}



}
