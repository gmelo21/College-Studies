package br.com.fiap.main;

import java.util.HashMap;
import java.util.Map;

public class NaviHashMap {
    public static void main(String[] args) {
        HashMap<String, Integer> people = new HashMap<>();
        people.put("Madeline", 18);
        people.put("Theo", 25);
        people.put("Oshiro", 140);
        people.put("Granny", 86);
        for (Map.Entry<String, Integer> i : people.entrySet()) {
            System.out.println("Name: " + i.getKey());
            System.out.println("Age: " + i.getValue());
        }
    }
}
