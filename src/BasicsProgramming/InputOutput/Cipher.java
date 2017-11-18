/*
 * Indian army is going to do a surprise attack on one of its enemies country. 
 * The President of India, the Supreme Commander of the Indian Army will be 
 * sending an alert message to all its commanding centers. As enemy would be 
 * monitoring the message, Indian army is going to encrypt(cipher) the message 
 * using basic encryption technique. A decoding key 'K' (number) would be sent 
 * secretly.
 * You are assigned to develop a cipher program to encrypt the message. Your 
 * cipher must rotate every character in the message by a fixed number making it 
 * unreadable by enemies.
 * Given a single line of string 'S' containing alpha, numeric and symbols, 
 * followed by a number '0<=N<=1000'. Encrypt and print the resulting string.
 * 
 * Note: The cipher only encrypts Alpha and Numeric. (A-Z, a-z, and 0-9) . All 
 * Symbols, such as - , ; %, remain unencrypted.
 * 
 * Explanation
 * First line contains the string to convert. S Second line contains the number, 
 * encrypt key. K
 */
package BasicsProgramming.InputOutput;

import java.util.*;
import java.io.*;

/**
 * @author Cristian Chitiva
 * @email cychitivav@unal.edu.co
 * @since 30/10/2017
 */
public class Cipher {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // All code application logic here
        File f = new File("input.txt");
        Scanner in = new Scanner(System.in);
        
        char[] S = in.next().toCharArray();
        int K = in.nextInt();

        for (int i = 0; i < S.length; i++) {
            if (S[i] > 47 && S[i] < 58) {
                S[i] -= 47;
                S[i] = (char) ((S[i] + K) % 10 + 47);
            } else if (S[i] > 64 && S[i] < 91) {
                S[i] -= 64;
                S[i] = (char) ((S[i] + K) % 26 + 64);
            } else if (S[i] > 96 && S[i] < 123) {
                S[i] -= 96;
                S[i] = (char) ((S[i] + K) % 26 + 96);
            }
        }
        System.out.println(S);
    }

}
