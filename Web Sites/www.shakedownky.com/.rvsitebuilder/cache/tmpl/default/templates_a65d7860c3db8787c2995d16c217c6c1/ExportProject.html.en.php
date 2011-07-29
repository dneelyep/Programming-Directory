<?php echo $t->scriptOpen;?>
function displayExporting()
{
	document.getElementById('Exporting').style.display = '';
	document.getElementById('displayValidateExport').style.display = 'none';
}
<?php echo $t->scriptClose;?>

<div align="center"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'msgGet'))) if ($t->msgGet()) { ?><span><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'msgGet'))) echo $t->msgGet();?></span><?php }?></div>

<form name="FrmExportProject" id="FrmExportProject" method="post" action="">
<table width="500" border="0" cellspacing="0" cellpadding="5" align="center">

	<tr>
		<td>			
			<div class="content">
				<div><strong><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Project Name");?> : <span id="setExportProjectName"><?php echo $t->project_name;?></span></strong></div>
			</div>
		</td>
	</tr>
	<!--Display STEP 2-->
	<!--Display progree by _cmd_export -->
	<tr>
		<td align="center" colspan="2" id="Exporting" style="display:none">
			<br><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Exporting");?> &nbsp;<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Please wait");?>...
			<br><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/default/images/progress_bar.gif"><br><br>
			<div class="locationButton">
				<input name="submitCancel" type="button" class="btnCancel" value="<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Close");?>" onclick="javascript: lightboxDeactivate()">
			</div>
		</td>
	</tr>

    <!--Display STEP 1-->
    <!--Display warning and Error output by _cmd_validateExportProject-->
	<tr id="displayValidateExport">
		<td>
			<div class="content">
				<div id="validateExport"></div>
			</div>
		</td>
	</tr>

	<input name="project_id" type="hidden" id="export_project_id" value="<?php echo htmlspecialchars($t->project_id);?>">

</table>
</form>