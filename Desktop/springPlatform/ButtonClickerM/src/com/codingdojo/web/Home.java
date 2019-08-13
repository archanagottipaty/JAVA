package com.codingdojo.web;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**
 * Servlet implementation class Home
 */
@WebServlet("/Home")
public class Home extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Home() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// ...
			HttpSession session = request.getSession();
//		        session.setAttribute("count", count);
		      int count = 0;
		                if (session.getAttribute("count") == null) 
		                	{count = 0;
		                	}
//		                else {
//		                	session.setAttribute("count", count);
//		                	}	
		                RequestDispatcher view = request.getRequestDispatcher("/WEB-INF/view/ButtonClickerM.jsp");
		 		        view.forward(request, response);
		                // ...
	}
	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		 HttpSession session = request.getSession();
		 int count = (Integer)session.getAttribute("count");
		count +=1;
		System.out.println("Count is: "+ count);
		session.setAttribute("count", count);
		response.sendRedirect("/ButtonClickerM/Home");

		
	}

}
