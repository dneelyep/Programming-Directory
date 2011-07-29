<?php // A do...while loop based on the previous examples
$count = 1;
do
	echo "$count times 12 is" . $count * 12 . "<br />";
while (++$count <= 12);
	  // In a do...while loop, the statement is first completed after the do, then
	  // repeated based on the conditions in the while statement 
?>