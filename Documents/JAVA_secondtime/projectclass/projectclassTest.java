
class projectclassTest{
public static void main(String[] args){

    projectclass myprojectclass = new projectclass("Rule the world", "Trump");
    projectclass myprojectclass1 = new projectclass();
    projectclass myprojectclass2 = new projectclass("Modi");
    myprojectclass.elevatorPitch();
    myprojectclass1.elevatorPitch();
    myprojectclass2.elevatorPitch();
    System.out.println(myprojectclass2.getDescription("Mow the whitehouse lawn"));
    }}