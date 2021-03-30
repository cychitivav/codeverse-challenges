/*
 * Akash and Vishal are quite fond of travelling. They mostly travel by railways.
 * They were travelling in a train one day and they got interested in the 
 * seating arrangement of their compartment. The compartment looked something 
 * like 
 * So they got interested to know the seat number facing them and the seat type 
 * facing them. The seats are denoted as follows : 
 * 
 * - Window Seat : WS
 * - Middle Seat : MS
 * - Aisle Seat : AS
 * 
 * You will be given a seat number, find out the seat number facing you and the 
 * seat type, i.e. WS, MS or AS.
 * 
 * INPUT
 * First line of input will consist of a single integer T denoting number of 
 * test-cases. Each test-case consists of a single integer N denoting the 
 * seat-number.
 * 
 * OUTPUT
 * For each test case, print the facing seat-number and the seat-type, separated 
 * by a single space in a new line.
 * 
 * CONSTRAINTS
 * 1 ≤ T ≤ 10^5
 * 1 ≤ N ≤ 108
 */
package BasicsProgramming.InputOutput;

import java.io.*;
import java.util.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 29/10/2017
 */
public class SeatingArrangement {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // All code application logic here
        File f = new File("input.txt");
        Scanner in = new Scanner(System.in);

        int T = in.nextInt();
        int N;

        int seat;

        while (T > 0) {
            N = in.nextInt();

            seat = 13 - ((N % 12 != 0) ? (N % 12) : 12);
            System.out.print((12 * ((N - 1) / 12)) + seat + " ");

            switch ((N - 1) % 6) {
                case 0:
                case 5:
                    System.out.println("WS");
                    break;
                case 1:
                case 4:
                    System.out.println("MS");
                    break;
                case 2:
                case 3:
                    System.out.println("AS");
                    break;
            }
            T--;
        }
    }

}
