package br.com.fiap;

import java.util.Scanner;

public class InputSubmission {
    public static void main(String[] args) {
        int num1 = 0, num2 = 0, result = 0;
        Scanner scan;

        try {
            scan = new Scanner(System.in);
            System.out.print("Type one (whole) number: ");
            num1 = scan.nextInt();
            System.out.print("Type another (whole) number: ");
            num2 = scan.nextInt();
            result = num1 + num2;
            System.out.println("Sum of both numbers: " + result);
        } catch (Exception e) {
            System.out.println("Number format invalid.");
        }
    }
}
