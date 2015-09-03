title: Echo della data
lang: it
tags: windows, batch
Category: Windows
Date: 8/23/2014 12:49:03 AM 

all'interno di un file `.bat`

	:::bat
	for /f "tokens=1-3* delims=/" %%a in ('date /t') do echo %%a %%b %%c


