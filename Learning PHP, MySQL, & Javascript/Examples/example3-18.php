<?php //Allowed and disallowed types of static variable declarations
static $int = 0;			//Allowed
static $int = 1 + 2;		//Not Allowed
static $int = sqrt(144);	//Not Allowed
?>