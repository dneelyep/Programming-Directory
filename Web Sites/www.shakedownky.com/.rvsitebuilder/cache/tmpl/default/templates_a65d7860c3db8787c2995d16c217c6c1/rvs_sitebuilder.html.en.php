
<?php 
$x = new HTML_Template_Flexy($this->options);
$x->compile('header.html');
$_t = function_exists('clone') ? clone($t) : $t;
foreach(get_defined_vars()  as $k=>$v) {
    if ($k != 't') { $_t->$k = $v; }
}
$x->outputObject($_t, $this->elements);
?> 

<input type="hidden" id="nextStep" value="<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo htmlspecialchars($this->plugin("ChangeStepImg",$t->step,"NextStep",9));?>" />
<input type="hidden" id="thisStep" value="<?php echo htmlspecialchars($t->step);?>" />

<!-- NEW Design -->
<table cellpadding="0" cellspacing="0" width="100%" class="borderOutside">
	<tr>
		<td class="tableRVS"><table cellpadding="0" cellspacing="0" width="100%">
            <tr>
                <td><!-- Start TOP BAR -->
                        <div id="topBar">
                            <table cellpadding="0" cellspacing="0" border="0" width="100%">
                                <tr>
                                    <td><div class="brand"><?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo $this->plugin("getTextBrand");?></div>
                                            <div class="menu">
                                                <div class="close"></div>
                                                <div class="link"><a href="<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo htmlspecialchars($this->plugin("getHomeUrl"));?><?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo htmlspecialchars($this->plugin("getLogoutUrl"));?>"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Logout");?></a></div>
                                                <div class="bar"></div>
                                                <div class="link"><a href="<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo htmlspecialchars($this->plugin("getHomeUrl"));?>"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Control Panel");?></a></div>
                                                <div class="open"></div>
                                            </div></td>
                                </tr>
                            </table>
                        </div>
                    <!-- End TOP BAR -->
                        <!-- Start STEP -->
                        <div id="step">
                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                <tr>
                                    <td valign="top"><table border="0" cellspacing="0" cellpadding="0">
                                            <tr>
                                                <td valign="top" class="side"><a href="<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'makeUrl'))) echo htmlspecialchars($t->makeUrl("","sitebuilder","sitebuilder"));?>" class="active"> <img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/iconHome.jpg" alt="" width="39" height="59" border="0" /><br />
                                                    <?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("HOME");?> </a> </td>
                                                <td><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/closeHome.gif" alt="" width="12" height="86" /></td>
                                            </tr>
                                    </table></td>
                                    <td width="99%" valign="top"><table border="0" cellspacing="0" cellpadding="0" id="sevenStep" width="100%">
                                            <tr> <?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo $this->plugin("ChangeMenu",$t->step,"step");?>
                                                <td width="99%"></td>
                                            </tr>
                                    </table></td>
                                    <td valign="top"><table border="0" cellspacing="0" cellpadding="0">
                                            <tr>
                                                <td><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/closePreview.gif" alt="" width="12" height="86" /></td>
                                                <td valign="top" class="side"><!-- <img src="{webRoot}/themes/{theme}/sitebuilder/images/iconPreview.jpg" alt="" width="39" height="59" /><br />
											  		Preview  -->
                                                    <?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo $this->plugin("ChangeMenu",$t->step,"preview");?> </td>
                                            </tr>
                                    </table></td>
                                </tr>
                            </table>
                        </div>
                    <!-- End STEP -->                </td>
            </tr>
            <!-- Start DEFINE STEP -->
            <tr id="rvStepInfo">
                <td bgcolor="#FFFFFF">
                <div id="StepInfo" style="<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo htmlspecialchars($this->plugin("showHideStepInfoBar"));?>">            
                <div id="defineStep">
                <div onclick="showHideAdminMenu('tableDefineStep');switchImage('iconArrowShortcut' , 'btnHideShortcut02.gif' , 'btnHideShortcut01.gif');doAjaxStepInfoBarTagWelcome();"></div>
                	<div style="float:right;" onclick="showHideAdminMenu('tableDefineStep');switchImage('iconArrowShortcut' , 'btnHideShortcut02.gif' , 'btnHideShortcut01.gif');doAjaxStepInfoBarTagWelcome();">
                        			<img id="iconArrowShortcut" default ='<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo htmlspecialchars($this->plugin("swapTagWelcomeArrow"));?>' tooltipid ="tipWelcome" positionX='-80' positionY='-20' src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo htmlspecialchars($this->plugin("swapTagWelcomeArrow"));?>" alt="" width="11" height="11" border="0" style="cursor:pointer;" /></div>
                        			<div style="display:none" id="tipWelcome">
                                        	<div class="tooltipStep5Bdr" style="z-index:0"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("show or hide");?></div>
										</div>
                        <table cellpadding="0" cellspacing="0" width="100%">
                        	<tr>
                        		<td>
                        		    <div id="tableDefineStep" style="<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo htmlspecialchars($this->plugin("showHideTagWelcome"));?>">
									<table cellpadding="0" cellspacing="0" width="100%">
			                            <tr>
			                              <td valign="top"><?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo $this->plugin("getLogoBrand");?></td>
			                                <td width="99%" class="detail" valign="top">                                
					                              <div id="header"> <?php if (!$t->step)  {?>
					                                    <?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Home Main");?>
					                                    <?php } else {?>
					                                    <?php if ($t->mode)  {?>	
					                                    <?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo $this->plugin("stepDescription",$t->step,"stepNo",$t->mode);?> :
					                                    <?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo $this->plugin("stepDescription",$t->step,"stepName",$t->mode);?>
					                                    <?php } else {?>
					                                    <?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo $this->plugin("stepDescription",$t->step,"stepNo");?> :
					                                    <?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo $this->plugin("stepDescription",$t->step,"stepName");?>														
					                                    <?php }?>
					                                    <?php }?> </div>
					                                    <div> <?php if (!$t->step)  {?>
					                                            <?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Home Description");?>
					                                            <?php } else {?>
					                                            <?php if ($t->mode)  {?>
					                                            <?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo $this->plugin("stepDescription",$t->step,"detail",$t->mode);?>
					                                            <?php } else {?>
					                                            <?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo $this->plugin("stepDescription",$t->step,"detail");?>
					                                            <?php }?>											
					                                            <?php }?> 
					                                      </div>
			                                    </td>                              
			                            </tr>
			                        </table>
			                        </div>
                        		</td>
                        	</tr>
                        </table>          		
                 
                </div>               
                        <div style="clear:both;">
                            <!--  Start ShortCutMenu add comment for distribuild -->
                            <?php 
