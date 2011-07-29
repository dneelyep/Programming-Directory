<?php //Using the $this variable within a method
class User
{
	public $name, $password;
	
	function get_password()
	{
		return $this->password;  /*Returns the value of $this (the User object [the
								   current instance of the User class, NOT the
								   User class]) variable 
								   $password*/
	}
}