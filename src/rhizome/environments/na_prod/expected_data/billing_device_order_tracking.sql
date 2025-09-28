CREATE TABLE `device_order_tracking` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `uuid` char(13) NOT NULL,
  `order_month` date NOT NULL,
  `serial_number` varchar(16) CHARACTER SET latin1 NOT NULL,
  `merchant_id` int unsigned NOT NULL,
  `activity` enum('ORDER','PAYMENTS') DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `merchant_id` (`merchant_id`)
) ENGINE=InnoDB AUTO_INCREMENT=50274 DEFAULT CHARSET=utf8mb3