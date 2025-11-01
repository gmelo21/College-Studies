package br.com.fiap;

import javax.swing.*;
import java.util.ArrayList;
import java.util.Collections;

public class Hero {
    private String name;
    private String secretIdentity;
    private ArrayList<String> powers;
    private ArrayList<String> weaknesses;

    public Hero() {
        this.powers = new ArrayList<>();
        this.weaknesses = new ArrayList<>();
    }

    public Hero(String name, String secretIdentity, ArrayList<String> powers, ArrayList<String> weaknesses) {
        this.name = name;
        this.secretIdentity = secretIdentity;
        this.powers = powers;
        this.weaknesses = weaknesses;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSecretIdentity() {
        return secretIdentity;
    }

    public void setSecretIdentity(String secretIdentity) {
        this.secretIdentity = secretIdentity;
    }

    public ArrayList<String> getPowers() {
        return powers;
    }

    public void setPowers(ArrayList<String> powers) {
        this.powers = powers;
    }

    public ArrayList<String> getWeaknesses() {
        return weaknesses;
    }

    public void setWeaknesses(ArrayList<String> weaknesses) {
        this.weaknesses = weaknesses;
    }

    public void listHero() {
        Collections.sort(powers);
        Collections.sort(weaknesses);
        String show = String.format("Hero: %s\nSecret Identity: %s\n\nPowers:\n", name, secretIdentity);
        int count = 1;
        for (String power : powers) {
            show += String.format("%d. %s\n", count, power);
            count++;
        }
        show += "\nWeaknesses:\n";
        count = 1;
        for (String weakness : weaknesses) {
            show += String.format("%d. %s\n", count, weakness);
            count++;
        }
        JOptionPane.showMessageDialog(null, show, "Hero", JOptionPane.INFORMATION_MESSAGE);
    }
}
