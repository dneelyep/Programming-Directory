<?php //Walking through a numeric array using the foreach...as loop
$paper = array("Copier", "Inkjet", "Laser", "Photo");
$j = 0;

foreach ($paper as $item)
{
	echo "$j: $item<br />";
	++$j;
}
?>