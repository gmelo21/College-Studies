package br.com.fiap;

import javax.swing.JOptionPane;

public class AgeCalculator {
    public static void main(String[] args) {
        int currentYear = Integer.parseInt(JOptionPane.showInputDialog("Enter the current year:"));
        int currentMonth = Integer.parseInt(JOptionPane.showInputDialog("Enter the current month (1-12):"));
        int currentDay = Integer.parseInt(JOptionPane.showInputDialog("Enter the current day (1-31):"));

        int birthYear = Integer.parseInt(JOptionPane.showInputDialog("Enter your birth year:"));
        int birthMonth = Integer.parseInt(JOptionPane.showInputDialog("Enter your birth month (1-12):"));
        int birthDay = Integer.parseInt(JOptionPane.showInputDialog("Enter your birth day (1-31):"));

        int age = currentYear - birthYear;

        if (currentMonth < birthMonth || (currentMonth == birthMonth && currentDay < birthDay)) {
            age--;
        }

        JOptionPane.showMessageDialog(null, "Your age is: " + age);
    }
}
