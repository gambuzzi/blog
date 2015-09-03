title: Disable NTFS Last Access Time
lang: en
tags: windows, batch
Category: Windows
Date: 8/23/2014 12:55:32 AM 

Disabling the Last Access Time improves the speed of folder and file access.

	:::bat
	[HKLM\SYSTEM\CurrentControlSet\Control\FileSystem] "NtfsDisableLastAccessUpdate"

Instructions - Go to "Start", "Run", and Type: 
	
	:::bat
	fsutil behavior set disablelastaccess 1

**Notes** - This can affect programs such as backup and Remote Storage that rely on this feature.