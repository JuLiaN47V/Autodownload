<?php

$All = "@\"%SystemRoot%\System32\WindowsPowerShell\\v1.0\powershell.exe\" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command \"iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))\" && SET \"PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin\"";

if ($_POST['WinRar'] == '1') {
	$WinRar = "choco install WinRar -y --Force";}

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

header("Content-disposition: attachment; filename=autoinstall.bat");
header("Content-type: application/bat");
readfile("autoinstall.bat");
exit;




?>

