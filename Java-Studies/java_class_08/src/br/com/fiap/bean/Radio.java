package br.com.fiap.bean;

public class Radio {
    private int volume;
    private float station;

    public int getVolume() {
        return volume;
    }

    public void setVolume(int volume) {
        try {
            if (volume >= 0 && volume <= 100) {
                this.volume = volume;
            } else {
                throw new Exception("Volume out of the allowed range (min=0 and max=100)");
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public float getStation() {
        return station;
    }

    public void setStation(float station) {
        try {
            if (station >= 80.0 && station <= 105.0) {
                this.station = station;
            } else {
                throw new Exception("Station out of the allowed range (min=80.0 and max=105.0)");
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public void increaseVolume() {
        if (volume < 100) {
            volume++;
        }
    }

    public void decreaseVolume() {
        if (volume > 0) {
            volume--;
        }
    }
}
