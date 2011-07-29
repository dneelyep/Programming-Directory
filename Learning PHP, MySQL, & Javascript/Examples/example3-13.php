<?php
function longdate($timestamp)
{
	$temp = date("1 F jS Y", $timestamp);
	return "The date it $temp";
}
?>