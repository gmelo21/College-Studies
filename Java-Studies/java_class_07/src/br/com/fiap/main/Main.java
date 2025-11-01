package br.com.fiap.main;
import br.com.fiap.bean.PaymentPlan;

public class Main {
    public static void main(String[] args) {
        PaymentPlan payment = new PaymentPlan();

        payment.rawSalary = 5000.00;
        payment.INSSpercentage = 10;
        payment.healthcarePlan = 200.00;
        payment.dependents = 2;

        double netSalary = payment.liquidSalaryCalc();

        System.out.println("Net salary: R$" + netSalary);
    }
}
