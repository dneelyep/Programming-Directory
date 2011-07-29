<div id="lightbox" class="leightbox">
    <?php 
$x = new HTML_Template_Flexy($this->options);
$x->compile('rvs_popup.html');
$_t = function_exists('clone') ? clone($t) : $t;
foreach(get_defined_vars()  as $k=>$v) {
    if ($k != 't') { $_t->$k = $v; }
}
$x->outputObject($_t, $this->elements);
?>
    <img id="lbMaxPos" src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/loading.gif" border="0" width="0" height="0" align="right">
</div>
<div id="loading" class="leightbox">
    <img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/loading.gif" border="0">
    <img id="loadingMaxPos" src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/loading.gif" border="0" width="0" height="0">
</div>
<div id="message" class="leightbox" style=" text-align:center;">
   <!-- 
   <img src="{webRoot}/themes/{theme}/sitebuilder/images/loading.gif" border="0" >
    <img id="messageMaxPos" src="{webRoot}/themes/{theme}/sitebuilder/images/loading.gif" border="0" width="0" height="0">
 -->
</div>
<div id="message2" class="leightbox" style="text-align:center;">
</div>
<img id="message2MaxPos" src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/loading.gif" border="0" width="0" height="0" align="right">

<!-- 
<div id="nonebody" class="leightbox">
    <img id="lbMaxPosNoneBody" src="{webRoot}/themes/{theme}/sitebuilder/images/loading.gif" border="0" width="0" height="0" align="right">
</div>
-->