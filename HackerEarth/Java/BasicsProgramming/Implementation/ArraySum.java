/*
 * You are given an array of integers of size . You need to print the sum of the
 * elements in the array, keeping in mind that some of those integers may be 
 * quite large.

 * Input:
 * The first line of the input consists of an integer . The next line contains 
 * space-separated integers contained in the array.

 * Output:
 * Print a single value equal to the sum of the elements in the array.

 * Constraints:
 * 1 ≤ N ≤ 10
 * 0 ≤ a[i] ≤ 10^10
 */
package BasicsProgramming.Implementation;

import java.io.*;
import java.util.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 2/12/2017
 */
public class ArraySum {

    /**
     * @param args the command line arguments
     * @throws java.io.FileNotFoundException
     */
    public static void main(String[] args) throws FileNotFoundException {
        // All code application logic here
        File f = new File("input.txt");
        Scanner in = new Scanner(System.in);

        int N = in.nextInt();
        long sum = 0;

        for (int i = 0; i < N; i++) {
            sum += in.nextLong();
        }
        System.out.println(sum);
    }
}