package br.com.fiap;

public class StringManipulation {
    public static void main(String[] args) {
        String sentence = "Mother... Wouldst thou truly lordship sanction, in one so bereft of light?";
        System.out.printf("Sentence: %s", sentence);

        int quantity = sentence.length();
        System.out.printf("\nQuantity of characters: %d", quantity);

        String uppercase = sentence.toUpperCase();
        System.out.printf("\nUppercase sentence: %s", uppercase);

        String word = sentence.substring(68, 74);
        System.out.printf("\nSpecific substring: %s", word);

        String newSentence = sentence.replace("Mother", "Dear Marika");
        System.out.printf("\nReplacing a word: %s", newSentence);
    }
}
