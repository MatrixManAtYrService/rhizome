CREATE TABLE `banner_details` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `banner_data_id` bigint NOT NULL,
  `tag` varchar(256) DEFAULT NULL,
  `config` varchar(256) DEFAULT NULL,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `banner_data_id` (`banner_data_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3