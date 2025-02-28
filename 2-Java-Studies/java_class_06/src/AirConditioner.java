public class AirConditioner {
    public int temperature;
    public String mode;

    public void increaseTemperature() {
        temperature++;
    }

    public void decreaseTemperature() {
        temperature--;
    }

    public void changeMode(String newMode) {
        if (newMode.equals("cool") || newMode.equals("heat") || newMode.equals("fan")) {
            mode = newMode;
        } else {
            System.out.println("Invalid Air Conditioner mode! Use: cool, heat, or fan.");
        }
    }
}
