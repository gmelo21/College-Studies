package br.com.fiap.main;

import java.time.LocalDate;
import br.com.fiap.bean.Employee;

public class MainFunc1 {
    public static void main(String[] args) {
        Employee emp = new Employee();

        emp.setName("Gemma");
        emp.setAge(30);
        emp.setPosition("Blacksmith");
        emp.setSalary(5000.0);

        System.out.println("Name: " + emp.getName());
        System.out.println("Age: " + emp.getAge());
        System.out.println("Position: " + emp.getPosition());
        System.out.println("Salary: $" + emp.getSalary());

        LocalDate today = LocalDate.now();
        System.out.printf("Current date: %02d/%02d/%d\n",
                today.getDayOfMonth(), today.getMonthValue(), today.getYear());
    }
}
