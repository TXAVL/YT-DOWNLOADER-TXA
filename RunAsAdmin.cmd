@echo off
cd /d "%~dp0"
start "" "%~dp0\{#MyAppExeName}" /runas
exit
