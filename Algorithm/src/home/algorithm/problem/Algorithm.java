package home.algorithm.problem;


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
		
		
	

}
