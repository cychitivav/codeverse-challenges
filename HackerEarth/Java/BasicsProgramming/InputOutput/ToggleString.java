/*
 * You have been given a String S consisting of uppercase and lowercase English 
 * alphabets. You need to change the case of each alphabet in this String. That 
 * is, all the uppercase letters should be converted to lowercase and all the 
 * lowercase letters should be converted to uppercase. You need to then print 
 * the resultant String to output.
 * 
 * Input Format
 * The first and only line of input contains the String S
 * 
 * Output Format
 * Print the resultant String on a single line.
 * 
 * Constraints
 * 1 ≤ |S| ≤ 100 where |S| denotes the length of string S.
 */
package BasicsProgramming.InputOutput;

import java.io.*;
import java.util.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 29/10/2017
 */
public class ToggleString {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // All code application logic here
        File f = new File("input.txt");
        Scanner in = new Scanner(System.in);

        char[] S = in.next().toCharArray();

        for (int i = 0; i < S.length; i++) {
            if (S[i] < 91) {
                S[i] += 32;
            } else {
                S[i] -= 32;
            }
        }
        System.out.print(S);
    }

}
