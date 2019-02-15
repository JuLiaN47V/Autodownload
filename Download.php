<?php

header("Content-disposition: attachment; filename=autoinstall.bat");
header("Content-type: application/bat");
readfile("autoinstall.bat");
exit;

?>
