/*
 * Given two strings, a and b , that may or may not be of the same length, 
 * determine the minimum number of character deletions required to make a and b 
 * anagrams. Any characters can be deleted from either of the strings.
 * 
 * Input :
 * test cases,t
 * two strings a and b, for each test case
 * 
 * Output:
 * Desired O/p
 * 
 * Constraints :
 * string lengths ≤ 10000
 * 
 * Note :
 * Anagram of a word is formed by rearranging the letters of the word.
 * 
 * For e.g. -> For the word RAM - MAR,ARM,AMR,RMA etc. are few anagrams.
 */
package BasicsProgramming.InputOutput;

import java.util.*;
import java.io.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 29/10/2017
 */
public class Anagrams {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // All code application logic here
        File f = new File("input.txt");
        Scanner in = new Scanner(System.in);

        int T = in.nextInt();

        while (T > 0) {
            char[] A = in.next().toCharArray();
            char[] B = in.next().toCharArray();

            int equal = 0;

            for (int i = 0; i < A.length; i++) {
                for (int j = 0; j < B.length; j++) {
                    if (A[i] == B[j]) {
                        equal++;
                        B[j] = 0;
                        break;
                    }
                }
            }
            System.out.println(A.length + B.length - (2 * equal));
            T--;
        }
    }

}
