package br.com.fiap;

import javax.swing.*;

public class StringComparison {
    public static void main(String[] args) {
        String password = JOptionPane.showInputDialog("Choose your password: ");

        if (password.equals("AlfredTheButtler")) {
            JOptionPane.showMessageDialog(null, "Access accepted.");
        } else if (password.equalsIgnoreCase("AlfredTheButtler")) {
            JOptionPane.showMessageDialog(null, "Access accepted. (Casing incorrect)");
        }else {
            JOptionPane.showMessageDialog(null, "Access denied.");
        }
    }
}
