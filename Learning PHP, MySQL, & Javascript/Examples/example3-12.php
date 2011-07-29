<?php
function longdate($timestamp)
{
	return date("1 F jS Y", $timestamp);
}

echo longdate(time());
?>