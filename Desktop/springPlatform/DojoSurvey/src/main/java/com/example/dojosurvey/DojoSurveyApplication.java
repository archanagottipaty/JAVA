package com.example.dojosurvey;

import javax.servlet.http.HttpSession;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@SpringBootApplication
@Controller
public class DojoSurveyApplication {

	public static void main(String[] args) {
		SpringApplication.run(DojoSurveyApplication.class, args);
	}
	
	@RequestMapping("/")
	public String index(Model model) {
        return "index.jsp";}
	
	@RequestMapping(value="/", method=RequestMethod.POST)
	public String login(HttpSession session,@RequestParam(value="name") String name,@RequestParam(value="location") String location, @RequestParam(value="language") String language, @RequestParam(value="comment") String comment, RedirectAttributes redirectAttributes ) {
        // ... process information and save it to the session
		
	        session.setAttribute("name", name);
	        session.setAttribute("location", location);
	        session.setAttribute("language", language);
	        session.setAttribute("comment", comment);
	       
	  System.out.println("I am printing out the FORM passed in name" + name);
	  
		  return "results.jsp";}
	  }


