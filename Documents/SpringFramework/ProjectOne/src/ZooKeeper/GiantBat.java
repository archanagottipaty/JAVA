package ZooKeeper;

public class GiantBat extends mammal{
	
	public GiantBat() {
	energyLevel = 300;}
	
	public void fly() {
	
		System.out.println("Fly():shwoooooooooooooosh");}
	
	public void eatHumans() {
		energyLevel += 25;
		}
	
	public void attackTowns() {
		energyLevel -=100;
		System.out.println("attackTowns():Fire!Fire!" + energyLevel);}
	
	
public void displayEnergy() {
	super.displayEnergy();
	
}}


