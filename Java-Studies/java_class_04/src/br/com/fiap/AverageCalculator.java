package br.com.fiap;

import java.util.Scanner;

public class AverageCalculator {
    public static void main(String[] args) {
        double exam1 = 0, exam2 = 0, exam3 = 0, exam4 = 0;
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Enter the score of Exam 1: ");
            exam1 = scanner.nextDouble();
            System.out.print("Enter the score of Exam 2: ");
            exam2 = scanner.nextDouble();
            System.out.print("Enter the score of Exam 3: ");
            exam3 = scanner.nextDouble();
            System.out.print("Enter the score of Exam 4: ");
            exam4 = scanner.nextDouble();
        } catch (Exception e) {
            throw new RuntimeException("Score format invalid.");
        }


        double average = (exam1 + exam2 + exam3 + exam4) / 4;
        System.out.println("The average score is: " + average);
    }
}

