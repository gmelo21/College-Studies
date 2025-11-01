package br.com.fiap;

import javax.swing.*;
import java.util.ArrayList;
import java.util.Collections;

public class Team {
    private String name;
    private ArrayList<String> members;

    public Team() {
        this.members = new ArrayList<>();
    }

    public Team(String name, ArrayList<String> members) {
        this.name = name;
        this.members = members;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ArrayList<String> getMembers() {
        return members;
    }

    public void setMembers(ArrayList<String> members) {
        this.members = members;
    }

    public void listTeam() {
        Collections.sort(members);
        String show = String.format("Team name: %s\n", name);
        int count = 1;
        for (String member : members) {
            show += String.format("Member %d: %s\n", count, member);
            count++;
        }
        JOptionPane.showMessageDialog(null, show, "Team", JOptionPane.INFORMATION_MESSAGE);
    }
}
