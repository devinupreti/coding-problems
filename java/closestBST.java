import java.util.*;
import java.io.*;
import java.lang.*;
/*
Input : BST head node -> left, right, value
Output: closest value to target

Solutions:
1. Recursive Traversal -> time : O(log n) | space : O(log n)
2. Iterative Traversal -> time : O(log n) | space : O(1)
at each node, check closer & move in that direction

*/

class Program {
  public static int findClosestValueInBst(BST tree, int target) {
		double closest = Double.MAX_VALUE;
		BST node = tree;
		while (node != null){
			if (Math.abs(target - node.value) < Math.abs(target - closest)){
				closest = node.value;
			}

			// compare
			if (target < node.value){
				node = node.left;
			}
			else if (target > node.value){
				node = node.right;
			}	
			else { break; }
		}
		return (int)closest;
  }

  static class BST {
    public int value;
    public BST left;
    public BST right;

    public BST(int value) {
      this.value = value;
    }
  }
}
