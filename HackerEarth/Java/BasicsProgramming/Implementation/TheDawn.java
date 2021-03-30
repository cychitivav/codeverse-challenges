/*
 * You are given a integer N denoting the multiplication of two numbers A and B. 
 * You have to find the minimum value of A+B for any integer A and B.
 * 
 * Constraints
 * 1 ≤ N ≤ 10^13
 */
package BasicsProgramming.Implementation;

import java.io.*;
import java.util.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 1/11/2017
 */
public class TheDawn {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws FileNotFoundException {
        // All code application logic here
        File f = new File("input.txt");
        Scanner in = new Scanner(f);

        long N = in.nextLong();

        long A = N;
        long B = 1;
        long sum = A + B;

        for (int i = 2; i < Math.sqrt(N); i++) {
            if (N % i == 0) {
                A = i;
                B = N / i;
                if (A + B < sum) {
                    sum = A + B;
                }
            }
        }
        System.out.println(sum);
    }
}