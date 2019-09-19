/*
Nth Fibonacci - 0, 1, 1, 2, 3, 5, 8, 13, ...
1. Recursive -> T: O(2^n) | S: O(n)
2. List -> T: O(n) | S: O(n)
3. Last two numbers in variables -> T : O(n) | S : O(1) 

*/

class Program {
	public static int solutionOne(int n){
		if (n < 2) { return 0; }
		else if (n == 2) { return 1; }
		else{
			return solutionOne(n-1) + solutionOne(n-2);
		}
	}
	
	public static int solutionTwo(int n){
		int[] array = new int[n];
		array[0] = 0;
		if (n < 2) { return 0; }
		
		array[1] = 1;
		int current = 2; // current = n - 1
		while(current < n){
			array[current] = array[current - 1] + array[current - 2];
			current++;
		}
		return array[n -1];
	}
	
	public static int solutionThree(int n){
		if (n < 2) { return 0; }
		if (n == 2) { return 1; }
		int last = 1;
		int second_last = 0;
		int current = 0;
		int count = 2;
		while (count < n){
			current = last + second_last;
			second_last = last;
			last = current;
			count += 1;
		}
		return current;
	}
	
  public static int getNthFib(int n) {
    //return solutionOne(n);
		//return solutionTwo(n);
		return solutionThree(n);
  }
}
