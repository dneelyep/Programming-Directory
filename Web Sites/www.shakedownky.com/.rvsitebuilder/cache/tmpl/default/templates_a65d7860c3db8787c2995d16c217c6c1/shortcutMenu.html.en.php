

<div id="debugShortCutMenu" style="display:none">
moseX<div id="debugShortCutMenuMouseX">0</div>
image width<div id="debugShortCutMenuImageWidth">0</div>
</div>
	<div>
		<div style="background-color:#F7F8F8; padding-top:2px;"></div>
		<div style="background-color:#C0CCD1; padding-top:1px;"></div>	
	<!-- Start menu 
	<input type="button" onclick="document.getElementById('a').value = document.getElementById('nav').innerHTML" />
	<textarea id="a" name="a"> </textarea>-->
		<div id="menu" class="corner">
			<ul id="nav">
					<?php if ($this->options['strict'] || (is_array($t->aShortCutMenu)  || is_object($t->aShortCutMenu))) foreach($t->aShortCutMenu as $shortKey => $shortValue) {?>
					<li>
						<a href="#" id="navS<?php echo htmlspecialchars($shortValue['tabID']);?>" headShortcut ="true" onclick="switchEffectAttribute('nav', 'navS<?php echo htmlspecialchars($shortValue['tabID']);?>', 'headShortcut', 'class' ,'activeme','')
									 switchEffectAttribute('tableShortcut', 'trShortCut<?php echo htmlspecialchars($shortValue['tabID']);?>', 'shortcut', 'display')
						"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate($shortKey);?></a>	
					</li>
					<?php }?>
			</ul>
		</div>
		<div class="clearit"></div>
	<!-- End menu -->
		
	<!-- Start Loop Table -->
		<div id="shortcutlist">	
			<table cellpadding="0" cellspacing="0" width="85%" id ="tableShortcut">
				<tr>
					<td valign="top" class="scubrand"></td>
					<td valign="top" width="99%">
						<table cellpadding="0" cellspacing="0" class="sc_contents" width="100%">
							
							<?php if ($this->options['strict'] || (is_array($t->aShortCutMenu)  || is_object($t->aShortCutMenu))) foreach($t->aShortCutMenu as $shortcutKey => $shortcutValue) {?>
								<tr id="trShortCut<?php echo htmlspecialchars($shortcutValue['tabID']);?>" style="display:none;" shortcut='true'>
									<td align="left" valign="top">
										<table cellpadding="0" cellspacing="0" width="100%">
											<tr>
												<td width="33%" align="left" valign="top"></td>
												<td width="33%" align="left" valign="top"></td>
												<td align="left" valign="top"></td>
											</tr>
											<tr>
											<?php if ($this->options['strict'] || (is_array($shortcutValue['tabData'])  || is_object($shortcutValue['tabData']))) foreach($shortcutValue['tabData'] as $shortcutTabDataKey => $shortcutTabDataValue) {?>
												<td align="left" valign="top" id="TD<?php echo htmlspecialchars($shortcutTabDataValue['divID']);?>">
						<?php if ($shortcutTabDataValue['helpOnly'])  {?>
												
												<img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/scbullet.gif" alt="" width="5" height="5" hspace="2" />
												<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate($shortcutTabDataKey);?>
												<?php if ($shortcutTabDataValue['textHelpKey'])  {?>
													<a id ="aLink<?php echo htmlspecialchars($shortcutTabDataValue['divID']);?>" onmouseover="
                                                    getDataShortCut('<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'makeUrl'))) echo htmlspecialchars($t->makeUrl("","tooltip","sitebuilder"));?>action/ajaxRunManager/rvsMgr/ToolTipMgr/rvsAct/viewtooltip/textHelpKey/<?php echo htmlspecialchars($shortcutTabDataValue['textHelpKey']);?>/width/<?php echo htmlspecialchars($shortcutTabDataValue['width']);?>/height/<?php echo htmlspecialchars($shortcutTabDataValue['height']);?>', '<?php echo htmlspecialchars($shortcutTabDataValue['divID']);?>' , '<?php echo htmlspecialchars($shortcutTabDataValue['width']);?>');
                                                    document.getElementById('span<?php echo htmlspecialchars($shortcutTabDataValue['divID']);?>').setAttribute('class','shortcuthelpOver');document.getElementById('span<?php echo htmlspecialchars($shortcutTabDataValue['divID']);?>').setAttribute('className','shortcuthelpOver');
                                                    " onmouseout="document.getElementById('span<?php echo htmlspecialchars($shortcutTabDataValue['divID']);?>').setAttribute('class','shortcuthelp'),document.getElementById('span<?php echo htmlspecialchars($shortcutTabDataValue['divID']);?>').setAttribute('className','shortcuthelp');"><img class="SPicon SPscques" src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" width="14" height="14" align="absmiddle" /></a>
                                                    <span id="span<?php echo htmlspecialchars($shortcutTabDataValue['divID']);?>" classname="shortcuthelp" class="shortcuthelp">
                                                        <span id="img_<?php echo htmlspecialchars($shortcutTabDataValue['divID']);?>"><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/loading02.gif" alt="" width="29" height="27" border="0" align="middle" /><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("loading...");?></span>                                                </span>
												<?php } else {?>
												<!-- image(?) disable -->
												<?php if ($shortcutTabDataValue['enabletooltip'])  {?>
												<img class="SPicon SPscquesdis" src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" width="6" height="8" align="absmiddle" />
												<?php }?>
												<?php }?>
												
												<!-- display flash help link -->
												<?php if ($shortcutTabDataValue['flashPath'])  {?>
													<a onclick="bSubmitted=true; openDialogCenter('<?php echo htmlspecialchars($shortcutTabDataValue['flashPath']);?>', '790', '560', '0', '0', '0', '0', '0', '0');" href="#">
													<img class="SPicon SPvdohelp" src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" width="12" height="13" align="absmiddle" border="0" /></a>
												<?php }?>
												
						<?php } else {?>
												<?php if ($shortcutTabDataValue['enable'])  {?>
												
													<!--  shortcut  enable = 1 -->
													<img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/scbullet.gif" alt="" width="5" height="5" hspace="2" />
													<a href="<?php echo htmlspecialchars($shortcutTabDataValue['urlPath']);?>" target="<?php echo htmlspecialchars($shortcutTabDataValue['target']);?>"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate($shortcutTabDataKey);?></a>
												<?php } else {?>
												
													<img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/scbulletdis.gif" alt="" width="5" height="5" hspace="2" />
													<font class="ShortcutDisable"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate($shortcutTabDataKey);?></font>
												<?php }?>
												
												<!--    helpKey -->
												<!--   {shortcutTabDataValue[width]}   -->
												<!--   {shortcutTabDataValue[height]}  -->
												<?php if ($shortcutTabDataValue['textHelpKey'])  {?>
											
													<a id ="aLink<?php echo htmlspecialchars($shortcutTabDataValue['divID']);?>" onmouseover="
													getDataShortCut('<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'makeUrl'))) echo htmlspecialchars($t->makeUrl("","tooltip","sitebuilder"));?>action/ajaxRunManager/rvsMgr/ToolTipMgr/rvsAct/viewtooltip/textHelpKey/<?php echo htmlspecialchars($shortcutTabDataValue['textHelpKey']);?>/width/<?php echo htmlspecialchars($shortcutTabDataValue['width']);?>/height/<?php echo htmlspecialchars($shortcutTabDataValue['height']);?>', '<?php echo htmlspecialchars($shortcutTabDataValue['divID']);?>' , '<?php echo htmlspecialchars($shortcutTabDataValue['width']);?>');
													document.getElementById('span<?php echo htmlspecialchars($shortcutTabDataValue['divID']);?>').setAttribute('class','shortcuthelpOver');document.getElementById('span<?php echo htmlspecialchars($shortcutTabDataValue['divID']);?>').setAttribute('className','shortcuthelpOver');
													" onmouseout="document.getElementById('span<?php echo htmlspecialchars($shortcutTabDataValue['divID']);?>').setAttribute('class','shortcuthelp'),document.getElementById('span<?php echo htmlspecialchars($shortcutTabDataValue['divID']);?>').setAttribute('className','shortcuthelp');"><img class="SPicon SPscques" src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" width="14" height="14" align="absmiddle" /></a>
													<span id="span<?php echo htmlspecialchars($shortcutTabDataValue['divID']);?>" classname="shortcuthelp" class="shortcuthelp">
														<span style="" id="img_<?php echo htmlspecialchars($shortcutTabDataValue['divID']);?>"><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/loading02.gif" alt="" width="29" height="27" border="0" align="middle" /><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("loading...");?></span>												</span>
												<?php } else {?>
												<!-- image(vdo_help) disable -->
												<?php if ($shortcutTabDataValue['enabletooltip'])  {?>
												<img class="SPicon SPscquesdis" src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" width="6" height="8" align="absbottom" hspace="2">
												<?php }?>
												<?php }?>
												
												
												<!-- display flash help link -->
												<?php if ($shortcutTabDataValue['flashPath'])  {?>
													<a onclick="bSubmitted=true; openDialogCenter('<?php echo htmlspecialchars($shortcutTabDataValue['flashPath']);?>', '790', '560', '0', '0', '0', '0', '0', '0');" href="#">
													<img class="SPicon SPvdohelp" src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" width="12" height="13" align="absmiddle" border="0" /></a>
												<?php }?>	
											<?php }?>												</td>
												<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) if ($this->plugin("isCountTd",3,$shortcutValue['tabData'])) { ?>
											</tr>
       											<?php }?>
											<?php }?>
											<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) if ($this->plugin("isCheckColspan")) { ?>
										        	<td colspan="<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo htmlspecialchars($this->plugin("isCheckColspan"));?>" align="left" valign="top">&nbsp;</td>
    											</tr>
											<?php }?>
											<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo htmlspecialchars($this->plugin("isCheckColspan",3,"unset"));?>
											
										</table>										
									</td>
								</tr>
							<?php }?>
							
						</table>
					</td>
				</tr>
			</table>	
			
		</div>
	</div>	
	
	<!-- End Loop Table -->	
<?php echo $t->scriptOpen;?>
 switchEffectAttribute('nav', 'navS<?php echo htmlspecialchars($t->aShortCutMenu['thisstep']['tabID']);?>', 'headShortcut', 'class', 'activeme');
 switchEffectAttribute('tableShortcut', 'trShortCut<?php echo htmlspecialchars($t->aShortCutMenu['thisstep']['tabID']);?>', 'shortcut', 'display')
<?php echo $t->scriptClose;?>
		
	