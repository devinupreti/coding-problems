import java.util.Arrays;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Stack;
import java.util.Queue;
import java.util.LinkedList;

class Solution {
  
  public static void testArrList() {
    int n = 5; 

    //declaring ArrayList with initial size n 
    ArrayList<Integer> arrli = new ArrayList<Integer>(); // [] created
    System.out.println(arrli); 

    for (int i=1; i<=n + 1; i++) 
        arrli.add(i); 
    
    System.out.println(arrli); 
    arrli.remove(3); 
    System.out.println(arrli); 
    
    for (int i=0; i<arrli.size(); i++) 
        System.out.print(arrli.get(i) +" "); 
  }
  
  public static void testHashMap(){
    HashMap<String, Integer> map = new HashMap<>(); 
          
    System.out.println(map);  
    map.put("vishal", 10); 
    map.put("sachin", 30); 
    map.put("vaibhav", 20); 

    System.out.println("Size of map is:- " + map.size()); 

    System.out.println(map);  
    if (map.containsKey("vishal"))  
    { 
      Integer a = map.get("vishal"); 
      System.out.println("value for key \"vishal\" is:- " + a); 
    } 

    map.clear(); 
    System.out.println(map); 
  }
  
  public static void testStack(){
    Stack<Integer> stack = new Stack<Integer>(); 
    
    stack.push(1);
    stack.push(2);
    stack.push(3);
    System.out.println(stack);
    Integer get = stack.pop();
    
    System.out.println(stack);
    System.out.println(get);
    System.out.println(stack.size());
    System.out.println(stack.isEmpty());   
  }
  
  public static void testQueue(){
    Queue<Integer> q = new LinkedList<>();
    q.add(1);
    q.add(2);
    int head = q.remove();
    int newHead = q.peek();
    System.out.println(q.size());
  }
  
  public static void main(String[] args){
    //testArrList();
    testHashMap();
  }
}


