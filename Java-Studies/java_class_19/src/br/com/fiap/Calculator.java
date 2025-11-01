package br.com.fiap;

import java.math.BigDecimal;

public class Calculator {
    private double numberA;
    private double numberB;

    public Calculator() {}

    public double getNumberA() {
        return numberA;
    }

    public void setNumberA(double numberA) {
        this.numberA = numberA;
    }

    public double getNumberB() {
        return numberB;
    }

    public void setNumberB(double numberB) {
        this.numberB = numberB;
    }

    public double add() {
        return numberA + numberB;
    }

    public double subtract() {
        return numberA - numberB;
    }

    public double multiply() {
        return numberA * numberB;
    }

    public double divide() {
        if (numberB == 0.0) {
            throw new ArithmeticException("Division by zero");
        }
        return numberA / numberB;
    }
}
