<?php
$number = 12345 * 67890;
echo substr($number, 3, 1); // prints out 1 number, starting at the 4th position of
							// the variable $number
							// ----------------------
							// Note that PHP is taking the number from $number and
							// converting it to a string to use the substr function,
							// based upon its context (the use of the substr function)
?>