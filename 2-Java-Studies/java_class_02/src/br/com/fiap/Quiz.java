package br.com.fiap;

import java.util.Scanner;

public class Quiz {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int correctAnswers = 0;

        System.out.println("Starting the Dark Souls quiz.\n");

        System.out.println("Question 1: Who is the only character Patches has explicitly shown empathy for?");
        System.out.println("1. Eygon\n2. Greyrat\n3. Siegward\n4. Firekeeper");
        int answer = scanner.nextInt();

        if (answer == 2) {
            System.out.println("\nCorrect! Well done.");
            correctAnswers++;
        } else {
            System.out.println("\nWrong answer.");
        }

        System.out.println("\nQuestion 2: Which of these bosses does Siegward help you defeat in his questline?");
        System.out.println("1. Yhorm the Giant\n2. Champion Gundyr\n3. Dragonslayer Armor\n4. Dancer of the Boreal Valley");
        answer = scanner.nextInt();

        if (answer == 1) {
            System.out.println("\nCorrect! Well done.");
            correctAnswers++;
        } else {
            System.out.println("\nWrong answer.");
        }

        System.out.println("\nQuestion 3: Which of these bosses isn't optional?");
        System.out.println("1. Centipede Demon\n2. Demon Firesage\n3. Pinwheel\n4. Gaping Dragon");
        answer = scanner.nextInt();

        if (answer == 3) {
            System.out.println("\nCorrect! Well done.");
            correctAnswers++;
        } else {
            System.out.println("\nWrong answer.");
        }

        System.out.println("\nQuiz Completed!");
        System.out.println("Your score: " + correctAnswers + "/3");
        System.out.println("Praise the Sun!");

        scanner.close();
    }
}