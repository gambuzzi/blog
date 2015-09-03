title: Ridistribuire programmi python come un unico file exe
lang: it
tags: python, batch
Category: Python
Date: 12/12/2009 14:12

Cominciamo col presentare uno script che permette di ridistribuire i nostri programmi python a chi non abbia installato l'interprete.

Necessitiamo di py2exe installato e del NullSoft Installer.

Questo script è stato preso dal sito del py2exe e poi largamente rimaneggiato.

Il file va salvato con lo stesso nome dello script python da impacchettare e con estensione BAT o CMD, percui se devo ridistribuire palla.py questo script andrebbe salvato come palla.cmd o palla.bat
	
	@echo off
	
	set PythonEXE=C:\Python25\python.exe
	set NsisEXE=C:\Programmi\NSIS\makensisw.exe
	
	if not exist %~dpn0.py          call :FileNotFound %~dpn0.py
	if not exist %PythonEXE%        call :FileNotFound %PythonEXE%
	if not exist %NsisEXE%          call :FileNotFound %NsisEXE%
	
	call :MakeSetupFile >"%~dpn0_EXESetup.py"
	
	%PythonEXE% "%~dpn0_EXESetup.py" py2exe
	if not "%errorlevel%"=="0" (
	        echo Py2EXE Error!
	        pause
	        goto:eof
	)
	
	del "%~dpn0_EXESetup.py"
	
	rd build /s /q
	xcopy dist\*.* "%~dpn0_EXE\" /d /y
	rd dist /s /q
	
	echo.
	echo.
	echo Done: "%~dpn0_EXE\"
	echo.
	
	::Create Exe MonoFile
	call :MakeNSISFile >"%~dpn0_NSIS.nsi"
	%NsisEXE% "%~dpn0_NSIS.nsi"
	del "%~dpn0_NSIS.nsi"
	
	pause
	goto:eof
	
	:MakeSetupFile
	        echo.
	        echo from distutils.core import setup
	        echo import py2exe
	        echo.
	        echo setup (console=[r"%~dpn0.py"],
	        echo    options = {"py2exe": {"packages": ["encodings"]}})
	        echo.
	goto:eof
	
	
	:MakeNSISFile
	        echo.
	        echo !include "FileFunc.nsh"
	        echo !insertmacro GetParameters
	        echo !define exe '%~n0'
	        echo.
	        echo SetCompressor lzma
	        echo Name ${exe}.exe
	        echo OutFile ${exe}.exe
	        echo SilentInstall silent
	        echo.
	        echo Section
	        echo InitPluginsDir
	        echo SetOutPath '$PLUGINSDIR'
	        echo File '${exe}_EXE\*.*'
	        echo.
	        echo SetOutPath '$EXEDIR'
	        echo ${GetParameters} $R0
	        echo.
	        echo ExecWait '"$PLUGINSDIR\${exe}" $R0' 
	        echo.
	        echo SectionEnd
	        echo.
	goto:eof
	
	:FileNotFound
	        echo.
	        echo Error, File not found:
	        echo [%1]
	        echo.
	        echo Check Path in %~nx0???
	        echo.
	        pause
	        exit
	goto:eof