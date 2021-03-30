/*
 * Having a good previous year, Monk is back to teach algorithms and data 
 * structures. This year he welcomes the learners with a problem which he calls 
 * "Welcome Problem". The problem gives you two arrays A and B (each array of 
 * size N) and asks to print new array C such that:
 * C[i] = A[i] + B[i]; 1 ≤ i ≤ N
 * Now, Monk will proceed further when you solve this one. So, go on and solve 
 * it :)

 * Input:
 * First line consists of an integer N, denoting the size of A and B.
 * Next line consists of N space separated integers denoting the array A.
 * Next line consists of N space separated integers denoting the array B.

 * Output:
 * Print N space separated integers denoting the array C.

 * Input Constraints:
 * 1 ≤ N ≤ 100000
 * 1 ≤ A[i] ≤ 100000; 1 ≤ i ≤ N 
 * 1 ≤ B[i] ≤ 100000; 1 ≤ i ≤ N 
 */
package DataStructures.Arrays1D;

import java.io.*;
import java.util.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 20/09/2017
 */
public class MonkAndWelcomeProblem {

    /**
     * @param args the command line arguments
     * @throws java.io.FileNotFoundException
     */
    public static void main(String[] args) throws FileNotFoundException {
        // All code application logic here
        File f = new File("input.txt");
        Scanner in = new Scanner(System.in);

        int N = in.nextInt();

        int[] A = new int[N];
        int[] B = new int[N];

        for (int i = 0; i < N; i++) {
            A[i] = in.nextInt();
        }

        for (int i = 0; i < N; i++) {
            B[i] = in.nextInt();
            System.out.print(A[i] + B[i] + " ");
        }
    }
}
