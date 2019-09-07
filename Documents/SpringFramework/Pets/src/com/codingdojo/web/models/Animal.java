package com.codingdojo.web.models;

public class Animal {

	protected String Name;
	protected String Breed;
	protected int weight;
	
	public Animal() {}
	
	public Animal(String name, String breed, int weight) {
		
		Name=name;
		Breed=breed;
		this.weight=weight;
	}
	
	public String getName() {
		return Name;
	}
	public void setName(String name) {
		Name = name;
	}
	public String getBreed() {
		return Breed;
	}
	public void setBreed(String breed) {
		Breed = breed;
	}
	public int getWeight() {
		return weight;
	}
	public void setWeight(int weight) {
		this.weight = weight;
	}
}
