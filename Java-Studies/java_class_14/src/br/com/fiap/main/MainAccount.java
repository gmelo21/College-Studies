package br.com.fiap.main;

import br.com.fiap.bean.SpecialAccount;

import javax.swing.JOptionPane;

public class MainAccount {
    public static void main(String[] args) {
        SpecialAccount account = new SpecialAccount();
        boolean continueLoop = true;

        while (continueLoop) {
            int number = Integer.parseInt(JOptionPane.showInputDialog("Enter the account number:"));
            float balance = Float.parseFloat(JOptionPane.showInputDialog("Enter the account balance:"));
            float limit = Float.parseFloat(JOptionPane.showInputDialog("Enter the account limit:"));

            account.setAccountNumber(number);
            account.setBalance(balance);
            account.setLimit(limit);

            String option = JOptionPane.showInputDialog("Choose the operation:\n1 - Withdraw\n2 - Deposit");
            float value = Float.parseFloat(JOptionPane.showInputDialog("Enter the amount:"));

            if (option.equals("1")) {
                account.withdraw(value);
            } else if (option.equals("2")) {
                account.deposit(value);
            }

            String details = String.format(
                    "Account number: %d\nCurrent balance: %.2f\nLimit: %.2f",
                    account.getAccountNumber(), account.getBalance(), account.getLimit()
            );
            JOptionPane.showMessageDialog(null, details);

            int resp = JOptionPane.showConfirmDialog(null, "Do you want to continue?", "Confirmation", JOptionPane.YES_NO_OPTION);
            continueLoop = (resp == JOptionPane.YES_OPTION);
        }

        JOptionPane.showMessageDialog(null, "Thank you for using our system!");
    }
}
