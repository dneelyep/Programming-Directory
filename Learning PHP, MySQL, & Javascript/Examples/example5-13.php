<?php //Cloning an object - in other words: taking the original values of a given 
	  //instance of a class, and assigning those values to a new instance, separate
	  //from the original instance
$object1 = new User();
$object1->name = "Alice";
$object2 = clone $object1;
$object2->name = "Amy";
echo "object1's name is " . $object1->name . "<br />";
echo "object2's name is " . $object2->name;

class User
{
	public $name;
}
?>