package br.com.fiap;

import javax.swing.*;

public class Exercise1 {
    public static void main(String[] args) {
        String sentence = JOptionPane.showInputDialog("Type in your sentence.");
        JOptionPane.showMessageDialog(null, String.format("Chosen sentence: %s", sentence));

        int quantity = sentence.length();
        JOptionPane.showMessageDialog(null, String.format("Quantity of characters: %d", quantity));

        String uppercase = sentence.toUpperCase();
        JOptionPane.showMessageDialog(null, String.format("Uppercase sentence: %s", uppercase));

        String toReplace = JOptionPane.showInputDialog("Type a part of the original sentence.");
        String newReplacement = JOptionPane.showInputDialog("Type what to replace the sentence by.");
        String newSentence = sentence.replace(toReplace, newReplacement);
        JOptionPane.showMessageDialog(null, String.format("New sentence: %s", newSentence));

        quantity = newSentence.length();
        JOptionPane.showMessageDialog(null, String.format("Quantity of characters: %d", quantity));
    }
}