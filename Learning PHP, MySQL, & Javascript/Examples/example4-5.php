<?php // + and - have the same precedence: the operation is performed normally, start to finish
echo 1 + 2 + 3 - 4 + 5;
echo 2 - 4 + 5 + 3 + 1;
echo 5 + 2 - 4 + 1 + 3;
?>