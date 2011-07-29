<?php // Logical operators
$a = 1; $b = 0;
echo ($a AND $b) . "<br />"; // Result is TRUE if both operands are TRUE
echo ($a or $b)  . "<br />"; // TRUE if either operand is TRUE
echo ($a XOR $b) . "<br />"; // TRUE if only one of the two operands are TRUE 
echo !$a		 . "<br />"; // TRUE if the operand is FALSE and vice versa
?>