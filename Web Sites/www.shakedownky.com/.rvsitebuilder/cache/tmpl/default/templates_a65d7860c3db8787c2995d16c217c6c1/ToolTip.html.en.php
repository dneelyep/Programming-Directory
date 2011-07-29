<?php if ($t->toolTipUrl)  {?>
	<?php if ($t->isMedia)  {?>
		<object width="<?php echo htmlspecialchars($t->width);?>" height="<?php echo htmlspecialchars($t->height);?>" classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,19,0">
			<param name="movie" value="<?php echo htmlspecialchars($t->toolTipUrl);?>" />
			<param name="quality" value="high" />
			<embed src="<?php echo htmlspecialchars($t->toolTipUrl);?>" quality="high" pluginspage="http://www.macromedia.com/go/getflashplayer" type="application/x-shockwave-flash" width="<?php echo htmlspecialchars($t->width);?>" height="<?php echo htmlspecialchars($t->height);?>"></embed>
		</object>		
	<?php } else {?>
   		<img src="<?php echo htmlspecialchars($t->toolTipUrl);?>" alt="" width="<?php echo htmlspecialchars($t->width);?>" height="<?php echo htmlspecialchars($t->height);?>">
    <?php }?>
    <?php if ($t->description)  {?>

    	<table cellpadding="3" cellspacing="0" width="454" align="left">
			<tr><td align="left" valign="top"><?php if ($this->options['strict'] || (isset($t) && method_exists($t, 'translate'))) echo $t->translate($t->description);?></td></tr>
		</table>
    <?php }?>
<?php }?>


