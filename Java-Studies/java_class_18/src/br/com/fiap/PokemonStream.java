package br.com.fiap;

import javax.swing.*;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class PokemonStream {
    public static void main(String[] args) {
        boolean keep = true;

        while (keep) {
            HashMap<String, String> pokemons = new HashMap<>();

            while (true) {
                String name = JOptionPane.showInputDialog("Enter Pokémon name (or type 'end' to stop):");
                if (name.equalsIgnoreCase("end")) break;

                if (pokemons.containsKey(name)) {
                    JOptionPane.showMessageDialog(null, "This Pokémon is already registered!");
                    continue;
                }

                String type = JOptionPane.showInputDialog("Enter Pokémon type:");
                pokemons.put(name, type);
            }

            String chosenType = JOptionPane.showInputDialog("Enter a type to search:");

            String result = pokemons.entrySet().stream()
                    .filter(entry -> entry.getValue().equalsIgnoreCase(chosenType))
                    .map(Map.Entry::getKey)
                    .collect(Collectors.joining("\n"));

            if (result.isEmpty()) {
                JOptionPane.showMessageDialog(null, "No Pokémon found of type: " + chosenType);
            } else {
                JOptionPane.showMessageDialog(null, "Pokémon of type: " + chosenType + "\n" + result);
            }

            int option = JOptionPane.showConfirmDialog(null, "Do you want to continue?", "Continue", JOptionPane.YES_NO_OPTION);
            if (option == JOptionPane.NO_OPTION) {
                JOptionPane.showMessageDialog(null, "Goodbye!");
                keep = false;
            }
        }
    }
}
