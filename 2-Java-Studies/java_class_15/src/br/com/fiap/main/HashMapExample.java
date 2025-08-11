package br.com.fiap.main;

import javax.swing.*;
import java.util.HashMap;

public class HashMapExample {
    public static void main(String[] args) {
        HashMap<String, String> map = new HashMap<>();

        do {
            try {
                String acronym, state;

                do {
                    acronym = JOptionPane.showInputDialog("Type in the acronym for a state or \"END\" to end the application.")
                            .toUpperCase();

                    if (!acronym.equals("END")) {
                        if (map.containsKey(acronym)) {
                            JOptionPane.showMessageDialog(null, "Error! This state is already registered.");
                        } else {
                            state = JOptionPane.showInputDialog("Type the full name for this state.");
                            map.put(acronym, state);
                        }
                    }
                } while (!acronym.equals("END"));

                String choice;
                do {
                    choice = JOptionPane.showInputDialog("Type in an acronym to search for its name.").toUpperCase();
                    if (map.containsKey(choice)) {
                        JOptionPane.showMessageDialog(null, "State name: " + map.get(choice),
                                "State Name", JOptionPane.INFORMATION_MESSAGE);
                    } else {
                        JOptionPane.showMessageDialog(null, "State not registered.");
                    }
                } while (JOptionPane.showConfirmDialog(null, "Do you want to search for another state?", "Search Again",
                        JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE) == JOptionPane.YES_OPTION);

            } catch (Exception e) {
                JOptionPane.showMessageDialog(null, e.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            }
        } while (JOptionPane.showConfirmDialog(null, "End the application?", "Attention",
                JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE) == JOptionPane.NO_OPTION);

        JOptionPane.showMessageDialog(null, "Application closed.", "Bye!", JOptionPane.WARNING_MESSAGE);
    }
}
