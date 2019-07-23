/*
Input : [] -> non empty | distinct | int, target_sum  
Output: (a,b) from [] which sum upto target | a <= b

Input data types : int Array, int 

Mathematical equation : 
a + b = t
a = t - b

Solutions:
1. Brute Force -> time: O(n^2) | space : O(1)
2. HashMap -> time : O(n) | space : O(n)
3. Sort and Two pointer -> time : O(nlogn) | space : O(1)
4. Sort and Binary Search -> time : O(nlogn) | space : O(1) or O(log n)
*/

import java.io.*;
import java.util.*;

class Program {
  public static int[] twoNumberSum(int[] array, int targetSum) {
		Arrays.sort(array);
		// now array is sorted
		for (int i = 0; i < array.length - 1; i++){
			int elementOne = array[i];
			int toFind = targetSum - elementOne;
			int first = i + 1;
			int last = array.length - 1;
			while (first <= last){
				int mid = (first + last) / 2;
				// three conditions 
				// condition 1: element found
				if ( array[mid] == toFind ){
					int [] elements = {elementOne, array[mid]};
					return elements;
				} 
				// condition 2: array[mid] > toFind | toFind in left half
				else if (array[mid] > toFind ){
					last = mid - 1;
				}
				// condition 2: array[mid] < toFind | toFind in right half
				else{
					first = mid + 1;
				}
		}
		}
		
		return new int[0];		
  }
}
