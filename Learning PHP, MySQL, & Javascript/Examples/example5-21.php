<?php //Declaring constants, within a class
Translate::lookup();

class Translate	//It's generally accepted to declare constant variables in all caps
{
	const ENGLISH = 0;
	const SPANISH = 1;
	const FRENCH  = 2;
	const GERMAN  = 3;
	// etc, etc...
	
	function lookup()
	{
		echo self::SPANISH;
	}
	
}
?>