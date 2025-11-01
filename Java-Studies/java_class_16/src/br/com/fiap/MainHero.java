package br.com.fiap;

import javax.swing.*;
import java.util.ArrayList;

public class MainHero {
    public static void main(String[] args) {
        boolean keep = true;
        while (keep) {
            String name = JOptionPane.showInputDialog("Enter the hero name:");
            String secretIdentity = JOptionPane.showInputDialog("Enter the secret identity:");
            ArrayList<String> powers = new ArrayList<>();
            ArrayList<String> weaknesses = new ArrayList<>();

            while (true) {
                String power = JOptionPane.showInputDialog("Enter a power (or type 'end' to stop):");
                if (power.equalsIgnoreCase("end")) break;
                powers.add(power);
            }

            while (true) {
                String weakness = JOptionPane.showInputDialog("Enter a weakness (or type 'end' to stop):");
                if (weakness.equalsIgnoreCase("end")) break;
                weaknesses.add(weakness);
            }

            Hero hero = new Hero(name, secretIdentity, powers, weaknesses);
            hero.listHero();
            int option = JOptionPane.showConfirmDialog(null, "Do you want to continue?", "Continue", JOptionPane.YES_NO_OPTION);
            if (option == JOptionPane.NO_OPTION) {
                JOptionPane.showMessageDialog(null, "Goodbye!");
                keep = false;
            }
        }
    }
}
