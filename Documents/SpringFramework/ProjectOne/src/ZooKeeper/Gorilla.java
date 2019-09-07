package ZooKeeper;

public class Gorilla extends mammal{
	
	public void throwThings(){
		energyLevel -=5;
		System.out.println("throwThings():energylevel:" + energyLevel);}
	
	public void eatBananas(){
		energyLevel += 10;
		System.out.println("throwThings:eatBananas():" + energyLevel);}
	

	public void Climb(){
		energyLevel  -= 10;
		System.out.println("Climb():energylevel:" + energyLevel);}
}
