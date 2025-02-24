package br.com.fiap;

import java.util.Scanner;

public class RectangleCalculator {
    public static void main(String[] args) {
        float side = 0, height = 0;
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Enter the side of the rectangle: ");
            side = scanner.nextFloat();
            System.out.print("Enter the height of the rectangle: ");
            height = scanner.nextFloat();
            System.out.println("The area of the rectangle is: " + (side * height));
        }
        catch (Exception e) {
            throw new RuntimeException("Number format invalid.");
        }

    }
}
