<?php //Using the compact function, to turn, in this example, a set of variables into
	  //an array
$fname   = "Elizabeth";
$sname   = "Windsor";
$address = "Buckingham Palace";
$city    = "London";
$country = "United Kingdom";

$contact = compact('fname', 'sname', 'address', 'city', 'country');
print_r($contact);
?>