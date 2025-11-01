package br.com.fiap.bean;

public class Adding {
    private int wholeNum1, wholeNum2;
    private double realNum1, realNum2;

    public Adding() {
    }

    public int getWholeNum1() {
        return wholeNum1;
    }

    public void setWholeNum1(int wholeNum1) {
        this.wholeNum1 = wholeNum1;
    }

    public int getWholeNum2() {
        return wholeNum2;
    }

    public void setWholeNum2(int wholeNum2) {
        this.wholeNum2 = wholeNum2;
    }

    public double getRealNum1() {
        return realNum1;
    }

    public void setRealNum1(double realNum1) {
        this.realNum1 = realNum1;
    }

    public double getRealNum2() {
        return realNum2;
    }

    public void setRealNum2(double realNum2) {
        this.realNum2 = realNum2;
    }

    public int add(int n1, int n2) {
        return n1 + n2;
    }

    public double add(double n1, double n2) {
        return n1 + n2;
    }
}
