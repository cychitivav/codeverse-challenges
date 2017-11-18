/*
 * You have been given 3 integers - l, r and k. Find how many numbers between l 
 * and r (both inclusive) are divisible by k. You do not need to print these 
 * numbers, you just have to find their count.
 * 
 * Input Format
 * The first and only line of input contains 3 space separated integers l, r and
 * k.
 * 
 * Output Format
 * Print the required answer on a single line.
 * 
 * Constraints
 * 1 ≤ l ≤ r ≤ 1000 
 * 1 ≤ k ≤ 1000
 */
package BasicsProgramming.InputOutput;

import java.util.*;
import java.io.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 29/10/2017
 */
public class CountDivisors {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // All code application logic here
        File f = new File("input.txt");
        Scanner in = new Scanner(System.in);

        int l = in.nextInt();
        int r = in.nextInt();
        int k = in.nextInt();

        int count = 0;

        for (; l <= r; l++) {
            if (l % k == 0) {
                count++;
            }
        }
        System.out.println(count);
    }

}
