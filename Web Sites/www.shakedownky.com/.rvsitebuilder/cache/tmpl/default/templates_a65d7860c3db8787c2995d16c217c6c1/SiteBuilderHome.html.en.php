<!DOCTYPE html public "-//W3C//DTD HTML 4.0 Transitional//EN">
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=iso-8859-1">
<title><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Detect JavaScript");?></title>
</head>
<body onLoad="DetectJavaScript('<?php echo htmlspecialchars($t->redirectPage);?>')">
<p>
<script type="text/javascript">
function DetectJavaScript(redirectPage) {
	window.location.href = redirectPage;
}
</script>
<noscript>
<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Your browser doesnot support JavaScript or JavaScript support has been disabled. Please enable it and try again.");?>
</noscript>
</p>

</body>
</html>