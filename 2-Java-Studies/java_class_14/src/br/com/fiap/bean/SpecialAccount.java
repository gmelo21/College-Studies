package br.com.fiap.bean;

public class SpecialAccount implements BankAccount {
    private int accountNumber;
    private float balance;
    private float limit;

    public SpecialAccount() {
    }

    public int getAccountNumber() {
        return accountNumber;
    }

    public void setAccountNumber(int accountNumber) {
        this.accountNumber = accountNumber;
    }

    public float getBalance() {
        return balance;
    }

    public void setBalance(float balance) {
        this.balance = balance;
    }

    public float getLimit() {
        return limit;
    }

    public void setLimit(float limit) {
        this.limit = limit;
    }

    public float withdraw(float amount) {
        if (amount <= balance + limit) {
            balance -= amount;
        }
        return balance;
    }

    public float deposit(float amount) {
        balance += amount;
        return balance;
    }
}
