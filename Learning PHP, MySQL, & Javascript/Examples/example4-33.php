<?php // Da almighty for loop
for ($count = 1; $count <= 12; ++$count)
	echo "$count times 12 is " . $count * 12 . "<br />";
	  // The for loop takes three parameters:
	  // Initialization expression; Condition expression; Modification expression
	  //
	  // In other words: at beginning of loop, the initialization expression ($count = 1;)
	  // is run. At the end of the loop, the modification expression (++$count) is
	  // executed. Then, when the loop starts over, the condition expression
	  // ($count <= 12) is tested - if TRUE, run the loop, else, don't run the loop.
?>