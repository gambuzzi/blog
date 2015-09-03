title: check ip con wildcard
lang: it
tags: php, regex
Category: Php
Date: 9/1/2014 05:47:17 AM 

	:::php
	#!/usr/bin/env php
	<?php
	
	echo preg_match("/".str_replace('\*','\d+',preg_quote('192.168.153.*'))."/", "192.168.153.12");
	echo "<br >";
	echo preg_match("/".str_replace('\*','\d+',preg_quote('192.168.153.*'))."/", "192.168.152.12");
	echo "<br >";
	echo preg_match("/^".str_replace('\*','\d+',preg_quote('192.168.153.12'))."$/", "192.168.153.12");
	echo "<br >";
