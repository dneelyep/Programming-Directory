<?php echo $t->scriptOpen;?>
function displayValidateImport()
{
	document.getElementById('validateImportProject').style.display = '';
	document.getElementById('confirmImport').style.display = 'none';	
}


function setFormActionForConfirmImport()
{
	objFormImport = document.getElementById('FrmImportProject');
	document.getElementById('FrmImportProject').action = "<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'makeUrl'))) echo htmlspecialchars($t->makeUrl("import","importproject","sitebuilder"));?>";
}

function displayProgessBar(visible)
{
    document.getElementById('ProgessBar').style.display = visible;
    
    if (visible == 'none') {
        document.getElementById('validateImportProject').style.display = '';
     } else {
        document.getElementById('validateImportProject').style.display = 'none';
     }
}

function backToStart()
{
    document.getElementById('ProgessBar').style.display = 'none';
    document.getElementById('validateImportProject').style.display = 'none';
    document.getElementById('confirmImport').style.display = '';

}

<?php echo $t->scriptClose;?>

<form name="FrmImportProject" id="FrmImportProject" method="post" enctype="multipart/form-data" action="" onsubmit="return AIM.submit(this, '','AIM_OUTPUT','validateImportProject')">
<table width="100%" border="0" cellspacing="0" cellpadding="0">
	
	<tr>
        <td id="ProgessBar" align="center" style="display:none">
            <br>
             <?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Please wait");?>...
            <br>
            <img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/default/images/progress_bar.gif"><br><br>
                            <div class="locationButton">
                                <input name="submitCancel" type="button" class="btnCancel" value="<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Cancel");?>" onclick="javascript: lightboxDeactivate()">
                            </div>
        </td>
    </tr>
	
	<tr>
		<td id="validateImportProject" align="center" style="display:none">
		</td>
	</tr>
	
	<tr>
		<td id="confirmImport" class="AIM_onComleteHide">
			<table width="100%" border="0" cellspacing="0" cellpadding="0">
				<tr>
					<td width="3%">&nbsp;</td>					
					<td>
						<div class="content">
						    <br />
							<div><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Select file");?>
								<input type="file" name="importProjectFile">
							</div>

				            <div class="locationButton">
							    <input name="project_id" type="hidden" id="import_project_id" value="<?php echo htmlspecialchars($t->project_id);?>">
							    <input name="submitValidateImport" type="submit" class="btnSubmit" value="<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Submit");?>" onclick="Javascript:bSubmitted=true;displayValidateImport()"> 
							    &nbsp;&nbsp;&nbsp;
							    <input name="submitCancel" type="button" class="btnCancel" value="<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Cancel");?>" onclick="javascript: lightboxDeactivate()">
							</div>
						
						</div>
					</td>
				</tr>				
			</table>
		</td>
	</tr>
</table>
</form>