package br.com.fiap.bean;

public class Weapon {
    public String name;
    public String affinity;
    public int damage;

    public void upgrade() {
        damage += 10;
    }

    public void changeAffinity(String newAffinity) {
        String[] validAffinities = {
                "Standard", "Heavy", "Keen", "Quality", "Magic",
                "Frost", "Fire", "Flame Art", "Lightning", "Sacred",
                "Poison", "Blood", "Occult"
        };

        boolean isValid = false;
        for (String valid : validAffinities) {
            if (valid.equalsIgnoreCase(newAffinity)) {
                isValid = true;
                break;
            }
        }

        if (isValid) {
            affinity = newAffinity.substring(0, 1).toUpperCase() + newAffinity.substring(1).toLowerCase();
        } else {
            System.out.println("Invalid affinity! Choose from: Standard, Heavy, Keen, Quality, Magic, Frost, Fire, Flame Art, Lightning, Sacred, Poison, Blood, Occult.");
        }
    }
}
