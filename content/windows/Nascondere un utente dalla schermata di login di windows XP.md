title: Nascondere un utente dalla schermata di login di windows XP
lang: it
tags: windows, batch
Category: Windows
Date: 2010/10/06 02:51 

Andare alla seguente chiave di registro

	:::bat	
	HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList

Sotto a questa chiave create un nuovo valore `DWORD` col nome corrispondente all'utente da nascondere e settatene il valore a:

    :::bat
	0 – Nasconde l'utente
	1 – Mostra l'utente

In alternativa da linea di comando...

	:::bat
	REG ADD "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList" /v <user> /d 0 /t REG_DWORD /f

**ATTENZIONE**: questa è una procedura che puo rendervi impossible l'accesso al PC. Declino ogni responzabilità.