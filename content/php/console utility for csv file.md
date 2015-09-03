title: console utility for csv file
slug: console-utility-for-csv-file
lang: en
tags: php, csv
Category: Php
Date: 9/1/2014 05:47:17 AM 

	:::php
	#!/usr/bin/env php
	<?php
	
	$opt = getopt('f:l:h');
	#echo '$opt: ';print_r($opt);
	$row = -1;
	if (($handle = fopen($opt['f'], "r")) !== FALSE) {
	    while (($data = fgetcsv($handle)) !== FALSE) {
	        if ($row==-1) $header=$data;
	        $row++;
	        if ($opt['l']==$row) {
	                $num = count($data);
	                echo "<p> $num fields in line $row: <br /></p>\n";
	                if (array_key_exists('h',$opt)) {
	                        print_r(array_combine($header,$data));
	                } else {
	                        print_r($data);
	                }
	        }
	    }
	    fclose($handle);
	}


