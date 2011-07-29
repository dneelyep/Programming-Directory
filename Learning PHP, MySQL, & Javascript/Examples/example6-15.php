<?php //Using the compact function to help with debugging
$j       = 23;
$temp    = "HAITHAR";
$address = "1 Old Street";
$age     = 61;

print_r(compact(explode(' ', 'j temp address age')));
?>