<?php echo $t->scriptOpen;?>
	//skip dirty form
	bSubmitted=true;
<?php echo $t->scriptClose;?>

<?php if ($t->aProjectNotInDb)  {?>

<?php echo $t->scriptOpen;?>
function checkConfirmDeleteProject() {
    strvalue = '<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo htmlspecialchars($this->plugin("translateJsMsg","Confirm delete project folder"));?>';
    actionSubmit = document.getElementById('actionSubmit').value;
    if (actionSubmit == 'delete') {
        return (confirm(strvalue)) ? true : false;
    } else {
        return true;
    }
}
<?php echo $t->scriptClose;?>

<form method="post" name="frmRestorePrject" action="<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'makeUrl'))) echo htmlspecialchars($t->makeUrl("","restoreprojectdbmissing","sitebuilder"));?>" OnSubmit="return checkConfirmDeleteProject()">

<table width="60%" border="0" cellspacing="0" cellpadding="0" align="center">
	<tr>
		<td>
		<div class="deselect">
		<div class="warningBorder" style="margin-bottom: 5px; width:100%" align="center">
		      <div class="error"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Total project missing","vprintf","countProjectNotInDb|countProjectNotInDb");?></div>
		</div>
		<div class="border">
		<div class="content">
		<ul>
			<?php if ($this->options['strict'] || (is_array($t->aProjectNotInDb)  || is_object($t->aProjectNotInDb))) foreach($t->aProjectNotInDb as $key => $projectId) {?>
			<input type="checkbox" id="aProjectData[<?php echo htmlspecialchars($projectId);?>]" name="aProjectData[<?php echo htmlspecialchars($projectId);?>]" value="<?php echo htmlspecialchars($projectId);?>">
			<label for="aProjectData[<?php echo htmlspecialchars($projectId);?>]"> <?php echo htmlspecialchars($projectId);?> </label>
			<br />
			<?php }?>
		</ul>
		</div>
		</div>
		<div class="shadow"></div>
		<div align="left">
		<input type="hidden" id ="actionSubmit" name="actionSubmit">
		  <input type="submit" id="Submit" name="Restore" value="<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Restore");?>" class="btnRestore" OnClick="Javascript:bSubmitted=true;document.getElementById('actionSubmit').value='Restore';">
		  &nbsp;&nbsp;&nbsp; 
		  <input type="submit" id="Delete" name="Delete" value="<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Delete");?>" class="btnDelete" OnClick="document.getElementById('actionSubmit').value='delete';">
		</div>
		</div>

		</td>
	</tr>
</table>
</form>
<br />

<?php }?>

