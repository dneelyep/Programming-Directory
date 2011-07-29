<div id ="dialogLog" style="display:none;position:absolute;width:580px;text-align: center; cursor:move;background:#fff; border:1px solid #333;">
    <div style="text-align: right;background:url('<?php echo htmlspecialchars($t->webRoot);?>/themes/<?php echo htmlspecialchars($t->theme);?>/sitebuilder/images/titleBar.gif');">
        <input type="text" id="bBar" onkeyup="logBrowserBarOnkeyUp(this,event)">
        <input type="button" onclick ="shwBar(this)" value=">"> 
        <input type="checkbox" id="logPesterScrolbar" />pester scrolbar
        <input type="button" onclick ="runScriptRVdebug()" value="run script">
        <input type="button" value="clear" onclick="dialogLogActClear();">
        <input type="button" value="X" onclick="dialogLogActEnd();">
    </div>
<div>
    <iframe id="bIF" style="display:none;position:absolute;left:0px;size:"></iframe>
    <div id="logShowPro" style="width:580px;overflow: auto;" onmouseover="this.style.cursor='pointer'"></div>
  </div>
  </div>
  