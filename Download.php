<?php

$Admin = "@echo off\n>nul 2>&1 \"%SYSTEMROOT%\system32\cacls.exe\" \"%SYSTEMROOT%\system32\config\system\"\nif \'%errorlevel%\' NEQ \'0\' (\n    echo Requesting administrative privileges...\n    goto UACPrompt\n) else ( goto gotAdmin )\n:UACPrompt\n    echo Set UAC = CreateObject^(\"Shell.Application\"^) > \"%temp%\getadmin.vbs\"\n    echo UAC.ShellExecute \"%~s0\", \"\", \"\", \"runas\", 1 >> \"%temp%\getadmin.vbs\"\n\n    \"%temp%\getadmin.vbs\"\n    exit /B\n\n:gotAdmin\n    if exist \"%temp%\getadmin.vbs\" ( del \"%temp%\getadmin.vbs\" )\n    pushd \"%CD%\"\n    CD /D \"%~dp0\"\n@echo off\n";                                                                                      
$All = "if exist %programdata%\chocolatey ( echo found ) ELSE (powershell -command \"Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))\")";


if ($_POST['office'] == '1') {
    $office = "choco install office -y --Force";}

if ($_POST['AcrobatReaderDC'] == '1') {
    $AcrobatReaderDC = "choco install adobereader -y --Force";}

if ($_POST['Putty'] == '1') {
    $Putty = "choco install putty.install -y --Force";}

if ($_POST['Firefox'] == '1') {
    $Firefox = "choco install firefox -y --Force";}

if ($_POST['NotepadPlusPlus'] == '1') {
    $NotepadPlusPlus = "choco install notepadplusplus -y --Force";}

if ($_POST['LANSpeedTest'] == '1') {
    $LANSpeedTest = "choco install lan-speed-test.portable -y --Force";}


if ($_POST['VMwareWorkstation'] == '1') {
    $VMwareWorkstation = "choco install vmwareworkstation -y --Force";}

if ($_POST['VirtualBox'] == '1') {
    $VirtualBox = "choco install virtualbox -y --Force";}

if ($_POST['Teamspeak'] == '1') {
    $Teamspeak = "choco install teamspeak -y --Force";}

if ($_POST['Uplay'] == '1') {
    $Uplay = "choco install uplay -y --Force";}

if ($_POST['Origin'] == '1') {
    $Origin = "choco install origin -y --Force";}

if ($_POST['AdwCleaner'] == '1') {
    $AdwCleaner = "choco install adwcleaner -y --Force";}

if ($_POST['Python'] == '1') {
    $Python = "choco install python -y --Force";}

if ($_POST['MicrosoftTeams'] == '1') {
    $MicrosoftTeams = "choco install microsoft-teams -y --Force";}

if ($_POST['Spotify'] == '1') {
    $Spotify = "choco install spotify -y --Force";}

if ($_POST['TorBrowser'] == '1') {
    $TorBrowser = "choco install tor-browser -y --Force";}

if ($_POST['AdobeCreativeCloud'] == '1') {
    $AdobeCreativeCloud = "choco install adobe-creative-cloud -y --Force";}

if ($_POST['Teamviewer'] == '1') {
    $Teamviewer = "choco install teamviewer -y --Force";}

if ($_POST['GeForceExperience'] == '1') {
    $GeForceExperience = "choco install geforce-experience -y --Force";}

if ($_POST['VLCmediaPlayer'] == '1') {
    $VLCmediaPlayer = "choco install vlc -y --Force";}

if ($_POST['WhatsApp'] == '1') {
    $WhatsApp = "choco install whatsapp -y --Force";}

if ($_POST['Java'] == '1') {
    $Java = "choco install jre8 -y --Force";}

if ($_POST['PaintNet'] == '1') {
    $PaintNet = "choco install paint.net -y --Force";}

if ($_POST['Minecraft'] == '1') {
    $Minecraft = "choco install minecraft -y --Force";}

if ($_POST['_7Zip'] == '1') {
    $_7Zip = "choco install 7zip -y --Force";}

if ($_POST['Steam'] == '1') {
    $Steam = "choco install steam -y --Force";}

if ($_POST['Sourcetree'] == '1') {
    $Sourcetree = "choco install sourcetree --version 2.5.5 -y --Force";}

if ($_POST['Discord'] == '1') {
    $Discord = "choco install discord -y --Force";}

if ($_POST['Chrome'] == '1') {
    $Chrome = "choco install googlechrome -y --Force";}

if ($_POST['WinRar'] == '1') {
    $WinRar = "choco install winrar -y --Force";}


$file = fopen("autoinstall.bat","w");
fwrite($file,"$Admin
$All



































































































$office


$AcrobatReaderDC


$Putty


$Firefox


$NotepadPlusPlus


$LANSpeedTest


















































$VMwareWorkstation


$VirtualBox


$Teamspeak


$Uplay


$Origin

$AdwCleaner


$Python


$MicrosoftTeams


$Spotify


$TorBrowser


$AdobeCreativeCloud


$Teamviewer


$GeForceExperience


$VLCmediaPlayer


$WhatsApp


$Java


$PaintNet


$Minecraft


$_7Zip



$Steam


$Sourcetree


$Discord


$Chrome


$WinRar
























































































");
fclose($file);

header("Content-disposition: attachment; filename=autoinstall.bat");
header("Content-type: application/bat");
readfile("autoinstall.bat");
exit;




?>