<table width="100%" border="0" cellspacing="0" cellpadding="0">
	<tr>
		<td>
			<table width="100%" border="0" cellspacing="0" cellpadding="0" id="tableStep0">
				<form name="formsite" method="post" action="">
				<tr>
					<td align="right" colspan="2">
						<table border="0" cellspacing="0" cellpadding="5" width="100%">
							<tr>
								<td align="right" width="50%">
									<div>
										<input name="action" type="hidden" id="action" value="create">
										<input name="submitCreate" type="submit" id="submitted" value=" <?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Create Web Site");?>" class="btnCreateWeb" onclick="Javascript:bSubmitted=true;" />
							
									</div>
								</td>
								<td width="5"></td>
								<!-- Validate is not tryout mode and is Blog active -->
							<?php if ($t->isBlogActive)  {?> 
								<td align="left">
									<div>
										  <input name="submitBlog" type="submit" id="submitted" value=" <?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Create Blog");?>" class="btnBlog" onclick="Javascript:bSubmitted=true;" />
									</div>
								</td>									
							<?php }?>
								
                                <?php if ($t->isAllowTutorial)  {?>
								<td align="right" valign="top"> 
									<a href="#" onclick="bSubmitted=true; 
				openDialogCenter('<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'makeUrl'))) echo htmlspecialchars($t->makeUrl("view","help","sitebuilder"));?>category/rvsitebuilderhelp/page/create_project', '790', '560', '0', '0', '0', '0', '0', '0');"><img class="SPicon SPoverview" src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" tooltipid ="tipOverview" positionx='-80' positiony='-20' alt="" width="26" height="30" hspace="10" border="0" /></a>
									<div style="display:none" id="tipOverview">
										<div class="tooltipStep5Bdr" style="z-index:0"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Overview");?></div>
									</div>
								</td>
								 <?php }?>
							</tr>
						</table>
					</td>
				</tr>
				
				<?php if ($t->pidOptions)  {?>
				<tr>
					<td colspan="2"><div class="tabblue"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Edit and Remove Project.");?></div></td>
				</tr>
				<tr>
					<td align="right" width="25%">&nbsp;</td>
					<td>
						<div class="content">
							<div class="bgEdit">
								<div class="icon"><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" width="48" height="48" border="0" /></div>
								<div class="title"><label for="name" style="font-weight:bold"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Edit existing site");?></label></div>
								<div>
									<span><select name="project_id" id="editProjectList" class="menu"><?php echo $t->pidOptions;?></select></span>
									<span><input name="submitEdit" type="submit" id="submitEdit" value=" <?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Edit");?>" onclick="Javascript:bSubmitted=true;" class="btnEdit" /></span>
								</div>
							</div>
						</div>
					</td>
				</tr>
				</form>
				<?php }?>
				
				<?php if ($t->pidOptions)  {?>
				<form name="FrmRemove" method="post" action="">
				<tr>
					<td align="right">&nbsp;</td>
					<td>
						<div class="content">
							<div class="bgRemove">
								<div class="icon"><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" width="48" height="48" border="0" /></div>
								<div class="title" id="removeProjectTitle"><label for="remove" style="font-weight:bold"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Remove Project");?></label></div>
								<div>
									<span><select name="project_id" class="menu" id="removeProjectList"><?php echo $t->pidOptions;?></select></span>
									<span>
										<a href="<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'makeUrl'))) echo htmlspecialchars($t->makeUrl("","sitebuilder","sitebuilder"));?>action/ajaxReturnOutput/rvsMgr/RemoveProject/rvsAct/remove/" rel="lightbox" class="lbOn" rvstemplate="RemoveProject" returnObj="removeProjectList,editProjectList" returnOperation="refresh" param="unset" frmName="FrmRemoveProject" jsFunc="getRemoveProject('removeProjectList', 'removeProjectName', 'remove_project_id')" onMouseOver="javascript:document.getElementById('pagetitle').innerHTML = document.getElementById('removeProjectTitle').innerHTML;">
										<input name="submitRemove" type="button" id="submitRemove" value=" <?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Remove");?>" class="btnRemove" />
										</a>
									</span>
								</div>
							</div>
						</div>
						
					</td>
				</tr>
				</form>
				<?php }?>
				
			<?php if ($t->isAllowExport)  {?>	
				<?php if ($t->pidOptions)  {?>
            <form name="FrmExport" method="post" action="">
			<tr>
				<td colspan="2"><div class="tabblue"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Backup and Restore Project.");?></div></td>
			</tr>
            <tr>
                <td align="right">&nbsp;</td>
                <td>
					<div class="content">
						<div class="bgBackup">
							<div class="icon"><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" width="48" height="48" border="0" /></div>
						<div class="title" id="exportProjectTitle"><label for="remove" style="font-weight: bold"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Export Project");?></label></div>
						 <div>
							<span>
								<select name="project_id" class="menu" id="ExportProjectList">
									<?php echo $t->pidOptions;?>
								</select>
							</span> 
							<span>
							<!-- ExportProjectMgr.php , template name ExportProject.html--> 
							<a href="<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'makeUrl'))) echo htmlspecialchars($t->makeUrl("","sitebuilder","sitebuilder"));?>action/ajaxReturnOutput/rvsMgr/exportproject/rvsAct/export/" rel="lightbox" class="lbOn" rvstemplate="ExportProject" returnObj="Exporting" returnOperation="wait_inner" param="unset" loading="true" frmName="FrmExportProject" jsFunc="getValiateExportProject('<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'makeUrl'))) echo htmlspecialchars($t->makeUrl("","sitebuilder","sitebuilder"));?>action/ajaxReturnOutput/rvsMgr/exportproject/rvsAct/validateExportProject/', 'ExportProjectList', 'setExportProjectName', 'export_project_id')" onMouseOver="javascript:document.getElementById('pagetitle').innerHTML = document.getElementById('exportProjectTitle').innerHTML;">
							<input name="submitExport" type="button" id="submitExport" value=" <?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Export");?>" class="btnBackup" /> </a> 
							</span>
						 </div>
						</div>
                	</div>
                </td>
            </tr>
            </form>
            <?php }?>
            
            <?php }?>

            <?php if ($t->isAllowImport)  {?>
            <!-- Start If don't have project -->
            <?php if (!$t->pidOptions)  {?>
			<tr><td colspan="2"><div class="tabblue"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Backup and Restore Project.");?></div></td></tr>
			<?php }?>
			<!-- End If don't have project -->
            <form name="FrmExport" method="post" action="">
            <tr>
                <td align="right">&nbsp;</td>
                <td width="64%">
            		<div class="content">
						<div class="bgRestore">
							<div class="icon"><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/spacer.gif" alt="" width="48" height="48" border="0" /></div>
						<div class="title" id="importProjectTitle"><label for="remove" style="font-weight: bold"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Import Project");?></label></div>
						<div>
						   <span>
						   <!-- importprojectMgr.php , template name ImportProject.html--> 
						   <a href="<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'makeUrl'))) echo htmlspecialchars($t->makeUrl("view","importproject","sitebuilder"));?>" frmActSet="fixed" rel="lightbox" class="lbOn" rvstemplate="ImportProject" returnObj="validateImportProject" returnOperation="wait_json" param="unset" frmName="FrmImportProject" onMouseOver="javascript:document.getElementById('pagetitle').innerHTML = document.getElementById('importProjectTitle').innerHTML;">
							<input name="submitImport" type="button" id="submitImport" value=" <?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Restore");?>" class="btnRestore" style="margin-top:5px;" /> </a> 
							</span>
						</div>
					</div>
				</div>
                </td>
            </tr>
            </form>
            <?php }?>
            
			</table>
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
<div id="RemoveProject" style="display:none"><?php 
$x = new HTML_Template_Flexy($this->options);
$x->compile('RemoveProject.html');
$_t = function_exists('clone') ? clone($t) : $t;
foreach(get_defined_vars()  as $k=>$v) {
    if ($k != 't') { $_t->$k = $v; }
}
$x->outputObject($_t, $this->elements);
?></div>
<div id="ExportProject" style="display:none"><?php 
$x = new HTML_Template_Flexy($this->options);
$x->compile('ExportProject.html');
$_t = function_exists('clone') ? clone($t) : $t;
foreach(get_defined_vars()  as $k=>$v) {
    if ($k != 't') { $_t->$k = $v; }
}
$x->outputObject($_t, $this->elements);
?></div>
<div id="ImportProject" style="display:none"><?php 
$x = new HTML_Template_Flexy($this->options);
$x->compile('ImportProject.html');
$_t = function_exists('clone') ? clone($t) : $t;
foreach(get_defined_vars()  as $k=>$v) {
    if ($k != 't') { $_t->$k = $v; }
}
$x->outputObject($_t, $this->elements);
?></div> 
<!--  load disQuota user and run ajax script warning message if more than 90% . -->
<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo $this->plugin("isQuotaUser",90);?>
<!-- //end load disQuota user and run ajax script warning message if more than 90% . -->
