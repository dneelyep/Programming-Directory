<div id="windowconfigviewlog" style="display: none;"> <!--  -->
<div id="viewlogForm">
<form method="post" name="frm234">
    <input name="rvsMgr" type="hidden" value="Viewlog" />  
    <input name="rvsAct" type="hidden" value="savelog" />  
	<div align="center" style="padding-top:20px;">	
		<table width="300" cellpadding="4" cellspacing="0" align="left">
		<tr>
			<td align="right" width="50%"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Enabled Log View");?> :</td>
			<td align="left"><?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo $this->plugin("generateEnableViewLogOption","frmviewlog[log][enabled]");?></td>
		</tr>
		<tr>
			<td align="right"><!-- {translate(#Show Production#):h} : --></td>
			<td align="left">
		<!--Start hidden show notic message -->
		<!--End hidden show notic message -->	
			</td>
		</tr>
		<tr>
		<td align="right"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("Priority");?> :</td>	
		<td align="left">
			<select show='leightbox' name="frmviewlog[log][priority]" id="logPriority">
				<?php if ($this->options['strict'] || (isset($this) && method_exists($this, 'plugin'))) echo $this->plugin("generatePriorityViewlogSelect");?>
			</select>
		</td>
		</tr>
		<tr>
			<td align="right">&nbsp;</td>
			<td align="right" style="padding:20px 10px 10px 0;">
				<input type="button" name="submited" onclick="UserViewLogConf.viewlogsubmit($(frm234));" value="<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo htmlspecialchars($t->translate("Save"));?>" class="btnSave" />
				<input type="reset" name="cancle" OnClick="lightboxDeactivate('windowconfigviewlog');" value="<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo htmlspecialchars($t->translate("Close"));?>" class="btnCancel" />
			</td>
		</tr>
		</table>
	</div>
</form>
</div>
	<div id="viewLogLoading" style="display:none;width:500px;">
		<img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/loading02.gif" alt="" width="29" height="27" border="0" align="middle" />
		<?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate("loading...");?>
	</div>
</div>
