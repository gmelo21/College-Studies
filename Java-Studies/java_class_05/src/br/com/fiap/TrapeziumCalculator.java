package br.com.fiap;

import javax.swing.*;

public class TrapeziumCalculator {
    public static void main(String[] args) {
        float base1 = 0, base2 = 0, height = 0;
        String auxiliar;

        try {
            auxiliar = JOptionPane.showInputDialog("Enter the size of base 1:");
            base1 = Integer.parseInt(auxiliar);
            auxiliar = JOptionPane.showInputDialog("Enter the size of base 2:");
            base2 = Integer.parseInt(auxiliar);
            auxiliar = JOptionPane.showInputDialog("Enter the height:");
            height = Integer.parseInt(auxiliar);
            JOptionPane.showMessageDialog(null, "Area of the trapezium: "
                    + ((base1 + base2) * height) / 2);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Number format invalid.");
        }
    }
}
