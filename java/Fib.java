/*
Input: n
Output : nth fibonacci number

Solutions:
1. Recursion -> time : O(2^n) | space :(n)
2. Dynammic Programming -> time : O(n) | space : O(n)
3. Two variable -> time : O(n) | space : O(1)
*/

class Fib {
  public static int getNthFib(int n) {
    // Write your code here.
		int secondLast = 0;
		int last = 1;
		
		if ( n == 2 ) {return last; }
		
		int fib = 0;
		int current = 3;
		while (current <= n){
			fib = secondLast + last;
			secondLast = last;
			last = fib;
			current = current + 1;
		}
		return fib;
  }
}
