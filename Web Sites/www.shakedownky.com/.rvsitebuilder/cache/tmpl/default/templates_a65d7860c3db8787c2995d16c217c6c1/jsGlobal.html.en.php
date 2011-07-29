<?php echo $t->scriptOpen;?>
       /*
       Don't delete this javascript comment because flexy print new line by self then get javascript error.
       '<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo htmlspecialchars($this->plugin("translateJsMsg","You have made any changes to the fields without submitting, your changes will be lost."));?>';
       */
var lostWarning = '<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo htmlspecialchars($this->plugin("translateJsMsg","You have made any changes to the fields without submitting, your changes will be lost."));?>';
var txtConfPre = '<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo htmlspecialchars($this->plugin("translateJsMsg","You have made any changes to the fields without submitting."));?>' + "\n" + '<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo htmlspecialchars($this->plugin("translateJsMsg","Do you want to preview without changes?"));?>';	
var msgChLang = '<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo htmlspecialchars($this->plugin("translateJsMsg","Change langauge warning"));?>';
var rvsPreviewUrl = "<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'makeUrl'))) echo htmlspecialchars($t->makeUrl("","preview","sitebuilder"));?>";
var rvsSelectStyleUrl = "<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'makeUrl'))) echo htmlspecialchars($t->makeUrl("","selectstyles","sitebuilder"));?>";
var rvsCategoryUrl = "<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'makeUrl'))) echo htmlspecialchars($t->makeUrl("","rvscategory","sitebuilder"));?>";
var rvsUrl = "<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'makeUrl'))) echo htmlspecialchars($t->makeUrl("","createproject","sitebuilder"));?>";
var rvsMod = "<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'makeUrl'))) echo htmlspecialchars($t->makeUrl("","","sitebuilder"));?>";
var rvsWebRoot = "<?php echo htmlspecialchars($t->webRoot);?>";
var sessID = "<?php echo htmlspecialchars($t->sessID);?>";
var msgSuccess = '<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo htmlspecialchars($this->plugin("translateJsMsg","success"));?>';
var msgCancel = '<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo htmlspecialchars($this->plugin("translateJsMsg","Cancel"));?>';
var msgXmlErrorMemoryAndMaxTime = '<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo htmlspecialchars($this->plugin("translateJsMsg","Due to lavge amount of data,please contact your provider to increase PHP max execution time must over 180 second and The maximum of memory must over 256Mb in WHM Tweak setting."));?>';
var RVS_AJAX_INDEX = '<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'makeUrl'))) echo htmlspecialchars($t->makeUrl("sitebuilderAjaxExecute","",""));?>';
var SGL_PRODUCTION = '';
var confirmTRUE = '';
var confirmFALSE = '';
<?php echo $t->scriptClose;?>

<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'addGlobalJavascriptFile'))) echo htmlspecialchars($t->addGlobalJavascriptFile(1,"js/RVdebug.js"));?>
<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'addGlobalJavascriptFile'))) echo htmlspecialchars($t->addGlobalJavascriptFile(1,"js/dirtyForm.js"));?>


<!-- Add jQuery UI -->
<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'addGlobalJavascriptFile'))) echo htmlspecialchars($t->addGlobalJavascriptFile(2,"js/jquery-ui/jquery.js"));?>
<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'addGlobalJavascriptFile'))) echo htmlspecialchars($t->addGlobalJavascriptFile(2,"js/jquery-ui/ui/ui.core.js"));?>
<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'addGlobalJavascriptFile'))) echo htmlspecialchars($t->addGlobalJavascriptFile(2,"js/jquery-ui/ui/ui.draggable.js"));?>
<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'addGlobalJavascriptFile'))) echo htmlspecialchars($t->addGlobalJavascriptFile(2,"js/jquery-ui/ui/ui.resizable.js"));?>
<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'addGlobalJavascriptFile'))) echo htmlspecialchars($t->addGlobalJavascriptFile(2,"js/jquery-ui/ui/ui.dialog.js"));?>
<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'addGlobalJavascriptFile'))) echo htmlspecialchars($t->addGlobalJavascriptFile(2,"js/jquery-ui/external/bgiframe/jquery.bgiframe.js"));?>
<!-- End Add jQuery UI -->

<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'addGlobalJavascriptFile'))) echo htmlspecialchars($t->addGlobalJavascriptFile(3,"js/prototype/prototype.js"));?>
<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'addGlobalJavascriptFile'))) echo htmlspecialchars($t->addGlobalJavascriptFile(3,"js/scriptaculous/src/effects.js"));?>
<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'addGlobalJavascriptFile'))) echo htmlspecialchars($t->addGlobalJavascriptFile(3,"js/scriptaculous/src/dragdrop.js"));?>
<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'addGlobalJavascriptFile'))) echo htmlspecialchars($t->addGlobalJavascriptFile(3,"js/lightbox/leightbox.js"));?>

<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'addGlobalJavascriptFile'))) echo htmlspecialchars($t->addGlobalJavascriptFile(4,"js/ShowHideStepInfo.js"));?>
<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'addGlobalJavascriptFile'))) echo htmlspecialchars($t->addGlobalJavascriptFile(4,"js/rvsitebuilder.js"));?>
<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'addGlobalJavascriptFile'))) echo htmlspecialchars($t->addGlobalJavascriptFile(4,"js/AjaxSitebuilder.js"));?>
<!-- BooM Test -->
<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'addGlobalJavascriptFile'))) echo htmlspecialchars($t->addGlobalJavascriptFile(4,"js/rvsModalWindow.js"));?>
