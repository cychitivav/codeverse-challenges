/*
 * You are given an array of n numbers and q queries. For each query you have to 
 * print the floor of the expected value(mean) of the subarray from L to R.
 * 
 * Input:
 * First line contains two integers N and Q denoting number of array elements 
 * and number of queries.
 * Next line contains N space seperated integers denoting array elements.
 * Next Q lines contain two integers L and R(indices of the array).
 * 
 * Output:
 * print a single integer denoting the answer.
 * 
 * Constraints :
 * 1 ≤ N,Q,L,R ≤ 10^6
 * 1 ≤ Array elements ≤ 10^9
 */
package BasicsProgramming.InputOutput;

import java.io.*;
import java.util.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 30/10/2017
 */
public class PlayWithNumbers {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // All code application logic here
        File f = new File("input.txt");
        Scanner in = new Scanner(System.in);

        int N = in.nextInt();
        int Q = in.nextInt();

        int[] A = new int[N];

        for (int i = 0; i < N; i++) {
            A[i] = in.nextInt();
        }

        int L = 1;
        int R = 1;
        long mean = 0;

        while (Q > 0) {
            mean = 0;
            L = in.nextInt();
            R = in.nextInt();

            for (int i = L; i <= R; i++) {
                mean += A[i - 1];
            }
            System.out.println(mean / (R - L + 1));
            Q--;
        }
    }

}
