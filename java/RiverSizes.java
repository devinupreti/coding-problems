import java.util.ArrayList;

/*
River Sizes
int[][] -> ArrayList<Integer>

// need to visit everynode
// if 1 -> DFS on all possibilities
*/

class RiverSizes {
	public static int traverse(int[][] matrix, int row, int col){
		if (row< 0 || row >= matrix.length || col < 0 || col >= matrix[0].length)
		{ return 0; }
		
		if (matrix[row][col] == 0) { return 0; }
		
		// mark current to 0
		int currentSize = 1;
		matrix[row][col] = 0;
		
		currentSize += traverse(matrix, row+1, col);
		currentSize += traverse(matrix, row-1, col);
		currentSize += traverse(matrix, row, col+1);
		currentSize += traverse(matrix, row, col-1);
		return currentSize;	
	}
	
  public static ArrayList<Integer> riverSizes(int[][] matrix) {
    ArrayList<Integer> sizes = new ArrayList<Integer>();
		
		for (int row = 0; row < matrix.length; row++) {
			for(int col = 0; col < matrix[row].length; col++){
				if (matrix[row][col] == 1) {
					sizes.add(traverse(matrix, row, col));
				}
			}
		}
		return sizes;
  }
}
