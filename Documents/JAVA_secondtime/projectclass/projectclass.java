import java.util.ArrayList;
class projectclass{
    String name;
    String description;

    projectclass(String name, String description){
        this.name = name;
        this.description = description;
    }

    public projectclass() {}

public projectclass(String name) { this.name = name;}


    String elevatorPitch(){
        String returnString =name + ":" + description;
        System.out.println(returnString);
        return returnString;
    
    }

    String getName(){
        return this.name;
    }

     void setName(String name){
        this.name = name;
    }

     void setDescription(String description){
        this.description = description;
    }

    String getDescription (String desc){
        this.description = desc;
        return desc;
    }


}
