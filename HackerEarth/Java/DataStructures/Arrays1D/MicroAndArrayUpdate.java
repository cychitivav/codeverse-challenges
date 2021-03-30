/*
 * Micro purchased an array A having N integer values. After playing it for a while, he got bored
 * of it and decided to update value of its element. In one second he can increase value of each
 * array element by 1. He wants each array element's value to become greater than or equal to 
 * K. Please help Micro to find out the minimum amount of time it will take, for him to do so.

 * Input: 
 * - First line consists of a single integer, T, denoting the number of test cases. 
 * - First line of each test case consists of two space separated integers denoting N and K. 
 * - Second line of each test case consists of N space separated integers denoting the array A.

 * Output:
 * - For each test case, print the minimum time in which all array elements will become 
 * greater than or equal to K. Print a new line after each test case.

 * Constraints: 
 * 1 ? T ? 5
 * 1 ? N ? 10^5 
 * 1 ? A[i], K ? 10^6
 */
package DataStructures.Arrays1D;

import java.io.*;
import java.util.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 18/09/2017
 */
public class MicroAndArrayUpdate {

    /**
     * @param args the command line arguments
     * @throws java.io.FileNotFoundException
     */
    public static void main(String[] args) throws FileNotFoundException {
        // All code application logic here
        File f = new File("input.txt");
        Scanner in = new Scanner(System.in);

        int T = in.nextInt();

        for (; T > 0; T--) {
            int N = in.nextInt();
            int K = in.nextInt();

            int[] A = new int[N];

            int C = 0;

            for (int i = 0; i < N; i++) {
                A[i] = in.nextInt() + C;
                if (A[i] < K) {
                    C += (K - A[i]);
                    A[i] += C;
                }
            }
            System.out.println(C);
        }
    }
}
