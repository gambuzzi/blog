title: Recuperare tutti i prodotti per Attribute Set
lang: it
tags: php, magento
Category: Magento
Date: 9/1/2014 20:01:20 PM 


Questo piccolo pezzo di codice server per recuperare tutti i prodotti dello store, dato il nome di un attribute set.

	:::php
	<?php
	public function productsByAttributeSet($attrSetName) {
	    $asId = Mage::getModel('eav/entity_attribute_set')
	            ->load($attrSetName, 'attribute_set_name')
	            ->getAttributeSetId();
	
	    $products = Mage::getModel('catalog/product')
		->getCollection()	
		->addFieldToFilter('attribute_set_id', $asId);
	
	    return $products;
	}

A questo punto sull'oggetto restituito va chiamata la load() se si vuole poi ciclare sui prodotti oppure si può usare la collection non caricata per altri scopi.

Prima della `load()` si possono anche inserire nella collection altri campi che potrebbero servire.

	:::php
	<?php
    $products->addAttributeToSelect('name');