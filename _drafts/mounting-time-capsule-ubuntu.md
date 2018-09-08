---
title: Mounting your Apple Time Capsule in Ubuntu 16.04
location: Lisbon, Portugal
tags: [stuff, c++]
---

The default version used transition with version2 or 3 with the update and needed to be manually specified from the number 1


```shell
sudo mount.cifs //192.168.1.71/Data /media/capsule/ -o username=<user>,password=<pass>,sec=ntlm,vers=1.0
```

Debug with smbclient 

My old time capsule

Things stopped working suddenly. Emplying samba 

smbclient -U Neglecive -L //192.168.1.71
Enter Neglecive's password: 
Server does not support EXTENDED_SECURITY  but 'client use spnego = yes and 'client ntlmv2 auth = yes'
session setup failed: NT_STATUS_ACCESS_DENIED

$ smbclient -U Neglecive -L //192.168.1.71 --option='client ntlmv2 auth'=no
Enter Neglecive's password: 
session setup failed: NT_STATUS_LOGON_FAILURE
sergio@Hipster:~/Data$ smbclient -U Neglecive -L //192.168.1.71 --option='client ntlmv2 auth'=no
Enter Neglecive's password: 
Domain=[WORKGROUP] OS=[Apple Base Station] Server=[CIFS 4.32]

	Sharename       Type      Comment
	---------       ----      -------
	IPC$            IPC       
	Data            Disk      
Domain=[WORKGROUP] OS=[Apple Base Station] Server=[CIFS 4.32]

	Server               Comment
	---------            -------

	Workgroup            Master
	---------            -------

sudo mount.cifs //192.168.1.71/Data /media/capsule/ --verbose -o uid=sergio,username=stuff,password=pass,sec=ntlm
mount.cifs kernel mount options: ip=192.168.1.71,unc=\\192.168.1.71\Data,sec=ntlmssp,uid=1000,user=stuff,pass=********
mount error(112): Host is down
Refer to the mount.cifs(8) manual page (e.g. man mount.cifs)

