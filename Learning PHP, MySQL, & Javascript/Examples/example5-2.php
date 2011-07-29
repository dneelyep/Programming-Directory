<?php // Making a full name print correctly (fixing user errors)
echo fix_names("WILLIAM", "henry", "gatES");

function fix_names($n1, $n2, $n3)
{
	$n1 = ucfirst(strtolower($n1));     // The value of the given argument is first
	$n2 = ucfirst(strtolower($n2));		// converted to all lower case (strtolower),
	$n3 = ucfirst(strtolower($n3));		// then the first letter to upper case (ucfirst)
	return $n1 . " " . $n2 . " " . $n3;	// The value of these are returned
}
?>