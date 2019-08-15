package com.example.counter;
import javax.servlet.http.HttpSession;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@SpringBootApplication
@Controller
public class CounterApplication{
	public static void main(String[] args) {
	SpringApplication.run(CounterApplication.class, args);
//		SpringApplication.run(HomeController1.class, args);
	}
	@RequestMapping("/your_server")
	public String index(HttpSession session) {
		Integer count = (Integer) session.getAttribute("count");
		if (count==null) {
			session.setAttribute("count", 0);
        }
		count+=1;
		session.setAttribute("count",count);
        return "welcome.jsp";}
	
	
	@RequestMapping("/your_server/counter")
	public String index1(HttpSession session, Model model) {
        return "counter.jsp";}
}
