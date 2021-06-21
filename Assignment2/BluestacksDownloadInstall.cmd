@echo off
set BluestacksPath=C:\Bluestacks
set PATH=%BluestacksPath%;%BluestacksPath%\Scripts;%PATH%

set logFolder=%~dp0bluestack
if not exist "%logFolder%" md "%logFolder%"

if exist "%BluestacksPath%" echo %date% %time% "%BluestacksPath%" found. &goto Bluestacks_installed
	ECHO  %date% %time% %BluestacksPath% not found, downloading and installing Bluestacks
	set "CURRENT=%~dp0%"
	python %CURRENT%python\getUrl.py
	if not exist "%~dp0BlueStacksInstaller_5.0.220.1003.exe" Echo Download "%~dp0BlueStacksInstaller_5.0.220.1003.exe" failed& exit /b
	ECHO  %date% %time% Successfully Downloaded BlueStacksInstaller_5.0.220.1003.exe....
	%~dp0BlueStacksInstaller_5.0.220.1003.exe /qn INSTALLDIR=%BluestacksPath%  >> "%logFolder%\BlueStacksInstaller_5.0.220.1003.exe.log" 2>&1
	if not exist "%BluestacksPath%" Echo Installing Bluestacks failed& exit /b
	ECHO  %date% %time% Successfully Installed BlueStacksInstaller_5.0.220.1003....
:Bluestacks_installed