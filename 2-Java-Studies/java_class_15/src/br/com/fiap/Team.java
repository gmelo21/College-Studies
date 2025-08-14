package br.com.fiap;

import javax.swing.*;

public class Team {
    private String name;
    private String[] members;

    public Team() {}

    public Team(String name, String[] members) {
        this.name = name;
        this.members = members;
    }

    public String getName() { return name; }

    public void setName(String name) { this.name = name; }

    public String[] getMembers() { return members; }

    public void setMembers(String[] members) { this.members = members; }

    public void listTeam() {
        String show = String.format("Team name: %s \n", name);

        int count = 1;

        for (String i : members) {
            show += String.format("Member %d: %s \n", count, i);
            count++;
        }
        JOptionPane.showMessageDialog(null, show, "Team List", JOptionPane.INFORMATION_MESSAGE);
    }

}
