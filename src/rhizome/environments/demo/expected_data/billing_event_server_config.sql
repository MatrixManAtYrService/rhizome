CREATE TABLE `server_config` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `config_key` varchar(127) NOT NULL,
  `config_value` varchar(2000) DEFAULT NULL,
  `created_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `audit_id` varchar(26) NOT NULL DEFAULT 'DEFAULTED',
  PRIMARY KEY (`id`),
  UNIQUE KEY `server_config_key1` (`config_key`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb3