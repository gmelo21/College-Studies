package br.com.fiap.main;
import br.com.fiap.bean.Employee;

import java.time.LocalDate;
import java.util.Scanner;

public class MainFunc2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Enter name: ");
            String name = scanner.nextLine();

            System.out.print("Enter age: ");
            int age = scanner.nextInt();
            scanner.nextLine();

            System.out.print("Enter position: ");
            String position = scanner.nextLine();

            System.out.print("Enter salary: ");
            double salary = scanner.nextDouble();

            Employee emp = new Employee(name, age, position, salary);

            System.out.println("Name: " + emp.getName());
            System.out.println("Age: " + emp.getAge());
            System.out.println("Position: " + emp.getPosition());
            System.out.println("Salary: $" + emp.getSalary());

            LocalDate today = LocalDate.now();
            System.out.printf("Current date: %02d/%02d/%d\n",
                    today.getDayOfMonth(), today.getMonthValue(), today.getYear());

        } catch (Exception e) {
            System.out.println("An error occurred during input.");
        } finally {
            scanner.close();
        }
    }
}