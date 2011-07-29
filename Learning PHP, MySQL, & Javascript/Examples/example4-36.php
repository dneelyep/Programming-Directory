<?php // Trapping division-by-zero errors using the continue statement
$j = 10;

while ($j > -10)
{
	$j--;
	if ($j == 0) continue; // skips this step, because 0/0 would result in an error
	echo (10 / $j) . "<br />";	
}
	  // The continue statement lets you jump to the next iteration of a loop
	  // automatically, rather than complete redundant steps
?>