package com.example.hellohuman;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;


@SpringBootApplication
@RestController
public class HellohumanApplication{
	public static void main(String[] args) {
	SpringApplication.run(HellohumanApplication.class, args);
//		SpringApplication.run(HomeController1.class, args);
	}
	
	@RequestMapping("/")
    public String index1(){
		
		
			return "Hello Human";

    }

	@RequestMapping("/")
    public String index(@RequestParam(value="name", required=false) String searchQuery) {
		
		if (searchQuery == null) {
			return "Hello Human";
		}
        return "Hello " + searchQuery;
    }
}
