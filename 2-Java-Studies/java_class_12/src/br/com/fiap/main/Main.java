package br.com.fiap.main;

import br.com.fiap.bean.Adding;

import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        Adding add = new Adding();
        String aux, choice = "1";
        int option;
        int inum1, inum2;
        double dnum1, dnum2;

        while (choice.equalsIgnoreCase("1")) {
            try {
                aux = JOptionPane.showInputDialog("1 - Add two integers together.\n2 - Add two doubles together.");
                option = Integer.parseInt(aux);
                switch (option) {
                    case 1:
                        aux = JOptionPane.showInputDialog("Type the first number:");
                        inum1 = Integer.parseInt(aux);
                        aux = JOptionPane.showInputDialog("Type the second number:");
                        inum2 = Integer.parseInt(aux);
                        JOptionPane.showMessageDialog(null, (add.add(inum1, inum2)));
                        break;
                    case 2:
                        aux = JOptionPane.showInputDialog("Type the first number:");
                        dnum1 = Double.parseDouble(aux);
                        aux = JOptionPane.showInputDialog("Type the second number:");
                        dnum2 = Double.parseDouble(aux);
                        JOptionPane.showMessageDialog(null, (add.add(dnum1, dnum2)));
                        break;
                    default:
                        throw new Exception("Invalid choice.");
                }
                choice = JOptionPane.showInputDialog("Press 1 if you wish to re-run the program.");
            } catch (Exception e) {
                JOptionPane.showMessageDialog(null, e.getMessage());
            }
        }
        JOptionPane.showMessageDialog(null, "Come back anytime!");
    }
}
