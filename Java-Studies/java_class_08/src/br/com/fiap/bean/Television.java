package br.com.fiap.bean;

public class Television {
    private int volume;
    private int channel;

    public int getVolume() {
        return volume;
    }

    public void setVolume(int volume) {
        if (volume >= 0 && volume <= 20) {
            this.volume = volume;
        } else {
            System.out.println("Volume out of the allowed range (min=0 and max=20)");
        }
    }

    public int getChannel() {
        return channel;
    }

    public void setChannel(int channel) {
        if (channel == 2 || channel == 4 || channel == 5 || channel == 7 || channel == 13) {
            this.channel = channel;
        } else {
            System.out.println("Invalid channel! Allowed channels: 2, 4, 5, 7, 13");
        }
    }

    public void increaseVolume() {
        if (volume < 20) {
            volume++;
        }
    }

    public void decreaseVolume() {
        if (volume > 0) {
            volume--;
        }
    }
}
