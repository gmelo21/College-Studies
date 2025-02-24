package br.com.fiap;

import java.util.Scanner;

public class TriangleCalculator {
    public static void main(String[] args) {
        float base = 0, height = 0;
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Enter the base of the triangle: ");
            base = scanner.nextFloat();
            System.out.print("Enter the height of the triangle: ");
            height = scanner.nextFloat();
            System.out.println("The area of the triangle is: " + ((base * height) / 2));
        }
        catch (Exception e) {
            throw new RuntimeException("Number format invalid.");
        }

    }
}
