/*
 * Arijit is a brilliant boy. He likes memory games. He likes to participate 
 * alone but this time he has to have a partner. So he chooses you.
 * In this Game , your team will be shown N numbers for few minutes . You will 
 * have to memorize these numbers.
 * Now, the questioner will ask you Q queries, in each query He will give you a 
 * number , and you have to tell him the total number of occurrences of that 
 * number in the array of numbers shown to your team . If the number is not 
 * present , then you will have to say “NOT PRESENT” (without quotes).

 * INPUT And OUTPUT
 * The first line of input will contain N, an integer, which is the total number 
 * of numbers shown to your team.
 * The second line of input contains N space separated integers .
 * The third line of input contains an integer Q , denoting the total number of 
 * integers.
 * The Next Q lines will contain an integer denoting an integer, Bi , for which 
 * you have to print the number of occurrences of that number (Bi) in those N 
 * numbers on a new line.
 * If the number Bi isn’t present then Print “NOT PRESENT” (without quotes) on a 
 * new line.

 * CONSTRAINTS
 * 1 ≤ N ≤ 10^5
 * 0 ≤ Bi ≤ 1000
 * 1 ≤ Q ≤ 10^5
 */
package DataStructures.Arrays1D;

import java.util.*;
import java.io.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 27/02/2018
 */
public class MemoriseMe {

    /**
     * @param args the command line arguments
     * @throws java.io.FileNotFoundException
     */
    public static void main(String[] args) throws FileNotFoundException {
        // All code application logic here
        File f = new File("input.txt");
        Scanner in = new Scanner(f);

        short N = in.nextShort();

        short[] B = new short[N];
        for (short i = 0; i < N; i++) {
            B[i] = in.nextShort();
        }

        short Q = in.nextShort();

        while (Q > 0) {
            short Bi = in.nextShort();
            short count = 0;

            for (short i = 0; i < N; i++) {
                if (B[i] == Bi) {
                    count++;
                }
            }
            if (count > 0) {
                System.out.println(count);
            } else {
                System.out.println("NOT PRESENT");
            }
            Q--;
        }
    }
}
