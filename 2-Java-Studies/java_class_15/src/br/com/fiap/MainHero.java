package br.com.fiap;

import javax.swing.*;

public class MainHero {
    public static void main(String[] args) {
        Hero hero;
        String name;
        String secretId;
        String[] powers;
        String[] weaknesses;
        int quantityPowers;
        int quantityWeaknesses;

        do {
            try {
                name = JOptionPane.showInputDialog("Choose the Hero's name: ");
                secretId = JOptionPane.showInputDialog("Choose the Hero's secret identity's name: ");
                quantityPowers = Integer.parseInt(JOptionPane.showInputDialog("How many powers? "));
                quantityWeaknesses = Integer.parseInt(JOptionPane.showInputDialog("How many weaknesses? "));

                powers = new String[quantityPowers];
                for (int i = 0; i < powers.length; i++) {
                    powers[i] = JOptionPane.showInputDialog(String.format("Power %d: ", (i + 1)));
                }

                weaknesses = new String[quantityWeaknesses];
                for (int i = 0; i < weaknesses.length; i++) {
                    weaknesses[i] = JOptionPane.showInputDialog(String.format("Weaknesses %d: ", (i + 1)));
                }

                hero = new Hero(name, secretId, powers, weaknesses);
                hero.listHero();

            } catch (Exception e) {
                JOptionPane.showMessageDialog(null, e.getMessage(), "Error!", JOptionPane.ERROR_MESSAGE);
            }

        } while (JOptionPane.showConfirmDialog(null, "Continue?", "Attention!", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE) == 0);
        JOptionPane.showMessageDialog(null, "End of program.", "Bye!", JOptionPane.WARNING_MESSAGE);
    }
}
