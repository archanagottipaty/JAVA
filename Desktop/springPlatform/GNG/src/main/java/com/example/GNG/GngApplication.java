package com.example.GNG;

import java.text.SimpleDateFormat;
import java.util.Calendar;

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
public class GngApplication {

	public static void main(String[] args) {
		SpringApplication.run(GngApplication.class, args);
	}

	
	@RequestMapping("/")
	public String index(Model model) {
        return "index.jsp";}
	
	@RequestMapping("/createError")
	public String flashMessages(RedirectAttributes redirectAttributes) {
        redirectAttributes.addFlashAttribute("error", "A test errror!");
        return "redirect:/";
	}
	
	
        
        
	    @RequestMapping(value="/", method=RequestMethod.POST)
	     public String login(@RequestParam(value="trycode") String user,RedirectAttributes redirectAttributes ) {
	            // ... process information and save it to the session
	    	  System.out.println("I am printing out the FORM passed in value" + user);
	    	  if (user.equals("Bushido"))
	            {return "redirect:/code";}
	    	  else 
	    	  {
	    		  System.out.println("I am in the else sttatmetn" + user);
	    		  return "redirect:/createError";}
	    	  }
	    		  
	      
	// ...
	
	@RequestMapping("/code")
	public String index2(Model model) {
        return "code.jsp";

}
}

