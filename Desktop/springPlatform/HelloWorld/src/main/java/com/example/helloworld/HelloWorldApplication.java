package com.example.helloworld;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


@SpringBootApplication
@RestController
public class HelloWorldApplication {
	public static void main(String[] args) {
	SpringApplication.run(HelloWorldApplication.class, args);
//		SpringApplication.run(HomeController1.class, args);
	}
	@RequestMapping("/")
	public String hello() {
		return "Hello client! How are you doing?";
	}
	
	@RequestMapping("/random")
	public String random() {	
		return "Spring Boot is great! So easy to just respond with strings";
		
	}
	
	@RequestMapping("dojo/m/{track}/{module}/{lesson}")
    public String showLesson(@PathVariable("track") String track, @PathVariable("module") String module, @PathVariable("lesson") String lesson){
    	return "Track: " + track + ", Module: " + module + ", Lesson: " + lesson;}
}
