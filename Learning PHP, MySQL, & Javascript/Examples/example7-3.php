<?php //Using the checkdate() function to make sure a given date is valid
$month = 9;    //September (note: only has 30 days)
$day   = 31;   //31st
$year  = 2012; //2012

if (checkdate($month, $day, $year)) echo "DA DATE ROCS!";
	else echo "TRY AGAIN TARD";

//if the result of checkdate() is true, echo good response, else bad response
?>