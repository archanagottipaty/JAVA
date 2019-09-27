package com.archana.languages.controllers;
import java.awt.print.Book;
import java.util.List;

import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import com.archana.languages.models.Language;
import com.archana.languages.services.LanguageService;

@Controller
public class Languages {
//1. Annotation

	
	private final LanguageService languageService;
	//private final LanguageValidator languageValidator;
	 
	 public Languages(LanguageService languageService) {
	     this.languageService = languageService;
	     //this.userValidator = userValidator;
	 }

@RequestMapping("/")
// 3. Method that maps to the request route above
public String hello() { // 3
	return "redirect:/languages";
}


@RequestMapping(value = "/createlanguage", method = RequestMethod.POST)
//3. Method that maps to the request route above
public String createlanguage(@RequestParam("name") String name,@RequestParam("creator") String creator,@RequestParam("version") double version, Model model)
{ // 3
	Language mylang = new Language();
	mylang.setName(name);
	mylang.setCreator(creator);
	mylang.setVersion(version);
	languageService.createLanguage(mylang);
	return "redirect:/languages";
}

@RequestMapping("/languages")
public String getlanguages(Model model) {
	List<Language> languages = languageService.allLanguages();
//	System.out.println("I am printng out langauges inside /languages");
//	System.out.println(languages.get(0).getName());
	//System.out.println(languages.get(0)[0]);
//	System.out.println(languages.get(0).getVersion());
//	System.out.println(languages.get(0).getCreator());
//	System.out.println(languages.get(1));
//	System.out.println(languages.get(2));
	model.addAttribute("languages",languages);
	return "languages.jsp";	
}

//@RequestMapping("/languages/delete/{id}")
//public void delete(@PathVariable)
//{}
//, method=RequestMethod.DELETE
@RequestMapping(value="/languages/delete/{id}")
public String delete(@PathVariable("id") Long id) {
	System.out.println("I am inside the /languages/delete/{id}" + id);
    languageService.deleteLanguage(id);
    System.out.println("I am inside the /languages/delete/id: SECOND TIME");
    return "redirect:/languages";
}


//@RequestMapping("/books/{id}/edit")
//public String edit(@PathVariable("id") Long id, Model model) {
//    Book book = bookService.findBook(id);
//    model.addAttribute("book", book);
//    return "/books/edit.jsp";


@RequestMapping("/languages/edit/{id}")
public String edit(@PathVariable("id") Long id,  Model model) {
    Language language = languageService.findLanguage(id);
    model.addAttribute("language",language);
    return "edit.jsp";
}

@RequestMapping(value="/languages/{id}", method=RequestMethod.PUT)
public String update(@Valid @ModelAttribute("language") Language language, BindingResult result) {
    if (result.hasErrors()) {
        return "edit.jsp";
    } else {
        languageService.updateLanguage(language);
        return "redirect:/languages";
    }
}

@RequestMapping(value = "/languages/{id}")
	public String details(@PathVariable("id") Long id, Model model) {
	Language language = languageService.findLanguage(id);
    model.addAttribute("language",language);
		
	    return "details.jsp";
	}
	
	
}

