package br.com.fiap.main;

import br.com.fiap.bean.Weapon;

public class UseWeapon {
    public static void main(String[] args) {
        Weapon myWeapon = new Weapon();

        myWeapon.name = "Rivers of Blood";
        myWeapon.affinity = "Blood";
        myWeapon.damage = 100;

        myWeapon.upgrade();
        myWeapon.upgrade();
        myWeapon.changeAffinity("Keen");

        System.out.println("br.com.fiap.bean.Weapon name: " + myWeapon.name);
        System.out.println("br.com.fiap.bean.Weapon affinity: " + myWeapon.affinity);
        System.out.println("Current damage: " + myWeapon.damage);
    }
}
