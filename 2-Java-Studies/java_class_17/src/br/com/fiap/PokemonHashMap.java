package br.com.fiap;

import javax.swing.*;
import java.util.HashMap;
import java.util.Map;

public class PokemonHashMap {
    public static void main(String[] args) {
        boolean keep = true;

        while (keep) {
            HashMap<String, String> pokemons = new HashMap<>();

            while (true) {
                String name = JOptionPane.showInputDialog("Enter Pokémon name (or type 'end' to stop):");
                if (name.equalsIgnoreCase("end")) break;

                if (pokemons.containsKey(name)) {
                    JOptionPane.showMessageDialog(null, "This Pokémon is already registered!", "Warning!", JOptionPane.WARNING_MESSAGE);
                    continue;
                }

                String type = JOptionPane.showInputDialog("Enter Pokémon type:");
                pokemons.put(name, type);
            }

            String chosenType = JOptionPane.showInputDialog("Enter a type to search:");
            String result = "Pokémon of type: " + chosenType + "\n";

            for (Map.Entry<String, String> entry : pokemons.entrySet()) {
                if (entry.getValue().equalsIgnoreCase(chosenType)) {
                    result += entry.getKey() + "\n";
                }
            }

            JOptionPane.showMessageDialog(null, result);

            int option = JOptionPane.showConfirmDialog(null, "Do you want to continue?", "Continue", JOptionPane.YES_NO_OPTION);
            if (option == JOptionPane.NO_OPTION) {
                JOptionPane.showMessageDialog(null, "Goodbye!");
                keep = false;
            }
        }
    }
}
