<?php //Defining a two-dimensional array - Like setting up a game of tic-tac-toe
$gamestate = array(array('x', '', 'o'),
				   array('o', 'o','x'),
				   array('x', 'o', ''));
echo $gamestate[0][0]; //printing the content of the first row and first cell
echo $gamestate[2][1]; //printing the content of the third row and second cell
?>