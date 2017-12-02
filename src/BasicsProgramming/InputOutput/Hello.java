/*
 * Kirti is new to programming and she doesn't know how to code. Can you write a
 * code, which would print "Hello Kirti" on the screen.
 */
package BasicsProgramming.InputOutput;

import java.io.*;
import java.util.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 2/12/2017
 */
public class Hello {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // All code application logic here
        File f = new File("input.txt");
        Scanner in = new Scanner(System.in);

        System.out.println("Hello Kirti");
    }

}
