CREATE TABLE `heartbeat` (
  `ts` varchar(26) NOT NULL,
  `server_id` int unsigned NOT NULL,
  `file` varchar(255) DEFAULT NULL,
  `position` bigint unsigned DEFAULT NULL,
  `relay_master_log_file` varchar(255) DEFAULT NULL,
  `exec_master_log_pos` bigint unsigned DEFAULT NULL,
  PRIMARY KEY (`server_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1