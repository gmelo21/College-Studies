package br.com.fiap;

import java.util.Scanner;

public class SingleLotteryV1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        byte chosenNum;
        byte winnerNum = 45;
        String answer = "yes";

        System.out.println("Welcome!");
        System.out.println("100 numbers. One winner. Ninety-nine losers. Can you guess the right one?");

        while(answer.equalsIgnoreCase("yes")) {
            System.out.println("Chose a number from 1 to 100: ");

            chosenNum = scanner.nextByte();

            if (chosenNum == winnerNum) {
                System.out.println("You win!");
            } else {
                System.out.println("You lose.");
            }

            System.out.println("Would you like to play again? (yes/no) ");

            answer = scanner.next();

            System.out.println("The end.");
        }
    }
}
