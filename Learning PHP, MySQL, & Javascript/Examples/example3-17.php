<?php //Declaring a static variable
	  //IE: A variable whose scope needs to be local, but that I don't want to be
	  //changed every time I recall the function
	  //IE: I want to count how many times a function has been called - I don't
	  //want that value to be reset every time I run the function
function test() //Note: this function doesn't actually print the value yet, because it isn't called
{
	static $count = 0;
	echo $count;
	$count++;
}
?>