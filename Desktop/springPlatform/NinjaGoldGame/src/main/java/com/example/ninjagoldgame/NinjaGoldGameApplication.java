package com.example.ninjagoldgame;

import java.util.Random;

import javax.servlet.http.HttpSession;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

@SpringBootApplication
@Controller
public class NinjaGoldGameApplication {

	public static void main(String[] args) {
		SpringApplication.run(NinjaGoldGameApplication.class, args);
	}

	@RequestMapping("/Gold")
		public String login(HttpSession session){
			int gold = 0;
		
		session.setAttribute("gold", gold);
        return "Gold.jsp";}
	
	
	
	@RequestMapping(value="/farm", method=RequestMethod.POST)
	public String calculate(HttpSession session,@RequestParam(value="location") String location) {
		System.out.println("printing out value:" + location);
		String activities = "";
		
		if (location.equals("farm")) {
			Random rand = new Random(); 
			Integer randint1 = rand.nextInt(10); 
			randint1 += 10;
			Integer gold = (Integer) session.getAttribute("gold");
			Integer total =  randint1+gold;
			session.setAttribute("gold",total);
			activities= "You entered a farm and earned " + randint1 + "\n";
			System.out.println("activities:"+activities);
			String activities1= (String)session.getAttribute("activities");
			session.setAttribute("activities", activities+activities1);
			}
		else if (location.equals("cave")) {
			Random rand = new Random(); 
			Integer randint1 = rand.nextInt(5); 
			randint1 += 5;
			Integer gold = (Integer) session.getAttribute("gold");
			Integer total =  randint1+gold;
			session.setAttribute("gold", total);
			activities= "You entered a farm and earned " + randint1+ "\n";
			System.out.println("activities:"+activities);
			String activities1= (String)session.getAttribute("activities");
			session.setAttribute("activities", activities+activities1);
			}
		else if (location.equals("house")) {
			Random rand = new Random(); 
			Integer randint1 = rand.nextInt(2); 
			randint1 += 2;
			Integer gold = (Integer) session.getAttribute("gold");
			Integer total =  randint1+gold;
			session.setAttribute("gold", total);
			activities= "You entered a farm and earned " + randint1+ "\n";
			System.out.println("activities:"+activities);
			String activities1= (String)session.getAttribute("activities");
			session.setAttribute("activities", activities+activities1);
			}
		
		else if (location.equals("casino")) {
			Random rand = new Random(); 
			Integer randint1 = rand.nextInt(50); 
			Integer gold = (Integer) session.getAttribute("gold");
			Integer total =  randint1+gold;
			session.setAttribute("gold", total);
			activities= "You entered a farm and earned" + randint1+ "\n";
			System.out.println("activities:"+activities);
			String activities1= (String)session.getAttribute("activities");
			session.setAttribute("activities", activities+activities1);
			}
			
//			else if(location.equals("cave"))
		
		
		
//		session.setAttribute("name", name);
//        session.setAttribute("location", location);
//        session.setAttribute("language", language);
//        session.setAttribute("comment", comment);
   
	  
	  return "Gold.jsp";
}}
