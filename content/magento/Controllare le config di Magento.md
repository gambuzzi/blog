title: Controllare le config di Magento
lang: it
tags: php, magento
Category: Magento
Date: 9/1/2014 20:03:20 PM 


dalla radice di magento

	:::sh
	find . -type f -name 'config.xml' -exec xmllint --noout {} \;

serve il comando **`xmllint`** installato
