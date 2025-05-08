package br.com.fiap.bean;

public class Salesperson extends Employee {
    private double commission;

    public Salesperson() {}

    public Salesperson(String name, double hourlyRate, double commission) {
        super(name, hourlyRate);
        this.commission = commission;
    }

    public double getCommission() {
        return commission;
    }

    public void setCommission(double commission) {
        this.commission = commission;
    }

    public double calculateSalary() {
        return ((super.getHourlyRate() * 40) * 4) * (1 + commission / 10);
    }
}
