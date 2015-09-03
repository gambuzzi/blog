title: Disabilitare i prodotti non in una categoria
lang: it
tags: php, magento
Category: Magento
Date: 9/1/2014 20:04:20 PM 


sql

	:::sql
	update catalog_product_entity_int set value=2 
		where attribute_id=96 
		and entity_id not in 
			(select distinct product_id from catalog_category_product);

in php

	:::php
	<?php	
	$write = Mage::getSingleton('core/resource')->getConnection('core_write'); 
	$write->update( 
	    'catalog_product_entity_int', 
	    array('value' => Mage_Catalog_Model_Product_Status::STATUS_DISABLED), 
	    'attribute_id=96 and entity_id not in (select distinct product_id from catalog_category_product)' 
	);

