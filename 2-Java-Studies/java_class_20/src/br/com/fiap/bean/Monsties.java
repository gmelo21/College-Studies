package br.com.fiap.bean;

import java.io.*;

public class Monsties implements IDBMonsties {
    private String name;
    private String species;
    private String element;
    private int statTotal;

    public Monsties() {}

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getSpecies() { return species; }
    public void setSpecies(String species) { this.species = species; }

    public String getElement() { return element; }
    public void setElement(String element) { this.element = element; }

    public int getStatTotal() { return statTotal; }
    public void setStatTotal(int statTotal) { this.statTotal = statTotal; }

    @Override
    public void record(String path) throws IOException {
        File folder = new File(path);
        if (!folder.exists()) {
            folder.mkdir();
        }

        String fileName = path + "/" + name + ".txt";
        try (PrintWriter pw = new PrintWriter(new FileWriter(fileName))) {
            pw.println(name);
            pw.println(species);
            pw.println(element);
            pw.println(statTotal);
        }
    }


    @Override
    public Monsties read(String path) throws IOException {
        String fileName = path + "/" + name + ".txt";
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            this.name = br.readLine();
            this.species = br.readLine();
            this.element = br.readLine();
            this.statTotal = Integer.parseInt(br.readLine());
        }
        return this;
    }

    @Override
    public String toString() {
        return "Name: " + name + "\nEspecies: " + species +
                "\nElement: " + element +
                "\nStat total: " + statTotal;
    }
}
