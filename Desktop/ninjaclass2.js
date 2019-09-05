function Ninja(name) {
    this.name = name;
    this.health = 100;
    var speed =3;
    var strength =3;

  this.sayName= function(){console.log("My ninja name is:", this.name);}
  this.showStats= function() { console.log(this.name,this.health,speed, strength);}
  this.drinkSake= function() {this.health += 10; console.log(this.health);}
  
  
  this.punch = function(myNinja) {if (myNinja instanceof Ninja) {myNinja.health -=5; console.log("Goemon was punched by" + this.name + "and lost 5 Health!");}}
  this.kick = function(myNinja) {myNinja.health -= 10;}

}
var ninja1 = new Ninja("Hyabusa");
ninja1.sayName();
// -> "My ninja name is Hyabusa!"
ninja1.showStats();
var blueNinja = new Ninja("Goemon");
var redNinja = new Ninja("Bill Gates");
redNinja.punch(1);
blueNinja.kick(redNinja);
console.log(typeof(ninja1));
console.log(ninja1 instanceof Ninja);
// -> "Bill Gates was kicked by Goemon and lost 15 Health!"
// In this case, redNinja Bill Gates lost 15 health because blueNinja Goemon has 1 point of strength

// -> "Goemon was punched by Bill Gates and lost 5 Health!"

// -> "Name: Hayabusa, Health: 100, Speed: 3, Strength: 3"
//sayName() - This should log that Ninja's name to the console.
// showStats() - This should show the Ninja's name, strength, speed, and health.
// drinkSake() - This should add +10 Health to the Ninja
