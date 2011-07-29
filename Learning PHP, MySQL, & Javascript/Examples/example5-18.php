<?php //Creating and accessing a static method - static methods can only access the
	  //properties of a class, not an object [an instance of a class]
User::pwd_string();

class User
{
	static function pwd_string()
	{
		echo "Enter yer password, plox";
	}
}
?>