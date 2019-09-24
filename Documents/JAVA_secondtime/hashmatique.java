import java.util.HashMap;
import java.util.Set;
public class hashmatique {
    public static void main(String[] args) {
        HashMap<String, String> hashmatique = new HashMap<String, String>();
        hashmatique.put("Something just like this", "I want something just like this");
        hashmatique.put("Opposites Attract", "Opposites attract always");
        hashmatique.put("Larger than life", "that makes you larger than life");
        hashmatique.put("Every step you take", "with every step you take I like you");

        
        System.out.println("Hash:" + hashmatique.get("Larger than life"));
        Set<String> keys = hashmatique.keySet();
        for(String key : keys) {
            System.out.println(key);
            System.out.println(hashmatique.get(key));    
        }
    
    }
}

