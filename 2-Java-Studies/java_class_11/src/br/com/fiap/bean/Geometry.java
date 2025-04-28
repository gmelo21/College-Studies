package br.com.fiap.bean;

import javax.swing.*;

public class Geometry {
    private float side;
    private float height;
    private double radius;

    public Geometry() {
    }

    public float getSide() {
        return side;
    }

    public void setSide(float side) {
        this.side = side;
    }

    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }

    public double getRadius() {
        return radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    public void calcArea(float side) {
        setSide(side);
        float area = this.side * this.side;
        JOptionPane.showMessageDialog(null, String.format("The square's area is: %.2f", area));
    }

    public void calcArea(float side, float height) {
        setSide(side);
        setHeight(height);
        float area = this.side * this.height;
        JOptionPane.showMessageDialog(null, String.format("The rectangle's area is: %.2f", area));
    }

    public void calcArea(double radius) {
        setRadius(radius);
        double area = Math.PI * Math.pow(this.radius, 2);
        JOptionPane.showMessageDialog(null, String.format("The circle's area is: %.2f", area));
    }
}
