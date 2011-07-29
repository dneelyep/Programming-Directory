<table cellpadding="0" cellspacing="0" id="rvs_popupTopTable" width="50%" align="center">
	<tr>
		<td id="framePopup">
			<table width="500" border="0" cellspacing="0" cellpadding="0">
				<tr>
					<td><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/framePopup01.gif" alt="" width="8" height="8" /></td>
					<td width="99%" id="topframe" bgcolor="#F1F1F1"></td>
					<td><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/framePopup03.gif" alt="" width="6" height="8" /></td>
				</tr>
				<tr>
					<td valign="top" id="left"><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/framePopup04.gif" alt="" width="8" height="28" /></td>
					<td valign="top" id="blockPopup">
						<div>
							<div id="titleBar">
								<div class="title" id="pagetitle"><?php echo $t->OnlineFlashPreview;?></div>
								<div style="float:right;"><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/help_popup.gif" alt="" width="27" height="27" /></div>
							</div>
							<div id="shadow"></div>
							<div class="clear"></div>
							<div>
								<table width="100%" border="0" cellspacing="0" cellpadding="0">
									<tr>
										<td id="rvsPopUpHtmlContent">
											<?php echo $t->rvsPopUpContent;?>
											
										</td>
									</tr>
								</table>
							</div>
						</div>
					</td>
					<td valign="top" id="right"><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/framePopup05.gif" alt="" width="6" height="28" /></td>
				</tr>
				<tr>
					<td><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/framePopup08.gif" alt="" width="8" height="6" /></td>
					<td id="bottom"></td>
					<td><img src="<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/framePopup10.gif" alt="" width="6" height="6" /></td>
				</tr>
			</table>
		</td>
	</tr>
</table>