package br.com.fiap;

import javax.swing.*;
import java.time.LocalDate;
import java.time.Period;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;

public class Exercise2 {
    public static void main(String[] args) {
        try {
            String dateInput1 = JOptionPane.showInputDialog("Select your date (DD/MM/YYYY format): ");
            String dateInput2 = JOptionPane.showInputDialog("Select your other date (DD/MM/YYYY format): ");

            DateTimeFormatter dateFormatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");

            LocalDate date1 = LocalDate.parse(dateInput1, dateFormatter);
            LocalDate date2 = LocalDate.parse(dateInput2, dateFormatter);

            Period period = Period.between(date1, date2);

            String formattedDate1 = date1.format(dateFormatter);
            String formattedDate2 = date2.format(dateFormatter);

            JOptionPane.showMessageDialog(null, String.format("Dates selected: \n%s\n%s", formattedDate1, formattedDate2));

            String message = String.format("There has been: \n%d years, %d months and %d days \nbetween the two dates.",
                    period.getYears(), period.getMonths(), period.getDays());
            JOptionPane.showMessageDialog(null, message);

        } catch (DateTimeParseException e) {
            JOptionPane.showMessageDialog(null, "Invalid date format! Please use DD/MM/YYYY.");
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "An unexpected error occurred: " + e.getMessage());
        }
    }
}
