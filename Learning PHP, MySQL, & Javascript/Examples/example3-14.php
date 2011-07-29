<?php // This example should fail - because $temp is a local variable,
	  // but it was declared before the function in which it occurs
	  // It should have been declared inside the actual function, I think
$temp = "The date is";
echo longdate(time());

function longdate($timestamp)
{
	return $temp . date("1 F jS Y", $timestamp);
}
?>