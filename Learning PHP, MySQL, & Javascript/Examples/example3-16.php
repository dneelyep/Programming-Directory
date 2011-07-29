<?php //An alternative solution the problems with Example 3-14
$temp = "The date is ";
echo longdate($temp, time());

function longdate($text, $timestamp)
{
	return $text . date("1 F jS Y", $timestamp);
}
?>