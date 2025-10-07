CREATE TABLE `bank_routing` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `routing_number` varchar(40) NOT NULL,
  `bank_name` varchar(256) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `routing_number` (`routing_number`)
) ENGINE=InnoDB AUTO_INCREMENT=7811 DEFAULT CHARSET=utf8mb3