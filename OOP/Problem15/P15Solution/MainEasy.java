public class MainEasy
{
	public static void main(String[] args) {

		Hero alexis = new ElvenWarrior("Alexis", 662, "Female", 90);
		Hero gideon = new Magician("Gideon", "Male", 20);
		Hero bigfoot = new Barbarian("Bigfoot", 30, 50);

		Item sword = new Item("Lighting Sword", 15);
		Item shield = new Item("Hardened Shield", 20);
		Item saber = new Item("Dragon Saber", 12);
		Item dagger = new Item("Poison Dagger", 10);

		alexis.pickUpItem(shield);
		alexis.pickUpItem(saber);
		gideon.pickUpItem(sword);
		bigfoot.pickUpItem(dagger);
			
		alexis.attackHero(gideon);

	}
}
