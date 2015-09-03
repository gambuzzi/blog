title: Entro tot giorni da fine trimestre
lang: it
tags: php, datetime
Category: Php
Date: 9/1/2014 05:47:17 AM 

	:::php
	#!/usr/bin/env php
	<?php
	
	date_default_timezone_set('UTC');
	
	$today = getdate(); 
	print_r($today);
	echo '<br/>';
	$y = $today['year'];
	$soglia = 60;
	$ok=false;
	for ($i=1; $i<13; $i+=3) {
	    #$diff = (strtotime('now')-strtotime(sprintf('%04i-%02i-01', $y, $i)))/3600/24;
	 $diff = (strtotime('now')-strtotime($y."-".$i."-01"))/3600/24;
	 echo $diff."<br>";
	 if ($diff>0 && $diff<$soglia) {
	   $ok = true;
	 }
	}
	
	var_dump($ok);
