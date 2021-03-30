/*
 * Given two strings of equal length, you have to tell whether they both strings 
 * are identical.
 * Two strings S1 and S2 are said to be identical, if any of the permutation of 
 * string S1 is equal to the string S2. See Sample explanation for more details.
 * 
 * Input :
 * First line, contains an intger 'T' denoting no. of test cases.
 * Each test consists of a single line, containing two space separated strings 
 * S1 and S2 of equal length.
 * 
 * Output:
 * For each test case, if any of the permutation of string S1 is equal to the 
 * string S2 print YES else print NO.
 * 
 * Constraints:
 * 1 ≤ T ≤ 100
 * 1 ≤ |S1| = |S2| ≤ 10^5
 * String is made up of lower case letters only.
 * 
 * Note : Use Hashing Concept Only . Try to do it in O(string length) .
 */
package BasicsProgramming.InputOutput;

import java.io.*;
import java.util.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 29/10/2017
 */
public class TwoStrings {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // All code application logic here
        File f = new File("input.txt");
        Scanner in = new Scanner(System.in);

        int T = in.nextInt();

        while (T > 0) {
            T--;
            char[] S1 = in.next().toCharArray();
            char[] S2 = in.next().toCharArray();

            int count = 0;

            for (int i = 0; i < S1.length; i++) {
                for (int j = 0; j < S2.length; j++) {
                    if (S1[i] == S2[j]) {
                        S2[j] = 0;
                        count++;
                        break;
                    }
                }
                if (count <= i) {
                    break;
                }
            }
            if (count == S1.length) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }

}
