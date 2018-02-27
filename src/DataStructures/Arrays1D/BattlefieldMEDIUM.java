/*
 * The war goes on.The Knights and the Demons are fighting at their fullest but 
 * as expected, the evil is dominating the good ones.In order to defeat the 
 * Demons the knights have to come together.
 * Initially everyone is standing in a circular path at the top of the Demon 
 * tower. The warrior at index 1 is standing next to warrior at index n and 
 * before the warrior at index 2.In order to win the fight the knights have to 
 * come together.
 * The knights have a special power through which they can swap them self with 
 * anyone. 
 * Help the Knights decide the minimum number of swaps they have to do so that 
 * all of them stand together. 

 * Input
 * The first line of the input contains t (the number of test cases).
 * The next 2*t line contains the following:
 * The first line contains n (the size of string).
 * The next line contains the string s.
 * The ith character denotes if there is a Knight (K) or a Demon (D).

 * Output
 * The output contains an integer denoting the minimum number of swaps required
 * for each test case t.
 
 * Constraints 
 * 1 ≤ t ≤ 100
 * 1 ≤ n ≤ 10^5
 */
package DataStructures.Arrays1D;

import java.util.*;
import java.io.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 27/02/2018
 */
public class BattlefieldMEDIUM {

    /**
     * @param args the command line arguments
     * @throws java.io.FileNotFoundException
     */
    public static void main(String[] args) throws FileNotFoundException {
        // All code application logic here
        File f = new File("input.txt");
        Scanner in = new Scanner(f);

        int T = in.nextInt();
        int N;
        int M;

        while (T > 0) {
            N = in.nextInt();
            M = in.nextInt();

            if (M % N == 0) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }

            T--;
        }
    }
}
