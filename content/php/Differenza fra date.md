title: Differenza fra date
lang: it
tags: php, datetime
Category: Php
Date: 9/1/2014 05:47:17 AM 

	:::php
	#!/usr/bin/env php
	<?php
	
	date_default_timezone_set('UTC');
	print_r( date_diff( date_create() , date_create('2013-01-01') ) );
	echo "<br>";
	echo strtotime('2013-01-01');
	echo "<br>";
	echo strtotime('now');
	echo "<br>";
	echo strtotime('now')-strtotime('2013-01-01');
	echo "<br>";
	echo (strtotime('now')-strtotime('2013-01-01'))/3600/24;
	echo "<br>";

Risutato

	DateInterval Object ( 
		[y] => 0 
		[m] => 4 
		[d] => 28 
		[h] => 14 
		[i] => 56 
		[s] => 5 
		[invert] => 1 
		[days] => 148 
	) 
	1356998400
	1369839365
	12840965
	148.62228009259
