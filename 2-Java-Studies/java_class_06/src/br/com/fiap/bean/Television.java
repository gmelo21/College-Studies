package br.com.fiap.bean;

public class Television {
    public int volume;
    public int channel;

    public void increaseVolume() {
        volume++;
    }

    public void decreaseVolume() {
        volume--;
    }

    public void changeChannel(int newChannel) {
        channel = newChannel;
    }
}
