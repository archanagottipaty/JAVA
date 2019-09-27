package com.archana.languages.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.archana.languages.models.Language;
import com.archana.languages.repositories.LanguageRepository;

@Service
public class LanguageService {
    private final LanguageRepository languageRepository;
    
    public LanguageService(LanguageRepository languageRepository) {
        this.languageRepository = languageRepository;
    }
    
 // find user by name
 	public Language findByName(String name) {
         return languageRepository.findByName(name);
     }
 	
 	public void createLanguage(Language language)
 	{ languageRepository.save(language);}

 	public List<Language> allLanguages() {
 		
 		return (List<Language>) languageRepository.findAll();
 	}
 	
 	public void deleteLanguage(Long id) {
 		
 		languageRepository.deleteById(id);
 	}
 	
// 	Optional<Book> optionalBook = bookRepository.findById(id);
//    if(optionalBook.isPresent()) {
//        return optionalBook.get();
//    } else {
//        return null;
//    }
public Language editLanguage(Long id) {
 		
	Optional<Language> optionalLanguage=languageRepository.findById(id);
	if(optionalLanguage.isPresent()) {
        return optionalLanguage.get();
    } else {
        return null;}}

public Language findLanguage(Long id) {
	Optional<Language> optionalLanguage=languageRepository.findById(id);
	if(optionalLanguage.isPresent()) {
        return optionalLanguage.get();
    } else {
        return null;}}

public void updateLanguage(Language language) {
	languageRepository.save(language);
}
	
}



