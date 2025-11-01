package br.com.fiap;

import javax.swing.*;
import java.time.LocalDate;
import java.time.Period;
import java.time.format.DateTimeFormatter;

public class DateFormat {
    public static void main(String[] args) {
        LocalDate actualDate = LocalDate.now();
        LocalDate theEnd = LocalDate.parse("2012-12-21");
        Period period = Period.between(theEnd, actualDate);

        String message = String.format("Since the end of times, it has passed: \n%d years, \n%d months and \n%d days.",
                period.getYears(), period.getMonths(), period.getDays());
        JOptionPane.showMessageDialog(null, message);

        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        JOptionPane.showMessageDialog(null, theEnd.format(dtf));
    }
}
