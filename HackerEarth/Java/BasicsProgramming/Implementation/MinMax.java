/*
 * Given an array of integers . Check if all the numbers between minimum and 
 * maximum number in array exist's within the array.
 * Print 'YES' if numbers exist otherwise print 'NO'(without quotes).

 * Input:
 * Integer N denoting size of array
 *  Next line contains N space separated integers denoting elements in array
 
 * Output:
 * Output your answer 

 * Constraints: 
 * 1 ≤ N ≤ 1000
 * 1 ≤ A[i] ≤ 100
 */
package BasicsProgramming.Implementation;

import java.io.*;
import java.util.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 4/12/2017
 */
public class MinMax {

    /**
     * @param args the command line arguments
     * @throws java.io.FileNotFoundException
     */
    public static void main(String[] args) throws FileNotFoundException {
        // All code application logic here
        File f = new File("input.txt");
        Scanner in = new Scanner(f);

        int N = in.nextInt();
        int max = 0;
        int min = 100;
        boolean contains = false;

        int[] A = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = in.nextInt();
            if (A[i] > max) {
                max = A[i];
            }
            if (A[i] < min) {
                min = A[i];
            }
        }

        for (int i = min + 1; i < max; i++) {
            for (int j = 0; j < N; j++) {
                if (A[j] == i) {
                    contains = true;
                }
            }
            if (!contains) {
                System.out.println("NO");
                return;
            }
            contains = false;
        }
        System.out.println("YES");
    }
}
