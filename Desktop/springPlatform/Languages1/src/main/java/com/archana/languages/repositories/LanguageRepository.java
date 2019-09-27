

package com.archana.languages.repositories;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.archana.languages.models.Language;
@Repository
public interface LanguageRepository extends CrudRepository<Language, Long> {
    Language findByName(String name);
}
