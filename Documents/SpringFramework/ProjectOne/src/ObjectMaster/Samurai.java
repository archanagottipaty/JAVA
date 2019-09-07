package ObjectMaster;

public class Samurai extends Human{
		
	Samurai(){
		numberofSamurai +=1;
	setHealth(200);
}
	
	void deathBlow(){
		this.setHealth(100);
	}
	
	void meditate(){
		this.setHealth(200);
		
	}

	int howMany(){
		
		return numberofSamurai;
	}
	
}