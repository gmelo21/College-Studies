package br.com.fiap.main;

import br.com.fiap.bean.Geometry;

import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        Geometry geo = new Geometry();
        String auxiliar, choice = "yes";
        int option;
        float side, height;
        double radius;

        while (choice.equalsIgnoreCase("yes")) {
            try {
                auxiliar = JOptionPane.showInputDialog("Which area do you wish to calculate? \n(1) Square\n(2) Rectangle\n(3) Circle");
                option = Integer.parseInt(auxiliar);
                switch (option) {
                    case 1:
                        auxiliar = JOptionPane.showInputDialog("Choose the size of the side: ");
                        side = Float.parseFloat(auxiliar);
                        geo.calcArea(side);
                        break;
                    case 2:
                        auxiliar = JOptionPane.showInputDialog("Choose the size of the side: ");
                        side = Float.parseFloat(auxiliar);
                        auxiliar = JOptionPane.showInputDialog("Choose the size of the height: ");
                        height = Float.parseFloat(auxiliar);
                        geo.calcArea(side, height);
                        break;
                    case 3:
                        auxiliar = JOptionPane.showInputDialog("Choose the size of the radius: ");
                        radius = Float.parseFloat(auxiliar);
                        geo.calcArea(radius);
                        break;
                    default:
                        throw new Exception("Invalid choice.");
                }
                choice = JOptionPane.showInputDialog("Do you wish to continue? ");
            } catch (Exception e) {
                JOptionPane.showMessageDialog(null, e.getMessage());
            }
        }
        JOptionPane.showMessageDialog(null, "Program closed. Come back anytime!");
    }
}
