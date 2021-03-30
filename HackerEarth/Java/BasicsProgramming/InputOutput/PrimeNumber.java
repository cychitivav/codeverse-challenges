/*
 * You are given an integer N. You need to print the series of all prime numbers
 * till N.

 * Input Format
 * The first and only line of the input contains a single integer N denoting the 
 * number till where you need to find the series of prime number.
 
 * Output Format
 * Print the desired output in single line separated by spaces.
 
 * Constraints
 * 1 ≤ N ≤ 1000
 */
package BasicsProgramming.InputOutput;

import java.io.*;
import java.util.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 14/10/2017
 */
public class PrimeNumber {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // All code application logic here
        File f = new File("input.txt");
        Scanner in = new Scanner(System.in);

        int N = in.nextInt();

        boolean prime = true;

        for (int i = 2; i <= N; i++) {
            for (int j = 2; j < i; j++) {
                if ((i % j) == 0) {
                    prime = false;
                    break;
                }
            }
            if (prime == true) {
                System.out.print(i + " ");
            }
            prime = true;
        }
    }

}
