package br.com.fiap;

import javax.swing.*;

public class Hero {
    private String name;
    private String secretId;
    private String[] powers;
    private String[] weaknesses;

    public Hero() {}

    public Hero(String name, String secretId, String[] powers, String[] weaknesses) {
        this.name = name;
        this.secretId = secretId;
        this.powers = powers;
        this.weaknesses = weaknesses;
    }

    public String getName() { return name; }

    public void setName(String name) { this.name = name; }

    public String getSecretId() { return secretId; }

    public void setSecretId(String secretId) { this.secretId = secretId; }

    public String[] getPowers() { return powers; }

    public void setPowers(String[] powers) { this.powers = powers; }

    public String[] getWeaknesses() { return weaknesses; }

    public void setWeaknesses(String[] weaknesses) { this.weaknesses = weaknesses; }

    public void listHero() {
        String show = String.format("Name: %s\n", name);
        show += String.format("Secret identity: %s\n", secretId);

        int count = 1;

        for (String i : powers) {
            show += String.format("Power %d: %s\n", count, i);
            count++;
        }

        count = 1;

        for (String i : weaknesses) {
            show += String.format("Weakness %d: %s\n", count, i);
            count++;
        }

        JOptionPane.showMessageDialog(null, show, "Hero's data", JOptionPane.INFORMATION_MESSAGE);
    }


}
