<?php // The "if...OR" statement modified - this will ensure the getnext function is called
$gn = getnext(); // Here the value of getnext() is stored in $gn, from which it will be
				 // called in the following if statement
if ($finished == 1 or $gn == 1) exit;
?>