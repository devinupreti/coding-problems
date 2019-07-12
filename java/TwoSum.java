import java.io.*;
import java.util.*;

class TwoSum {
	// Solution 1 : Checking all possible combinations  
	// time : O(n^2) | space : O(1)
	public static int[] twoNumberSum(int[] array, int targetSum) {
		for (int i = 0; i < array.length - 1; i++){
			int firstNum = array[i];
			for (int j = i+1; j < array.length; j++){
				int secondNum = array[j];
				if (firstNum + secondNum == targetSum){
					return firstNum > secondNum ? new int[] {secondNum, firstNum} : new int[] {firstNum, secondNum};
				}
			}
		}
		return new int[0];
  	}

  	public static void main(String[] args){
  		int [] test = {1,2,3};
  		int targetSum = 5;
  		System.out.println(Arrays.toString(twoNumberSum(test, targetSum)));
  	}
}


