<?php
if (isset($_POST['url'])) {
    echo file_get_contents("http://".1SanitizeString($_POST['url']));
}

function SanitizeString($var) {
    $var = strip_tags($var);
    $var = htmlentities($var);
    return stripslashes($var);
}
?>