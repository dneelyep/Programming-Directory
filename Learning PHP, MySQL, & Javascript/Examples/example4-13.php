<?php // The == operator converts the values to a different type (numerical values) before comparing them
	  // The === operator keeps their original types (strings) and compares them
$a = "1000";
$b = "+1000";
if ($a == $b) echo "1";
if ($a === $b) echo "2";
?>