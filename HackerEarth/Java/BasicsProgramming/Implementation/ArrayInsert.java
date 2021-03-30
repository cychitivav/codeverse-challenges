/*
 * Gary likes to solve problems of array, but he doesn't like problems that 
 * involve queries. His school teacher gave him an assignment full of problems 
 * but one of them involve queries. Can you help Gary in solving that problem so 
 * that he can go and play with his friends? The problem is :
 * Given an Array A consisting of N positive integers, you have to answer Q 
 * queries on it. Queries can be of the two types: * 1 X Y - Update X at 
 * location Y in the array. * 2 L R - Print the sum of range [L, R], i.e. Both 
 * L and R are inclusive.
 * 
 * Note:
 * Array indexing is from 0.
 * 
 * Input:
 * The first line contains two space separated integers N(Length of Array) and 
 * Q(Queries).
 * Next Line contains N space separated integers denoting array A.
 * Next Q Line contains 3 space separated integers for each line, as described 
 * above
 * 
 * Output: Answer to the each query of type 2 in a new line, only when range is 
 * valid, otherwise ouput `-1`
 * 
 * Constraints: 
 * 1 ≤ N ≤ 10^9 
 * 1 ≤ Q ≤ 10^5 
 * 1 ≤ A[i], X, Y, L, R ≤ 10^5
 */
package BasicsProgramming.Implementation;

import java.io.*;
import java.util.Scanner;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 1/11/2017
 */
public class ArrayInsert {

    /**
     * @param args the command line arguments
     * @throws java.io.FileNotFoundException
     */
    public static void main(String[] args) throws FileNotFoundException {
        // All code application logic here
        //File f = new File("input.txt");
        Scanner in = new Scanner(System.in);

        int N = in.nextInt();
        int Q = in.nextInt();

        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = in.nextInt();
        }

        int X, Y, sum;

        while (Q-- > 0) {
            X = in.nextInt();

            if (X == 1) {
                X = in.nextInt();
                Y = in.nextInt();

                A[X] = Y;
                X = 0;
            }
            if (X == 2) {
                X = in.nextInt();
                Y = in.nextInt();

                if (X <= Y) {
                    sum = 0;
                    while (X <= Y) {
                        sum += A[X];
                        X++;
                    }
                    System.out.println(sum);
                } else {
                    System.out.println(-1);
                }
            }
        }
        in.close();
    }
}