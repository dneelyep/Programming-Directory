<?php //Copying an object
	  //This is confusing - $object1 and $object2 are referring to the same instance of
	  //the User class - thus, the name "Amy" is assigned to both - refer to later
	  //examples to avoid this
$object1 = new User();
$object1->name = "Alice";
$object2 = $object1;
$object2->name = "Amy";
echo "object1 name = " . $object1->name . "<br />";
echo "object2 name = " . $object2->name;

class User
{
	public $name;
}
?>