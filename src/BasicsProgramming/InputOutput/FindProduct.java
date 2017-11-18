/*
 * You have been given an array A of size N consisting of positive integers. You 
 * need to find and print the product of all the number in this array Modulo 
 * 10^9 + 7.
 * 
 * Input Format:
 * The first line contains a single integer N denoting the size of the array. The 
 * next line contains N space separated integers denoting the elements of the array
 * 
 * Output Format:
 * Print a single integer denoting the product of all the elements of the array
 *  Modulo 10^9 + 7.
 * 
 * Constraints:
 * 1 ≤ N ≤ 10^3
 * 1 ≤ A[i] ≤ 10^3
 */
package BasicsProgramming.InputOutput;

import java.util.*;
import java.io.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 29/10/2017
 */
public class FindProduct {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // All code application logic here
        File f = new File("");
        Scanner in = new Scanner(System.in);

        int N = in.nextInt();

        long mult = 1;
        int A;

        for (int i = 0; i < N; i++) {
            A = in.nextInt();
            mult *= A;
            mult %= 1000000007;
        }

        System.out.println(mult);
    }

}
