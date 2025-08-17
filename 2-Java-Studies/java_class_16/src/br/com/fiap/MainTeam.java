package br.com.fiap;

import javax.swing.*;
import java.util.ArrayList;

public class MainTeam {
    public static void main(String[] args) {
        boolean keep = true;
        while (keep) {
            String name = JOptionPane.showInputDialog("Enter the team name:");
            ArrayList<String> members = new ArrayList<>();
            while (true) {
                String member = JOptionPane.showInputDialog("Enter a member name (or type 'end' to stop):");
                if (member.equalsIgnoreCase("end")) break;
                members.add(member);
            }
            Team team = new Team(name, members);
            team.listTeam();
            int option = JOptionPane.showConfirmDialog(null, "Do you want to continue?", "Continue", JOptionPane.YES_NO_OPTION);
            if (option == JOptionPane.NO_OPTION) {
                JOptionPane.showMessageDialog(null, "Goodbye!");
                keep = false;
            }
        }
    }
}
