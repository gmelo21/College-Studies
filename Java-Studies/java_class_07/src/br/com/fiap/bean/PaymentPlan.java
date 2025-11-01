package br.com.fiap.bean;

public class PaymentPlan {
    public double rawSalary;
    public double INSSpercentage;
    public double healthcarePlan;
    public int dependents;

    public double liquidSalaryCalc() {
        double INSSdiscount = rawSalary * (INSSpercentage / 100);

        return rawSalary - INSSdiscount - (healthcarePlan * dependents);
    }
}
