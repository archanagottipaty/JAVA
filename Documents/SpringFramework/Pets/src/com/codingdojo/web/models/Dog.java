package com.codingdojo.web.models;

public class Dog extends Animal implements Pet{
	
	public Dog() {}
	
	public Dog(String name, String breed, int weight) {
		super(name,breed,weight);
	}
	
	@Override
	public String showAffection() {
		if (this.weight >=30){
			return Name+"curled up next to you";
		}
		return Name+"dog hopped into your lap and cuddled you!";
	}

}
