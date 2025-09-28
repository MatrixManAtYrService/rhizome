CREATE TABLE `reseller_invoice_alliance` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `reseller_id` bigint unsigned NOT NULL,
  `alliance` char(3) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `reseller_id` (`reseller_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3