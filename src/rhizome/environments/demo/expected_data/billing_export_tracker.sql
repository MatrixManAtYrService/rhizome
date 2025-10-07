CREATE TABLE `export_tracker` (
  `id` bigint unsigned NOT NULL AUTO_INCREMENT,
  `exported_uuid` char(13) NOT NULL,
  `export_type` enum('CATALOG_APP','CATALOG_PLAN','VENDOR') NOT NULL,
  `system_type` enum('INFOLEASE','GOLEO','ODESSA') DEFAULT NULL,
  `exported_data` text,
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid_export_system` (`exported_uuid`,`export_type`,`system_type`),
  KEY `et_types` (`export_type`,`system_type`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3