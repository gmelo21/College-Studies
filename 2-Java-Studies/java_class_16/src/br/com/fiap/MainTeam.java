package br.com.fiap;

import javax.swing.*;

public class MainTeam {
    public static void main(String[] args) {
        Team group;
        String name;
        String[] members;
        int quantity;

        do {
            try {
                name = JOptionPane.showInputDialog("Choose the team's name: ");
                quantity = Integer.parseInt(JOptionPane.showInputDialog("How many members: "));
                members = new String[quantity];
                for (int i = 0; i < members.length; i++) {
                    members[i] = JOptionPane.showInputDialog(String.format("Member %d: ", (i + 1)));
                }
                group = new Team(name, members);
                group.listTeam();

            } catch (Exception e) {
                JOptionPane.showMessageDialog(null, e.getMessage(), "Error!", JOptionPane.ERROR_MESSAGE);
            }

        } while (JOptionPane.showConfirmDialog(null, "Continue?", "Attention!", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE) == 0);
        JOptionPane.showMessageDialog(null, "End of program.", "Bye!", JOptionPane.WARNING_MESSAGE);
    }
}
