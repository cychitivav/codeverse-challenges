/*
 * Given a character C, print the ASCII value of that character.
 * 
 * Input:
 * First and only line in input contains a character C.
 * 
 * Output:
 * Print the ASCII value of the character C.
 * 
 * Constraints:
 * C ∈ ASCII characters
 */
package BasicsProgramming.InputOutput;

import java.util.*;
import java.io.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 29/10/2017
 */
public class ASCIIValue {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // All code application logic here
        File f = new File("input.txt");
        Scanner in = new Scanner(System.in);

        char C = in.next().charAt(0);

        System.out.println((int) C);
    }

}
