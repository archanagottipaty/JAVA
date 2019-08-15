package com.example.hellohuman;

import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;


@SpringBootApplication
@Controller
public class HellohumanApplication{
	public static void main(String[] args) {
	SpringApplication.run(HellohumanApplication.class, args);
//		SpringApplication.run(HomeController1.class, args);
	}
	
	@RequestMapping("/date")
	public String index(Model model) {
		model.addAttribute("dojoName", "Burbank");
        
        Date date = new java.util.Date();
        model.addAttribute("date", date);
        return "date.jsp";}
	
	@RequestMapping("/time")
	public String index2(Model model) {
		Calendar cal = Calendar.getInstance();
        SimpleDateFormat sdf = new SimpleDateFormat("HH:mm:ss");
        
		 
        model.addAttribute("sdf", sdf.format(cal.getTime()));
        return "time.jsp";

}}

