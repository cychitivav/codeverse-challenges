/*
 * Your program is to use the brute-force approach in order to find the Answer 
 * to Life, the Universe, and Everything. More precisely... rewrite small numbers 
 * from input to output. Stop processing input after reading in the number 42. 
 * All numbers at input are integers of one or two digits.
 */
package BasicsProgramming.InputOutput;

import java.util.*;
import java.io.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 30/10/2017
 */
public class LifeTheUniverseAndEverything {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // All code application logic here
        //File f = new File("");
        Scanner in = new Scanner(System.in);

        short N = in.nextShort();

        while (N != 42) {
            System.out.println(N);
            N = in.nextShort();
        }
        in.close();

    }

}
