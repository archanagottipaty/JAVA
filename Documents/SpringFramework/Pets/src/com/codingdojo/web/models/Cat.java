package com.codingdojo.web.models;

public class Cat extends Animal implements Pet{
	
	public Cat() {}
	
	public Cat(String name, String breed, int weight) {
		super(name,breed,weight);
	}
	
	@Override
	public String showAffection() {
		
		return "Your" +Breed+ "cat" +Name+ "at looked at you with affection.";
	}

}