$x = new HTML_Template_Flexy($this->options);
$x->compile('shortcutMenu.html');
$_t = function_exists('clone') ? clone($t) : $t;
foreach(get_defined_vars()  as $k=>$v) {
    if ($k != 't') { $_t->$k = $v; }
}
$x->outputObject($_t, $this->elements);
?>
                            <!-- End ShortCutMenu -->
                    </div>
                    </div>
                    </td>
            </tr>
            <tr>
                <td><div class="hideBar">
                        <table border="0" cellspacing="0" cellpadding="0" class="bgbutton" onclick="showHideStepInfo();doAjaxStepInfoBar()" style="cursor:pointer">
                            <tr>
                                <td><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo htmlspecialchars($this->plugin("swapHideBarArrow"));?>" alt="" width="20" height="27" id="hideBarArrow" /></td>
                                <td><div><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Click to show or hide.");?></div></td>
                                <td><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/hidBar03.gif" alt="" width="11" height="27" /></td>
                            </tr>
                        </table>
                </div>

                <div id="rvDisplayMSGBOXALL">
                <div id ="rvDisplayMSGBOX">
                    <?php if (!$t->DisableResMsg)  {?>
                    <!-- Start Display Error -->
                    <div id ="rvDisplayError" align="center" style="margin-bottom:5px;"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'msgGet'))) if ($t->msgGet()) { ?><span><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'msgGet'))) echo $t->msgGet();?></span><?php }?></div>
                    <!-- End Display Error -->
                    <!-- Start Warning -->
                    <?php if ($t->error)  {?>
                    <table id =" " border="0" cellspacing="0" cellpadding="0" class="errorStep2" align="center">
                        <tr>
                            <td><ul>
                                <?php if ($this->options['strict'] || (is_array($t->error)  || is_object($t->error))) foreach($t->error as $k => $v) {?>
                                <li><?php echo $v;?></li>
                                <?php }?>
                            </ul></td>
                        </tr>
                    </table>
                    <?php }?>
                    </div>
                    <?php if ($t->errorcopy)  {?>
                    <table border="0" cellspacing="0" cellpadding="0" class="errorStep2" align="center">
                        <tr>
                            <td><ul>
                                <?php if ($this->options['strict'] || (is_array($t->errorcopy)  || is_object($t->errorcopy))) foreach($t->errorcopy as $k => $v) {?>
                                <li><?php echo $v;?></li>
                                <?php }?>
                            </ul></td>
                        </tr>
                    </table>
                    <?php }?>
                    </div>
                    <!-- End Warning Error -->
                    <?php }?> </td>
            </tr>
            <!-- End DEFINE STEP -->
            <!-- Start STEP FRAME -->
		    <?php if (!$t->step)  {?>
    <tr>
        <td id="paddingFormStep0"> <?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'outputBody'))) echo htmlspecialchars($t->outputBody());?> </td>
    </tr>
		    <?php } else {?>
    <tr> <?php if ($t->iswysiwyg)  {?>
        <td id="stepFrameWysiwyg"> <?php } else {?> </td>
        <td id="stepFrame"> <?php }?>
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                        <tr>
                            <td id="imgFrame01"></td>
                            <td width="99%" id="top"></td>
                            <td id="imgFrame02"></td>
                        </tr>
                        <tr>
                            <td id="left" valign="top"><div id="imgFrame09"></div></td>
                            <td valign="top" id="bodyBlock"><div id="titleBar">
                                    <div class="title"> <?php if ($t->mode)  {?>	
                                        <?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo $this->plugin("stepDescription",$t->step,"stepNo",$t->mode);?> :
                                        <?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo $this->plugin("stepDescription",$t->step,"stepName",$t->mode);?>
                                        <?php } else {?>
                                        <?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo $this->plugin("stepDescription",$t->step,"stepNo");?> :
                                        <?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo $this->plugin("stepDescription",$t->step,"stepName");?>													
                                        <?php }?> </div>
                                <!-- showlog js --> 
                                    <?php 
$x = new HTML_Template_Flexy($this->options);
$x->compile('dialogTool.html');
$_t = function_exists('clone') ? clone($t) : $t;
foreach(get_defined_vars()  as $k=>$v) {
    if ($k != 't') { $_t->$k = $v; }
}
$x->outputObject($_t, $this->elements);
?>
                                <!-- end showlog js -->
                                <div style="float:right;">
                                
                                <img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/help.gif" alt="" width="27" height="27" /></div>
                            </div>
                                    <div id="shadow"></div>
                                <div class="clear"></div>
                                <div> <?php if ($t->isWysiwygAllowScript)  {?>
                                        <?php 
$x = new HTML_Template_Flexy($this->options);
$x->compile('wysiwygAllowScript.html');
$_t = function_exists('clone') ? clone($t) : $t;
foreach(get_defined_vars()  as $k=>$v) {
    if ($k != 't') { $_t->$k = $v; }
}
$x->outputObject($_t, $this->elements);
?>
                                    <?php }?>
                                    <?php if ($t->componentConfigUser)  {?>
                                    <?php 
$x = new HTML_Template_Flexy($this->options);
$x->compile('rvs_usercomponent.html');
$_t = function_exists('clone') ? clone($t) : $t;
foreach(get_defined_vars()  as $k=>$v) {
    if ($k != 't') { $_t->$k = $v; }
}
$x->outputObject($_t, $this->elements);
?>
                                    <?php } else {?>
                                    <!-- START OUT PUT BODY -->
                                    <?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'outputBody'))) echo htmlspecialchars($t->outputBody());?>
                                    <!-- END OUT PUT BODY -->
                                    <?php }?> </div></td>
                            <td id="right" valign="top"><div id="imgFrame10"></div></td>
                        </tr>
                        <tr>
                            <td id="imgFrame03"></td>
                            <td id="bottom">&nbsp;</td>
                            <td id="imgFrame04"></td>
                        </tr>
                </table></td>
    	</tr>
		    <?php }?>
    <!-- End STEP FRAME -->
        </table></td>
	</tr>
	<tr>
	   <td class="footerversion">

	   		<div style="float:left;"><?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo $this->plugin("getRVSLicense");?> (v<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo $this->plugin("getRVSVersion");?>) <?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo $this->plugin("getRVSProjectId");?></div>
			<div align="right">
				<!-- icon view log -->
				<!-- 
                    <a hrefLog="{makeUrl(#view#,#viewlog#,#sitebuilder#)}" target="ifrmviewlog" onclick="loadingActivate();makeViewLogIF(this)" class="viewlog"><img src="{webRoot}/themes/{theme}/sitebuilder/images/logview.gif" alt="" width="10" height="11" border="0" align="absbottom" /> {translate(#Viewlog#):h}</a>
				-->
				<a hrefLog="<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'makeUrl'))) echo htmlspecialchars($t->makeUrl("view","viewlog","sitebuilder"));?>" target="ifrmviewlog" onclick="loadingActivate();windowRVSiteBox($('windowconfigviewlog').innerHTML, $('windowconfigviewlog'), '<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("User view log");?>'); setFormLog()" class="viewlog">
				    <img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/logview.gif" alt="" width="10" height="11" border="0" align="absbottom" /> <?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Viewlog");?>
				</a>
                
				<!-- make iframe in id ifrmviewlogDIV to load manager view log -->
				<div id ="ifrmviewlogDIV"></div>
			</div>
	   </td>
	</tr>
</table>


<?php 
$x = new HTML_Template_Flexy($this->options);
$x->compile('modalwindows/viewlog.html');
$_t = function_exists('clone') ? clone($t) : $t;
foreach(get_defined_vars()  as $k=>$v) {
    if ($k != 't') { $_t->$k = $v; }
}
$x->outputObject($_t, $this->elements);
?> 

<!-- middle column -->

<!-- footer column -->
<?php if ($t->removeFooter)  {?>
<?php } else {?>
<?php 
$x = new HTML_Template_Flexy($this->options);
$x->compile('footer.html');
$_t = function_exists('clone') ? clone($t) : $t;
foreach(get_defined_vars()  as $k=>$v) {
    if ($k != 't') { $_t->$k = $v; }
}
$x->outputObject($_t, $this->elements);
?> 
<?php }?>
<!--start sent LogMessage -->
<div id ="divViewLog">
<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) if ($this->plugin("isUserEnableLog")) { ?>
<!-- Display user log -->
<textarea style="width:99%" rows="20" readonly="readonly"><?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo $this->plugin("getUserLogMessage");?></textarea>
<?php }?>
</div>
<div>
<span style="display:none" id="defaultLoadIng"><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/loading02.gif" alt="" width="29" height="27" border="0" align="middle" />
<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("loading...");?>
</span>
</div>
