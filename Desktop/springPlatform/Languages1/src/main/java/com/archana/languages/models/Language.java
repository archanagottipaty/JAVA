
package com.archana.languages.models;
import java.util.Date;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.PrePersist;
import javax.persistence.Table;
import javax.validation.constraints.Size;

import org.springframework.beans.factory.annotation.Required;

//imports removed for brevity
@Entity
@Table(name="languages")
public class Language {
 @Id
 @GeneratedValue(strategy=GenerationType.IDENTITY)
 private Long id;
 @Size(min=2, max=20)
 private String name;
 @Size(min=2, max=20)
 private String creator;
 private double version;
 @Column(updatable=false)
 private Date createdAt;
 private Date updatedAt;
 
 public Long getId() {
	return id;
}
public void setId(Long id) {
	this.id = id;
}
public String getName() {
	return name;
}
public void setName(String name) {
	this.name = name;
}
public String getCreator() {
	return creator;
}
public void setCreator(String creator) {
	this.creator = creator;
}
public double getVersion() {
	return version;
}
public void setVersion(double version) {
	this.version = version;
}
public Date getCreatedAt() {
	return createdAt;
}
public void setCreatedAt(Date createdAt) {
	this.createdAt = createdAt;
}
public Date getUpdatedAt() {
	return updatedAt;
}
public void setUpdatedAt(Date updatedAt) {
	this.updatedAt = updatedAt;
}

 
 public Language() {}
@PrePersist
 protected void onCreate(){
     this.createdAt = new Date();
 }
}