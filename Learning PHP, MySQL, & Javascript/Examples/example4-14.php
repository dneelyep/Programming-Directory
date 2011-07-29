<?php // The inequality and not identical operators
$a = "1000";
$b = "+1000";
if ($a != $b) echo "1";  // Here, a = b because they're converted to numerical values and compared
if ($a !== $b) echo "2"; // Here, a != b because they're compared as strings
?>