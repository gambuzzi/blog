title: Installare Magento da console o ssh
lang: it
tags: php, magento
Category: Magento
Date: 9/1/2014 20:02:20 PM 


A seguire

	:::sh
	php -f install.php -- \
	--license_agreement_accepted "yes" \
	--locale "en_US" \
	--timezone "Europe/Berlin" \
	--default_currency "EUR" \
	--db_host "localhost" \
	--db_name "magento" \
	--db_user "root" \
	--db_pass "pass" \
	--url "http://magento.local/" \
	--use_rewrites "yes" \
	--use_secure "no" \
	--secure_base_url "" \
	--use_secure_admin "no" \
	--admin_firstname "John" \
	--admin_lastname "Doe" \
	--admin_email "dymmy@dummy.it" \
	--admin_username "admin" \
	--admin_password "pass"