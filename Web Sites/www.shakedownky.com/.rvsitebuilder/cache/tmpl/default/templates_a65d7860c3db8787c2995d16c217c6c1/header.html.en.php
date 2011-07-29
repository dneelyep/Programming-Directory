<?php if (!$t->ignoreXmlDeclare)  {?><?php echo "<"; ?>?xml version="1.0" encoding="<?php echo htmlspecialchars($t->charset);?>" ?><?php }?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="<?php echo htmlspecialchars($t->currLang);?>" xml:lang="<?php echo htmlspecialchars($t->currLang);?>">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=<?php echo htmlspecialchars($t->charset);?>" /> 
    <meta http-equiv="Content-Language" content="<?php echo htmlspecialchars($t->currLang);?>" />
    <!-- Support IE 6 / IE 7 open dialog submit form -->
	<base target="_self" />
	
    <title><?php echo htmlspecialchars($t->siteName);?> :: <?php echo htmlspecialchars($t->pageTitle);?></title>
    <style type="text/css" media="screen">
	<?php if ($t->phpSuExecRoot)  {?>
	    @import url("<?php echo htmlspecialchars($t->phpSuExecRoot);?>/www/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/css/style.php?charset=<?php echo htmlspecialchars($t->charset);?>");
	<?php } else {?>
        @import url("<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/css/style.php?charset=<?php echo htmlspecialchars($t->charset);?>");
	<?php }?>
    </style>
    <?php if ($t->aCssFiles)  {?>
        <?php if ($this->options['strict'] || (is_array($t->aCssFiles)  || is_object($t->aCssFiles))) foreach($t->aCssFiles as $file) {?>
	            <link rel="stylesheet" type="text/css" media="screen" href="<?php echo htmlspecialchars($t->webRoot);?>/<?php echo htmlspecialchars($file);?>" />
	     <?php }?>
    <?php }?>
    <?php echo $t->scriptOpen;?>
        var SGL_JS_WEBROOT="<?php echo htmlspecialchars($t->webRoot);?>";
        var SGL_JS_WINHEIGHT=<?php echo htmlspecialchars($t->conf['popup']['winHeight']);?>;
        var SGL_JS_WINWIDTH=<?php echo htmlspecialchars($t->conf['popup']['winWidth']);?>;
        var SGL_JS_SESSID="<?php echo htmlspecialchars($t->sessID);?>";
        var SGL_JS_CURRURL="<?php echo htmlspecialchars($t->currUrl);?>";
        var SGL_JS_INDEX = "<?php echo htmlspecialchars($t->webRoot);?>/<?php echo htmlspecialchars($t->conf['site']['frontScriptName']);?>"
    <?php echo $t->scriptClose;?>
    
    <?php 
$x = new HTML_Template_Flexy($this->options);
$x->compile('jsGlobal.html');
$_t = function_exists('clone') ? clone($t) : $t;
foreach(get_defined_vars()  as $k=>$v) {
    if ($k != 't') { $_t->$k = $v; }
}
$x->outputObject($_t, $this->elements);
?>
    <?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'makeJsOptimizerLink'))) echo $t->makeJsOptimizerLink();?>
    
    <?php echo $t->scriptOpen;?>
	    <?php if ($this->options['strict'] || (is_array($t->onReadyDom)  || is_object($t->onReadyDom))) foreach($t->onReadyDom as $eventHandler) {?>
	        sgl.ready("<?php echo htmlspecialchars($eventHandler);?>");
	    <?php }?>
	    <?php if ($t->onLoad)  {?>
	    window.onload = function() {
	        <?php if ($this->options['strict'] || (is_array($t->onLoad)  || is_object($t->onLoad))) foreach($t->onLoad as $eventHandler) {?>
	             <?php echo htmlspecialchars($eventHandler);?>;
	        <?php }?>
	    }
	    <?php }?>
	    <?php if ($t->onUnload)  {?>
	    window.onunload = function() {
	        <?php if ($this->options['strict'] || (is_array($t->onUnload)  || is_object($t->onUnload))) foreach($t->onUnload as $eventHandler) {?>
	             <?php echo htmlspecialchars($eventHandler);?>;
	        <?php }?>
	    }
	    <?php }?>
    <?php echo $t->scriptClose;?>

 </head>
 
<body onbeforeunload="return dirtyFormWin()">
