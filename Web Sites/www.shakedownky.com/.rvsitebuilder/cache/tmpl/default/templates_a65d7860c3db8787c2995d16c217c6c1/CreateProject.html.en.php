<form method="post" id="FrmCreate" name="FrmCreate" enctype="multipart/form-data" action="">
<!-- <div align="center"><span flexy:if="msgGet()">{msgGet():h}</span></div> -->
<table width="100%" border="0" cellspacing="0" cellpadding="0">
	<tr>
		<td id="paddingForm">
			<div>

				<table cellpadding="2" cellspacing="0" id="topSelect" align="right">
					<tr>
						<td><input name="no_company_name" type="checkbox" id="no_company_name" value="checked" <?php echo htmlspecialchars($t->checked_no_company_name);?> onclick="companyBox()" /></td>
						<td><label for="no_company_name"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("No Company Name");?></label></td>
						<td><input name="no_slogan" type="checkbox" id="no_slogan" value="checked" <?php echo htmlspecialchars($t->checked_no_slogan);?> onclick="sloganBox()" /></td>
						<td><label for="no_slogan"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("No Slogan");?></label></td>	
						<td><input name="no_logo" type="checkbox" id="no_logo" <?php echo htmlspecialchars($t->checked_no_logo);?> value="checked" onclick="LogoBox()" /></td>
						<td><label for="no_logo"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("No Logo");?></label></td>
					</tr>
				</table>
			</div>
			<div class="clear" align="center">
				<div id="formCreate">
					<table width="100%" border="0" cellspacing="0" cellpadding="0">
						<script type="text/javascript" src="<?php echo htmlspecialchars($t->webRoot);?>/js/inlinehelp.js"></script>
						<?php if ($t->error['project_name'])  {?>
						<tr>
							<td>
								<div style="width:40%;"><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" /></div>
								<div id="warningInform"><?php echo $t->error['project_name'];?></div>
							</td>
						</tr>
						<?php }?>
						
						<tr>
							<td class="normal">
							 	<div style="width:40%;"><label for="project_name"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Project Name");?>  :</label></div>
								
								<div>
								    <input name="project_name" type="text" id="project_name" value="<?php echo $t->project_name;?>" class="width" />	
								</div>
                                <div class="left" style="margin-top:3px;">
                                    <span class="inlinehelp" onmouseover="this.className='inlinehelpOver';" onMouseOut="this.className='inlinehelp';"> <img class="SPicon SPtooltiphelp" src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" width="16" height="16" border="0" />
								    <span style="margin:0px 0 0 10px;"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("help Project Name");?></span>
								</div>
								
							</td>
						</tr>
						
						<?php if ($t->error['project_charset'])  {?>
						<tr>
							<td>
								<div style="width:40%;"><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" /></div>
								<div id="warningInform"><?php echo $t->error['project_charset'];?></div>
							</td>
						</tr>
						<?php }?>						
						
						<tr>
							<td class="normal">
								<div style="width:40%;"><label for="project_charset"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Web Site Langauge");?>  :</label></div>
								<div>
									<select name="project_charset" id="project_charset" onChange="Javascript:bSubmitted=true; changLang()" class="menu" style="width:155px;" <?php echo htmlspecialchars($t->isprojectChangeLang);?>>
										<?php echo $t->langOptions;?>
									</select>
									<?php if ($t->isprojectChangeLang)  {?>
									   <input type="hidden" name="project_charset" value="<?php echo htmlspecialchars($t->selectLangDisableKey);?>" />
									<?php }?>
								</div>
                                <div class="left" style="margin-top:3px;">
                                    <span class="inlinehelp" onmouseover="this.className='inlinehelpOver';" onMouseOut="this.className='inlinehelp';"> <img class="SPicon SPtooltiphelp" src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" width="16" height="16" border="0" />
									<span style="margin:-110px 0 0 10px;"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("help Web Site Language");?></span>
								</div>
								<?php if (!$t->projectChangeLang)  {?>
							     <div class="left" style="margin-top:3px;">
                                <span class="inlinehelp" onmouseover="this.className='inlinehelpOver';" onMouseOut="this.className='inlinehelp';"> <img class="SPicon SPtooltiphelp" src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" width="16" height="16" border="0" />
                                    <span style="margin:-30px 0 0 20px;"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo htmlspecialchars($t->translate("Admin disable project change laguage."));?></span>
                                </div>
                                <?php }?>
							</td>
						</tr>

						<tr>
							<td class="normal">
							 	<div style="width:40%;"><label for="project_title"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Web Site Title");?> :</label></div>
								<div>
										<input name="project_title" type="text" id="project_title" value="<?php echo $t->project_title;?>" class="text width" />
								</div>
                                <div class="left" style="margin-top:3px;">
                                    <span class="inlinehelp" onmouseover="this.className='inlinehelpOver';" onMouseOut="this.className='inlinehelp';"> <img class="SPicon SPtooltiphelp" src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" width="16" height="16" border="0" />
										<span style="margin:-110px 0 0 10px;"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("help Web Site Title","vprintf","SB_IMG_URL|SB_IMG_URL");?></span>
								</div>
							</td>
						</tr>
						
						
						<?php if ($t->error['project_company'])  {?>
						<tr>
							<td>
								<div style="width:40%;"><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" /></div>
								<div id="warningInform"><?php echo $t->error['project_company'];?></div>
							</td>
						</tr>
						<?php }?>				
						
						<tr>
							<td class="normal">
							 	<div style="width:40%;">
							 		<label for="project_company" id="project_company_label">
							 			<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Company");?> :<br />
							 			<font class="f10b_green"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("HTML tag allowed.");?></font>
							 		</label>
							 	</div>
								<div>
									<?php if ($t->error['project_company'])  {?><div class="error"><?php echo $t->error['project_company'];?></div><?php }?>
									<div>
									   <input name="project_company" type="text" id="project_company" value="<?php echo htmlspecialchars($t->project_company);?>" class="text width" />
									</div>
                                    <div class="left" style="margin-top:3px;">
                                        <span class="inlinehelp" onmouseover="this.className='inlinehelpOver';" onMouseOut="this.className='inlinehelp';"> <img class="SPicon SPtooltiphelp" src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" width="16" height="16" border="0" />
									   <span style="margin:-110px 0 0 10px;"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("help Company Name2");?></span>
									</div>
								</div>
							</td>
						</tr>
						<tr>
							<td class="normal">
							 	<div style="width:40%;">
							 		<label for="project_slogan" id="project_slogan_label">
							 			<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Slogan");?> :<br />
							 			<font class="f10b_green"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("HTML tag allowed.");?></font>
							 		</label>
							 	</div>
								<div>
									<input name="project_slogan" type="text" id="project_slogan" value="<?php echo htmlspecialchars($t->project_slogan);?>" class="text width" />
								</div>
                                <div class="left" style="margin-top:3px;">
                                    <span class="inlinehelp" onmouseover="this.className='inlinehelpOver';" onMouseOut="this.className='inlinehelp';"> <img class="SPicon SPtooltiphelp" src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" width="16" height="16" border="0" />	
									<span style="margin:-110px 0 0 10px;"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("help Slogan");?></span>
								</div>
							</td>
						</tr>
						<?php if ($t->error['project_logo'])  {?>
						<tr>
							<td>
								<div style="width:40%;"><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" /></div>
								<div id="warningInform"><?php echo $t->error['project_logo'];?></div>
							</td>
						</tr>
						<?php }?>
						<tr>
							<td class="normal">
							 	<div style="width:40%;">
							 		<label for="project_logo" id="project_logo_label"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Logo");?> :<br /><font class="f10b_green"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("recommended size 120 x 70");?></font></label>							 	
							 	</div>
								<div>
									<input name="project_logo" type="file" id="project_logo" size="26" />
									
									<br />
									<input name="autoresize_logo" type="checkbox" id="autoresize_logo" <?php echo htmlspecialchars($t->checked_no_logo);?> value="checked" />
									<label for="autoresize_logo" id="autoresize_logo_label"><font class="f10b_green"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Auto Resize");?></font></label>
								</div>
								<div class="left" style="margin-top:3px;">
								<span class="inlinehelp" onmouseover="this.className='inlinehelpOver';" onMouseOut="this.className='inlinehelp';"> <img class="SPicon SPtooltiphelp" src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" width="16" height="16" border="0" />
									<span style="margin:-150px 0 0 0px;"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("help Logo");?></span>
								</div>
							</td>
						</tr>
						
						<?php if ($t->show_logo)  {?>
						<tr>
							<td class="normal">
								<div style="width:40%;"><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" /></div>
								<div>
									<img src="<?php echo htmlspecialchars($t->show_logo);?>?<?php echo htmlspecialchars($t->rndMcTime);?>" border="0" <?php echo $t->setautoresize;?>>
								</div>
							</td>
						</tr>
						
										
						<?php }?>
						
						
						<tr>
							<td>
								<div style="width:40%;"><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" /></div>
								<div><input class="btnUpload" type="submit" name="submitted" value=" <?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Upload Logo");?>" onclick="bSubmitted=true;" /></div>
								<?php if ($t->show_logo)  {?> 		
								<div>
									<input name="DeletedLogo" type="submit" class="btnRemove" value="<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Remove Logo");?>" onclick="javascript:delLogo.value='Yes';bSubmitted=true;">
									<input name="delLogo" type="hidden" id="delLogo2">
									<input name="show_logo" type="hidden" id="show_logo2" value="<?php echo htmlspecialchars($t->show_logo);?>">
									<input name="logoNameDel" type="hidden" id="logoNameDel" value="<?php echo htmlspecialchars($t->project_logo);?>">
								</div>
								<?php }?>
							</td>
						</tr>						
					</table>
					<br />
				<?php if ($t->isPro)  {?><!-- start check isPro -->
				    <?php if ($t->sessionBlog)  {?><!-- start check session -->
					   <?php if (!$t->editBlog)  {?><!-- start edit -->
					<hr color="#999999" size="1" width="60%" />
					<table id="frmCretaeDB" border="0" cellspacing="3" cellpadding="0" width="100%">
                        <tr>
                            <td colspan="2" height="20" valign="top" style="padding-left:130px;"><div align="left"><b><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo htmlspecialchars($t->translate("Database Setting"));?> </b></div>
                          </td>
                        </tr>
                        <tr>
                        <td colspan="2" height="30"><center> <?php echo $t->compoDBmsgBox;?> </center>
                        </td>
                        </tr>
                        <tr>
                            <td align="right" width="40%"><label for="dbHostName"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo htmlspecialchars($t->translate("HostName"));?> :</label></td>
                            <td align="left"><div align="left"><input type ="text" id="dbHostName" style="width:150px;" name ="compoDB[HostName]" value="<?php echo htmlspecialchars($t->compoDB['HostName']);?>"></div></td>
                        </tr>
                        <tr>
					        <td align="right"><label for="dbPortName"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo htmlspecialchars($t->translate("Port"));?> :</label></td>
					        <td align="left"><div align="left"><input type ="text" id="dbProtocal" style="width:150px;" name ="compoDB[Port]" value="<?php echo htmlspecialchars($t->compoDB['Port']);?>"></div></td>
					    </tr>
						<tr>
					        <td align="right"><label for="dbName"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo htmlspecialchars($t->translate("DatabaseName"));?> :</label></td>
							<td align="left"><div align="left"><input type ="text" id="dbName" style="width:150px;" name ="compoDB[DatabaseName]" value="<?php echo htmlspecialchars($t->compoDB['DatabaseName']);?>"></div></td>
					    </tr>
					    <tr>
					        <td align="right"><label for="dbUserName"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo htmlspecialchars($t->translate("UserName"));?> :</label></td>
					        <td align="left"><div align="left"><input type ="text" id="dbUserName" style="width:150px;" name ="compoDB[UserName]" value="<?php echo htmlspecialchars($t->compoDB['UserName']);?>"></div></td>
					    </tr>
					    <tr>
					        <td align="right"><label for="Password"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo htmlspecialchars($t->translate("Password"));?> :</label></td>
					        <td align="left"><div align="left"><input type ="password" style="width:150px;" id="Password" name ="compoDB[Password]" value="<?php echo htmlspecialchars($t->compoDB['Password']);?>"></div><br>
					   </td>
					   <!-- Don't work
					   <tr>
					        <td align="right" height="10" colspan="2"></td>
					   </td>
					   <tr>
					        <td align="right"></td>
					        <td align="left"><div align="left">
					        	<input type="checkbox" id="autocreatedb" name="autocreatedb" value="1"> 
					        	<label for="autocreatedb">{translate(#Generate new MySQL database automatically if not exist.#):h}</label></div><br>
					   </td>
					   -->
					    </tr>
					</table>
					   <?php }?><!-- end check session -->
					<?php }?><!-- end check edit blog-->
				<?php }?> <!-- end check isPro -->

				</div>
				<div align="left"> 
					<input type="hidden" name="project_domain" value="<?php echo htmlspecialchars($t->project_domain);?>" />
					<input type="hidden" name="project_description" value="<?php echo htmlspecialchars($t->project_description);?>" />
					<input type="hidden" name="project_keyword" value="<?php echo htmlspecialchars($t->project_keyword);?>" />
					<input type="hidden" name="action" value="<?php echo htmlspecialchars($t->project_action);?>" />
				</div>
				<div align="right"><input type="submit" name="submit_save" value="<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Save");?>" onclick="Javascript:bSubmitted=true;" class="btnSave" /></div>
			</div>
		</td>
	</tr>
</table>
</form>
<?php 
$x = new HTML_Template_Flexy($this->options);
$x->compile('rvs_ajaxpopup.html');
$_t = function_exists('clone') ? clone($t) : $t;
foreach(get_defined_vars()  as $k=>$v) {
    if ($k != 't') { $_t->$k = $v; }
}
$x->outputObject($_t, $this->elements);
?>