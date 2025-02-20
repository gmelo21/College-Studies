package br.com.fiap;

public class Operators {
    public static void main(String[] args) {
        int num1 = 10;
        int num2 = 5;
        double num3 = 12.5;
        double num4 = 4.5;
        long num5 = 100000L;
        float num6 = 3.14f;

        int sum = num1 + num2;
        int subtraction = num1 - num2;
        int multiplication = num1 * num2;
        double division = num3 / num4;
        long longMultiplication = num5 * num2;
        float floatSum = num6 + (float) num3;

        System.out.println("Results of the operations: \n" +
                "Sum (num1 + num2): " + num1 + " + " + num2 + " = " + sum + "\n" +
                "Subtraction (num1 - num2): " + num1 + " - " + num2 + " = " + subtraction + "\n" +
                "Multiplication (num1 * num2): " + num1 + " * " + num2 + " = " + multiplication + "\n" +
                "Division (num3 / num4): " + num3 + " / " + num4 + " = " + String.format("%.2f", division) + "\n" +
                "Long Multiplication (num5 * num2): " + num5 + " * " + num2 + " = " + longMultiplication + "\n" +
                "Sum with Float (num6 + num3): " + num6 + " + " + num3 + " = " + String.format("%.2f", floatSum));
    }
}