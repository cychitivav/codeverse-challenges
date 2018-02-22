/*
 * Mr. X's birthday is in next month. This time he is planning to invite N of 
 * his friends. He wants to distribute some chocolates to all of his friends  
 * after party. He went to a shop to buy a packet of chocolates.
 * At chocolate shop, each packet is having different number of chocolates. He 
 * wants to buy such a packet which contains number of chocolates, which can be  
 * distributed equally among all of his friends. 
 * Help Mr. X to buy such a packet.

 * Input: 
 * First line contains T, number of test cases. 
 * Each test case contains two integers, N and M. where is N is number of 
 * friends and M is number number of chocolates in a packet.

 * Output: 
 * In each test case output "Yes" if he can buy that packet and "No" if he can't
 * buy that packet.
 
 * Constraints:
 * 1 ≤ T ≤ 20
 * 1 ≤ N ≤ 100
 * 1 ≤ M ≤ 10^5
 */
package BasicsProgramming.Operators;

import java.util.*;
import java.io.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 22/02/2018
 */
public class BirthdayParty {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // All code application logic here
        File f = new File("input.txt");
        Scanner in = new Scanner(System.in);

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
