<?php //Using the foreach...as loop on an associative array
$paper = array('copier' => "Copier & Multipurpose",
			   'inkjet' => "Inkjet Printer",
			   'laser'  => "Laser Printer",
			   'photo'  => "Photographic Paper");

foreach ($paper as $item => $description)
	echo "$item: $description<br />";
	
/* So here: the contents of the above array are assigned to the $paper variable.
 * Then comes the foreach...as loop. The loop is stating: Foreach item in the
 * $paper array, starting with the first, set the keyword equal to the $item
 * variable and the value of the keyword to the $description variable, then
 * perform the steps in the loop. Do this until all items in the array are 
 * depleted */
?>