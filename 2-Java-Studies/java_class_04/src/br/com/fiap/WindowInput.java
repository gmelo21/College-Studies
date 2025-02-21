package br.com.fiap;

import javax.swing.*;

public class WindowInput {
    public static void main(String[] args) {
        int num1 = 0, num2 = 0, result = 0;
        String auxiliar;

        try {
            auxiliar = JOptionPane.showInputDialog("Type one (whole) number:");
            num1 = Integer.parseInt(auxiliar);
            auxiliar = JOptionPane.showInputDialog("Type another (whole) number:");
            num2 = Integer.parseInt(auxiliar);
            result = num1 + num2;
            JOptionPane.showMessageDialog(null, "Sum of both numbers: " + result);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Number format invalid.");
        }
    }
}
