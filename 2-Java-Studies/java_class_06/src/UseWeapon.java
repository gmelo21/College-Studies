public class UseWeapon {
    public static void main(String[] args) {
        Weapon myWeapon = new Weapon();

        myWeapon.name = "Rivers of Blood";
        myWeapon.affinity = "Blood";
        myWeapon.damage = 100;

        myWeapon.upgrade();
        myWeapon.upgrade();
        myWeapon.changeAffinity("Keen");

        System.out.println("Weapon name: " + myWeapon.name);
        System.out.println("Weapon affinity: " + myWeapon.affinity);
        System.out.println("Current damage: " + myWeapon.damage);
    }
}
