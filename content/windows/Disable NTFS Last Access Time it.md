title: Disabilitare la memorizzazione del Last Access Time in NTFS
lang: it
tags: windows, batch
Category: Windows
Date: 8/23/2014 12:55:32 AM 

Disabilitare il "Last Access Time", il momento di ultimo accesso al file, aumenta la velocità di accesso ai file e cartelle. 

	:::bat
	[HKLM\SYSTEM\CurrentControlSet\Control\FileSystem] "NtfsDisableLastAccessUpdate"

Come fare - Vai su "Start", "Esegui", e scrivi: 
	
	:::bat
	fsutil behavior set disablelastaccess 1

**Nota** - Questo può compromettere funzionalità come programmi di backup e/o storage remoto che sfruttino questa informazione.
