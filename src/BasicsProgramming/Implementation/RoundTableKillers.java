/*
 * There is a round table in which N people are sitting. You can look at the 
 * image for their seating arrangement. Initially the person numbered X holds a
 * gun. In addition to it there is a special number K that helps in determining 
 * the persons to be killed. The killing starts as follows - Firstly the person 
 * numbered X starts and he kills a total of X % K people sitting clockwise of 
 * him and he gives gun to the person i who is sitting just next to the last 
 * person killed. Now that person also kills the next i % K people and this goes
 * on. If at any instant the total persons that are remaining is not greater than 
 * i % K where i is the number of person holding the gun then the person i wins.
 * You can show that sooner or later only one person remains. So your job is to 
 * decide which numbered person will win this killing game.
 * X % K is the remainder when X is divided by K

 * Input
 * First line contains three numbers N, K and X as input.

 * Output 
 * In the output you have to tell the number of the player who will be the winner.

 * Constraints
 * 1 ≤ N ≤ 10^3
 * 2 ≤ K < N
 * 1 ≤ X ≤ N
 */
package BasicsProgramming.Implementation;

import java.io.*;
import java.util.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 2/12/2017
 */
public class RoundTableKillers {

    /**
     * @param args the command line arguments
     * @throws java.io.FileNotFoundException
     */
    public static void main(String[] args) throws FileNotFoundException {
        // All code application logic here
        File f = new File("input.txt");
        Scanner in = new Scanner(f);

        int N = in.nextInt();
        boolean[] P = new boolean[N];

        for (int i = 0; i < N; i++) {
            P[i] = true;
        }

        final int K = in.nextInt();
        int X = in.nextInt();

        while (true) {
            int D = X % K;
            int i = X;
            while (D > 0) {
                if (i >= N) {
                    i = 0;
                }
                if (P[i]) {
                    if (X == i + 1) {
                        System.out.println(X);
                        return;
                    }

                    P[i] = false;
                    D--;
                }
                i++;
            }
            if (i >= N) {
                i = 0;
            }
            while (!P[i]) {
                i++;
                if (i >= N) {
                    i = 0;
                }
            }

            X = i + 1;
        }
    }
}
