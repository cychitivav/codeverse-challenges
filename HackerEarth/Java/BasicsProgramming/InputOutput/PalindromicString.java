/*
 * You have been given a String S. You need to find and print whether this 
 * string is a palindrome or not. If yes, print "YES" (without quotes), else 
 * print "NO" (without quotes).
 * 
 * Input Format
 * The first and only line of input contains the String S. The String shall 
 * consist of lowercase English alphabets only.
 * 
 * Output Format
 * Print the required answer on a single line.
 * 
 * Constraints 
 * 1 ≤ |S| ≤ 100
 * 
 * Note
 * String S consists of lowercase English Alphabets only.
 */
package BasicsProgramming.InputOutput;

import java.util.*;
import java.io.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 18/11/2017
 */
public class PalindromicString {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // All code application logic here
        File f = new File("");
        Scanner in = new Scanner(System.in);

        char[] S = in.next().toCharArray();

        for (int i = 0, j = S.length - 1; i != j;) {
            if (S[i] != S[j]) {
                System.out.println("NO");
                return;
            }
            j--;
            if (j == i) {
                break;
            }
            i++;
        }
        System.out.println("YES");
    }

}
