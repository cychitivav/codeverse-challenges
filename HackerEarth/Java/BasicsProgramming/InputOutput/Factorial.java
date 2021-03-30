/*
 * You have been given a positive integer N. You need to find and print the
 * Factorial of this number. The Factorial of a positive integer N refers to the 
 * product of all number in the range from 1 to N. You can read more about the
 * factorial of a number here.
 * 
 * Input Format:
 * The first and only line of the input contains a single integer N denoting the
 * number whose factorial you need to find.
 * 
 * Output Format
 * Output a single line denoting the factorial of the number N.
 * 
 * Constraints
 * 1 ≤ N ≤ 10
 */
//package BasicsProgramming.InputOutput;

import java.util.*;
import java.io.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 29/10/2017
 */
public class Factorial {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // All code application logic here
        File f = new File("");
        Scanner in = new Scanner(System.in);

        int N = in.nextInt();
        System.out.println(factorial(N));
    }

    public static int factorial(int N) {

        if (N == 1) {
            return 1;
        }

        return N * factorial(N - 1);
    }
}
