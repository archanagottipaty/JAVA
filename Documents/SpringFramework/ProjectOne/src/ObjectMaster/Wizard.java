package ObjectMaster;

public class Wizard extends Human{
	
	Wizard(){
		setHealth(50);
		setIntelligence(8);
	}
	
	void heal() {
		setHealth(this.getIntelligence());
		System.out.println("Wizard.getHealth():" + getHealth());
	}
	
	void fireball(){
		setHealth(3*this.getIntelligence());
		System.out.println("Wizard.fireballgetHealth():" + getHealth());
	}
	

}
