package br.com.fiap.main;

import br.com.fiap.bean.Monsties;
import javax.swing.*;
import java.io.IOException;

public class UsesMonsties {
    public static void main(String[] args) {
        boolean keepRunning = true;

        while (keepRunning) {
            String opcao = JOptionPane.showInputDialog("Select an option:\n1 - Register\n2 - Consult\n3 - Exit");

            switch (opcao) {
                case "1":
                    register();
                    break;
                case "2":
                    consult();
                    break;
                case "3":
                    keepRunning = false;
                    JOptionPane.showMessageDialog(null, "Until later, rider!");
                    break;
                default:
                    JOptionPane.showMessageDialog(null, "Invalid option.");
            }
        }
    }

    private static void register() {
        String path = JOptionPane.showInputDialog("Type the folder path: ");
        Monsties m = new Monsties();
        m.setName(JOptionPane.showInputDialog("What's your monstie's name? "));
        m.setSpecies(JOptionPane.showInputDialog("What about it's species? "));
        m.setElement(JOptionPane.showInputDialog("And it's element?"));
        m.setStatTotal(Integer.parseInt(JOptionPane.showInputDialog("Finally, it's stat total? ")));

        try {
            m.record(path);
            JOptionPane.showMessageDialog(null, "Monstie sent to the stable!");
        } catch (IOException e) {
            JOptionPane.showMessageDialog(null, "Failed to save! Error: " + e.getMessage());
        }
    }

    private static void consult() {
        String path = JOptionPane.showInputDialog("Type the folder's path: ");
        String name = JOptionPane.showInputDialog("Type your monstie's name: ");

        Monsties m = new Monsties();
        m.setName(name);
        try {
            m.read(path);
            JOptionPane.showMessageDialog(null, m.toString());
        } catch (IOException e) {
            JOptionPane.showMessageDialog(null, "Failed to read! Error: " + e.getMessage());
        }
    }
}
