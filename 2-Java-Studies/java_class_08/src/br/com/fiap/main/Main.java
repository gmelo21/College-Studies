package br.com.fiap.main;

import br.com.fiap.bean.Radio;
import br.com.fiap.bean.Television;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int option;

        System.out.println("Choose the device: 1 - Radio | 2 - Television");
        int choice = scanner.nextInt();

        if (choice == 1) {
            Radio radio = new Radio();
            System.out.println("Enter the initial station (80.0 - 105.0 MHz):");
            radio.setStation(scanner.nextFloat());
            System.out.println("Enter the initial volume (0 - 100):");
            radio.setVolume(scanner.nextInt());

            do {
                System.out.println("\nChoose an option:");
                System.out.println("1 - Set new station");
                System.out.println("2 - Set new volume");
                System.out.println("3 - Increase volume");
                System.out.println("4 - Decrease volume");
                System.out.println("0 - Exit");
                option = scanner.nextInt();

                switch (option) {
                    case 1:
                        System.out.println("New station:");
                        radio.setStation(scanner.nextFloat());
                        break;
                    case 2:
                        System.out.println("New volume:");
                        radio.setVolume(scanner.nextInt());
                        break;
                    case 3:
                        radio.increaseVolume();
                        break;
                    case 4:
                        radio.decreaseVolume();
                        break;
                }
                System.out.printf("Current station: %.1f MHz \nCurrent volume: %d%n",
                        radio.getStation(), radio.getVolume());

            } while (option != 0);

        } else if (choice == 2) {
            Television tv = new Television();
            System.out.println("Enter the initial channel (2, 4, 5, 7, 13):");
            tv.setChannel(scanner.nextInt());
            System.out.println("Enter the initial volume (0 - 20):");
            tv.setVolume(scanner.nextInt());

            do {
                System.out.println("\nChoose an option:");
                System.out.println("1 - Set another channel");
                System.out.println("2 - Set new volume");
                System.out.println("3 - Increase volume");
                System.out.println("4 - Decrease volume");
                System.out.println("0 - Exit");
                option = scanner.nextInt();

                switch (option) {
                    case 1:
                        System.out.println("New channel:");
                        tv.setChannel(scanner.nextInt());
                        break;
                    case 2:
                        System.out.println("New volume:");
                        tv.setVolume(scanner.nextInt());
                        break;
                    case 3:
                        tv.increaseVolume();
                        break;
                    case 4:
                        tv.decreaseVolume();
                        break;
                }
                System.out.printf("Current channel: %d \nCurrent volume: %d%n",
                        tv.getChannel(), tv.getVolume());

            } while (option != 0);
        } else {
            System.out.println("Invalid option.");
        }
        scanner.close();
    }
}
