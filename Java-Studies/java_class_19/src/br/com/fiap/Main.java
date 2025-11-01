package br.com.fiap;

import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Locale.setDefault(Locale.US);
        Scanner scanner = new Scanner(System.in);
        Calculator calc = new Calculator();
        boolean keepRunning = true;
        while (keepRunning) {
            Double a = null;
            Double b = null;
            while (a == null) {
                System.out.print("Enter the first real number: ");
                String s = scanner.nextLine().trim();
                try {
                    a = Double.parseDouble(s);
                } catch (NumberFormatException e) {
                    System.out.println("Invalid number. Try again.");
                }
            }
            while (b == null) {
                System.out.print("Enter the second real number: ");
                String s = scanner.nextLine().trim();
                try {
                    b = Double.parseDouble(s);
                } catch (NumberFormatException e) {
                    System.out.println("Invalid number. Try again.");
                }
            }
            calc.setNumberA(a);
            calc.setNumberB(b);
            String choice = null;
            while (choice == null) {
                System.out.println("Choose an operation:");
                System.out.println("1) Addition");
                System.out.println("2) Subtraction");
                System.out.println("3) Multiplication");
                System.out.println("4) Division");
                System.out.print("Your choice: ");
                String input = scanner.nextLine().trim();
                if (input.equals("1") || input.equalsIgnoreCase("addition") || input.equals("+")) {
                    choice = "ADD";
                } else if (input.equals("2") || input.equalsIgnoreCase("subtraction") || input.equals("-")) {
                    choice = "SUB";
                } else if (input.equals("3") || input.equalsIgnoreCase("multiplication") || input.equals("*")) {
                    choice = "MUL";
                } else if (input.equals("4") || input.equalsIgnoreCase("division") || input.equals("/")) {
                    choice = "DIV";
                } else {
                    System.out.println("Invalid option. Try again.");
                }
            }
            try {
                double result;
                switch (choice) {
                    case "ADD":
                        result = calc.add();
                        System.out.println("Result: " + result);
                        break;
                    case "SUB":
                        result = calc.subtract();
                        System.out.println("Result: " + result);
                        break;
                    case "MUL":
                        result = calc.multiply();
                        System.out.println("Result: " + result);
                        break;
                    default:
                        result = calc.divide();
                        System.out.println("Result: " + result);
                        break;
                }
            } catch (ArithmeticException ex) {
                System.out.println("Error: " + ex.getMessage());
            }
            String again = null;
            while (again == null) {
                System.out.print("Do you want to continue? (Y/N): ");
                String s = scanner.nextLine().trim();
                if (s.equalsIgnoreCase("Y") || s.equalsIgnoreCase("YES")) {
                    again = "Y";
                } else if (s.equalsIgnoreCase("N") || s.equalsIgnoreCase("NO")) {
                    again = "N";
                } else {
                    System.out.println("Please answer Y or N.");
                }
            }
            if (again.equals("N")) {
                keepRunning = false;
                System.out.println("Goodbye!");
            }
        }
        scanner.close();
    }
}

