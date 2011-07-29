<?php //This example should fix the problems in example 3-14
$temp = "The date is ";
echo $temp . longdate(time());

function longdate($timestamp)
{
	return date("1 F jS Y", $timestamp);
}
?>