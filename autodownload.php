<html>
<style rel="stylesheet" type="text/css">
.checkbox {
  float: left;
  margin: 0 0 0 17px;
  width: 20px;
  height: 20px;
}
</style>

<body>
<form method="POST" action="autodownload.php">
<input type="checkbox" name="WinRar" value="1" class="checkbox"> Winrar
<img src="Winrar.jpg" width="20" height="17"> <br>
<input type="checkbox" name="Steam" value="1" class="checkbox" >  Steam
<img src="Winrar.jpg" width="20" height="17" > <br>
<input type="checkbox" name="Discord" value="1" class="checkbox" >  Discord




<br><input type="submit"><br><br>





<?php

echo "Find-Packageprovider -name Chocolatey -Force <br>";

if ($_POST['WinRar'] == '1') {
	$WinRar = "Install-Package Winrar -provider Chocolatey -Force";
	}

if ($_POST['Steam'] == '1') {
	$Steam = "Install-Package Steam -provider Chocolatey -Force";}

if ($_POST['Discord'] == '1') {
    $Discord = "Install-Package Discord -provider Chocolatey -Force";}


$file = fopen('autoinstall.bat', 'w');
fwrite($file,$WinRar);
fclose($file);
		
		
		
		
		
		
		
		
		
		?>







</body>

</html>


