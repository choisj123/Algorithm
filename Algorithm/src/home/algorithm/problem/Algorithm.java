package home.algorithm.problem;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Algorithm {

	/** 0312 숫자 비교하기
	 * @param num1
	 * @param num2
	 * @return answer
	 */
	public int solution(int num1, int num2) {
			
		int answer = 0;
		
		if (num1 == num2) {
			answer = 1;
		}else {
			answer = -1;
		}
		return answer;
		
		//int answer = (num1 == num2) ? 1 : -1;
		
	}
		
	
		// 0312 분수의 덧셈
	public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        
        int max = 0;
        
        for(int i = 1; i <= denom1 && i <= denom2; i++) {
        	if(denom1 % i == 0 && denom2 % i == 0) {
        		max = i;
        		
        	}
        }
        int min = (denom1 * denom2)/max; // 최소 공배수 
        int n1 = (numer1 * min /denom1) + (numer2 * min / denom2);
        
        int maxfin = 0;
        for(int i = 1; i <= n1 && i <= min; i++) {
        	if(n1 % i == 0 && min % i == 0) {
        		maxfin = i;
        		
        	}
        }
        
        int[] answer = {n1 /maxfin, min /maxfin};
        
        
       return answer ;
       
	}
		
		
    /** 0608 크기가 작은 부분문자
     * @param t
     * @param p
     * @return answer
     */
    public int solution(String t, String p) {
        int answer = 0;
        
        String[] tArr = t.split("");
        
        List<String> arrList = new ArrayList<>(Arrays.asList(tArr));
        
        List<String> tList = new ArrayList<>();
        
        System.out.println(Arrays.toString(tArr));
        String num = "";
        
//        for(int i = 0; i < p.length(); i++) {
//        	
//        	num += arrList.get(i);
//        	
//        	if(num.length() == p.length()) {
//        		
//        		System.out.println("num : " + num);
//        		arrList.remove(0);
//        		tList.add(num);
//        		num = "";
//        		
//        		System.out.println(arrList);
//        		
//        		
//        	} 	
//        	
//        }
        
//        System.out.println("tList:" + tList);
        
        int i = 0;
        
        // 어떻게 하지..
        while(true) {
        	
        	if(i==arrList.size()) break;
        	
        	num += arrList.get(i);
        	
        	if(num.length() == p.length()) {
        		
        		System.out.println("num : " + num);
        		arrList.remove(0);
        		tList.add(num);
        		num = "";
        		i -= p.length()+1;
        		
        		
        		System.out.println(arrList);
        	} 	
        	
        	i++;
        }
        
        System.out.println("tList:" + tList);
        
        for(String tt: tList) {
        	
        	if(Integer.parseInt(tt) <= Integer.parseInt(p)) {
        		
        		answer ++;
        	}
        	
        }
        
        
        return answer;
    }
	

}
