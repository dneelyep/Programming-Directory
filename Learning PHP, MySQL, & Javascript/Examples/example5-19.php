<?php /*Defining a property implicitly
		Here the User class begins with no properties, but automatically "gains"
		properties along with values once they're declared above. It's not 
		neccessary to declare these properties in the class, because adding new
		properties with values implies that these new properties and values should
		become default properties and values in the given class*/
$object1 = new User();
$object1->name = "Alice";
echo $object1->name;

class User {}
?>