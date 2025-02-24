package br.com.fiap;

import javax.swing.*;

public class AmazingCalculator {
    public static void main(String[] args) {
        float a = 0, b = 0, c = 0;
        String auxiliar;

        try {
            JOptionPane.showMessageDialog(null, "Let's work with ax^2 + bx + c.");
            auxiliar = JOptionPane.showInputDialog("Enter A:");
            a = Float.parseFloat(auxiliar);
            auxiliar = JOptionPane.showInputDialog("Enter B:");
            b = Float.parseFloat(auxiliar);
            auxiliar = JOptionPane.showInputDialog("Enter C:");
            c = Float.parseFloat(auxiliar);

            auxiliar = JOptionPane.showInputDialog("Enter X (leave empty to solve for X using Y):");
            if (auxiliar == null || auxiliar.trim().isEmpty()) {
                auxiliar = JOptionPane.showInputDialog("Enter Y:");
                float y = Float.parseFloat(auxiliar);

                c = c - y;

                float discriminant = (b * b) - (4 * a * c);

                if (discriminant > 0) {
                    double x1 = (-b + Math.sqrt(discriminant)) / (2 * a);
                    double x2 = (-b - Math.sqrt(discriminant)) / (2 * a);
                    JOptionPane.showMessageDialog(null, "Two solutions: x1 = " + x1 + " and x2 = " + x2);
                } else if (discriminant == 0) {
                    double x = -b / (2 * a);
                    JOptionPane.showMessageDialog(null, "One solution: x = " + x);
                } else {
                    JOptionPane.showMessageDialog(null, "No real solutions.");
                }
            } else {
                float x = Float.parseFloat(auxiliar);
                JOptionPane.showMessageDialog(null, "Result: " + ((a * Math.pow(x, 2)) + (b * x) + c));
            }
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Number format invalid.");
        }
    }
}
