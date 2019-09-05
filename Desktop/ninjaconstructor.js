function Ninja(name) {
    this.name = name;
    this.health = 100;
    var speed =3;
    var strength =3;

  this.sayName= function(){console.log("My ninja name is:", this.name);}
  this.showStats= function() { console.log(this.name,this.health,speed, strength);}
  this.drinkSake= function() {this.health += 10; console.log(this.health);}
}
var ninja1 = new Ninja("Hyabusa");
ninja1.sayName();
// -> "My ninja name is Hyabusa!"
ninja1.showStats();
// -> "Name: Hayabusa, Health: 100, Speed: 3, Strength: 3"
//sayName() - This should log that Ninja's name to the console.
// showStats() - This should show the Ninja's name, strength, speed, and health.
// drinkSake() - This should add +10 Health to the Ninja
