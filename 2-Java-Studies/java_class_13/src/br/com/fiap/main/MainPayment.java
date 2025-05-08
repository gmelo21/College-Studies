package br.com.fiap.main;

import javax.swing.JOptionPane;
import br.com.fiap.bean.Employee;
import br.com.fiap.bean.NightGuard;
import br.com.fiap.bean.Salesperson;

public class MainPayment {
    public static void main(String[] args) {
        String[] options = {"Employee", "Night Guard", "Salesperson"};
        String name;
        int choice, continueOption;
        double hourlyRate, nightBonus, commission, salary;
        Employee emp;

        while (true) {
            choice = JOptionPane.showOptionDialog(null, "Select employee type:", "Salary Calculator",
                    JOptionPane.DEFAULT_OPTION, JOptionPane.INFORMATION_MESSAGE, null, options, options[0]);

            if (choice == -1) break;

            name = JOptionPane.showInputDialog("Enter name:");
            hourlyRate = Double.parseDouble(JOptionPane.showInputDialog("Enter hourly rate:"));

            if (choice == 0) {
                emp = new Employee(name, hourlyRate);
            } else if (choice == 1) {
                nightBonus = Double.parseDouble(JOptionPane.showInputDialog("Enter night bonus:"));
                emp = new NightGuard(name, hourlyRate, nightBonus);
            } else {
                commission = Double.parseDouble(JOptionPane.showInputDialog("Enter commission (%):"));
                emp = new Salesperson(name, hourlyRate, commission);
            }

            salary = emp.calculateSalary();
            JOptionPane.showMessageDialog(null, "Name: " + emp.getName() + "\nSalary: $" + salary);

            continueOption = JOptionPane.showConfirmDialog(null, "Do you want to continue?", "Continue",
                    JOptionPane.YES_NO_OPTION);
            if (continueOption != JOptionPane.YES_OPTION) break;
        }

        JOptionPane.showMessageDialog(null, "Goodbye!");
    }
}
