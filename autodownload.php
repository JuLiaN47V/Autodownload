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
<img src="Steam.jpg" width="20" height="17" > <br>
<input type="checkbox" name="Discord" value="1" class="checkbox" >  Discord
<img src="Discord.jpg" width="20" height="17" > <br>
<input type="checkbox" name="Chrome" value="1" class="checkbox" >  Chrome
<img src="Chrome.jpg" width="20" height="17" > <br>
<input type="checkbox" name="Notepad" value="1" class="checkbox" >  Notepad ++
<img src="Notepad.jpg" width="20" height="17" > <br>
<input type="checkbox" name="Java" value="1" class="checkbox" >  Java
<img src="Java.jpg" width="20" height="17" > <br>



<br>
<input type="submit" action="Download.php">
</form>
<br><br>





<?php

$All = "@\"%SystemRoot%\System32\WindowsPowerShell\\v1.0\powershell.exe\" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command \"iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))\" && SET \"PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin\"";

if ($_POST['WinRar'] == '1') {
	$WinRar = "choco install winRar -y --Force";}

if ($_POST['Steam'] == '1') {
	$Steam = "choco install steam -y --Force";}

if ($_POST['Discord'] == '1') {
    $Discord = "choco install discord -y --Force";}

if ($_POST['Chrome'] == '1') {
    $Chrome = "choco install googlechrome -y --Force";}
	
if ($_POST['Notepad'] == '1') {
    $Notepad = "choco install notepadplusplus -y --Force";}
	
if ($_POST['Java'] == '1') {
    $Java = "choco install jre8 -y --Force";}


$file = fopen("autoinstall.bat","w");
fwrite($file,"$All
$WinRar
$Steam
$Discord
$Chrome
$Notepad
$Java







");
fclose($file);





	
		
		
		
		?>







</body>

</html>


