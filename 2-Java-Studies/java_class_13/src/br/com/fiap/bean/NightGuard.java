package br.com.fiap.bean;

public class NightGuard extends Employee {
    private double nightBonus;

    public NightGuard() {}

    public NightGuard(String name, double hourlyRate, double nightBonus) {
        super(name, hourlyRate);
        this.nightBonus = nightBonus;
    }

    public double getNightBonus() {
        return nightBonus;
    }

    public void setNightBonus(double nightBonus) {
        this.nightBonus = nightBonus;
    }

    public double calculateSalary() {
        return (super.getHourlyRate() * 40) * 4 + (nightBonus * 20);
    }
}
