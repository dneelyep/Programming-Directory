
<form name="FrmRemoveProject" id="FrmRemoveProject" method="post" action="">
<table width="100%" border="0" cellspacing="0" cellpadding="0">
	<tr>
		<td>

		</td>
	</tr>
	
	<tr>
		<td>
			<table border="0" cellspacing="0" cellpadding="0" class="warningBorder" align="center">
				<tr>
					<td class="error"><label><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Click \"Remove\" to confirm delete project.");?></td>
				</tr>
			     <?php if ($t->error)  {?> 
        			<?php if ($this->options['strict'] || (is_array($t->error)  || is_object($t->error))) foreach($t->error as $k => $v) {?><tr><td class="error"><?php echo $v;?></td></tr><?php }?>
        		<?php }?> 	
			</table><br />			
		
		
			<table width="100%" border="0" cellspacing="0" cellpadding="0">
				<tr>
					<td width="20%">&nbsp;</td>					
					<td>
						<div class="content">
							<div><strong><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Project Name");?> : <span id="removeProjectName"><?php echo $t->project_name;?></span></strong></div>
							<div>
								<input name="removeFolderPublish" id="removeFolderPublish" type="checkbox" value="1" class="bclear">
								<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Do you want to remove folder published all web site.");?>
							</div>
							
							<div class="locationButton">
							    <input name="project_id" type="hidden" id="remove_project_id" value="<?php echo htmlspecialchars($t->project_id);?>">
							    <input name="submitRemoveProject" type="submit" class="btnRemove" value="<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Remove");?>" onclick="Javascript:bSubmitted=true;"> 
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