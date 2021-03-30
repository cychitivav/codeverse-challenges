/*
 * Some problems appear hard though they are very easy. Today Aakash is stuck in 
 * a range query problem. He has been given an array with only numbers 0 and 1. 
 * There are two types of queries -

 * 0 L R : Check whether the number formed from the array elements L to R is 
 * even or odd and print EVEN or ODD respectively. Number formation is the
 * binary number from the bits status in the array L to R

 * 1 X : Flip the Xth bit in the array 

 * Indexing is 1 based

 * Input
 * First line contains a number N and Q as input. Next line contains N space 
 * separated 0 or 1. Next Q lines contain description of each query 

 * Output
 * Output for only query type 0 L R whether the number in range L to R is "EVEN" 
 * or "ODD" (without quotes).

 * Constraints
 * 1 ≤ N ≤ 10^6 
 * 1 ≤ L ≤ R ≤ 10^6 
 * 1 ≤ Q ≤ 10^6
 * 1 ≤ X ≤ N
 */
package DataStructures.Arrays1D;

import java.util.*;
import java.io.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 26/09/2017
 */
public class BinaryQueries {

    /**
     * @param args the command line arguments
     * @throws java.io.FileNotFoundException
     */
    public static void main(String[] args) throws FileNotFoundException {
        // All code application logic here
        File f = new File("input.txt");
        Scanner in = new Scanner(System.in);

        int N = in.nextInt();
        int Q = in.nextInt();

        int[] A = new int[N];

        for (int i = 0; i < A.length; i++) {
            A[i] = in.nextInt();
        }

        while (Q > 0) {
            int Ans = in.nextInt();

            if (Ans == 1) {
                int X = in.nextInt();

                if (A[X - 1] == 1) {
                    A[X - 1] = 0;
                } else {
                    A[X - 1] = 1;
                }
            } else {
                int L = in.nextInt();
                int R = in.nextInt();

                if (A[R - 1] == 1) {
                    System.out.println("ODD");
                } else {
                    System.out.println("EVEN");
                }
            }
            Q--;
        }
    }
}
