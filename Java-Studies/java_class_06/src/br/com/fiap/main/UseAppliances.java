package br.com.fiap.main;

import br.com.fiap.bean.AirConditioner;
import br.com.fiap.bean.Television;

public class UseAppliances {
    public static void main(String[] args) {
        Television tv = new Television();

        tv.volume = 10;
        tv.channel = 5;

        tv.increaseVolume();
        tv.increaseVolume();
        tv.decreaseVolume();
        tv.changeChannel(12);

        System.out.println("Current volume: " + tv.volume);
        System.out.println("Current channel: " + tv.channel);

        AirConditioner ac = new AirConditioner();

        ac.temperature = 22;
        ac.mode = "cool";

        ac.increaseTemperature();
        ac.increaseTemperature();
        ac.decreaseTemperature();
        ac.changeMode("heat");

        System.out.println("Current temperature: " + ac.temperature);
        System.out.println("Current mode: " + ac.mode);
    }
}
