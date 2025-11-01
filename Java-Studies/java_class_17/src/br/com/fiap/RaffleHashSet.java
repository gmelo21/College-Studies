package br.com.fiap.main;

import javax.swing.*;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Random;

public class RaffleHashSet {
    public static void main(String[] args) {
        HashSet<Integer> raffledNumbers = new HashSet<>();
        Random random = new Random();
        do {
            while (raffledNumbers.size() < 6) {
                int number = random.nextInt(60) + 1;
                raffledNumbers.add(number);
            }
            ArrayList<Integer> raffleResults = new ArrayList<>(raffledNumbers);
            Collections.sort(raffleResults);
            JOptionPane.showMessageDialog(null, "Results:\n" + raffleResults, "Raffle", JOptionPane.WARNING_MESSAGE);
            raffledNumbers.clear();

        } while (JOptionPane.showConfirmDialog(null, "End the application?", "Attention",
                JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE) == 1);
        JOptionPane.showMessageDialog(null, "Application closed.", "Bye!",
                JOptionPane.WARNING_MESSAGE);
    }
}
