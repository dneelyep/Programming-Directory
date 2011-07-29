<?php //creating a simple php text file for use in later example
$fh = fopen("testfile.txt", 'w') or die("FILE CREATION FAILED");
$text = <<<_END
Line 1
Line 2
Line 3

_END;
fwrite($fh, $text) or die("NO COULD RITE TO DA FILE");
fclose($fh);
echo "File 'testfile.txt' written successfully"
?>