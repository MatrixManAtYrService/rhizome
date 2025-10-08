CREATE TABLE `look_data` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `look_uuid` char(32) NOT NULL,
  `payload` blob NOT NULL,
  `created_timestamp` datetime(6) NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
  PRIMARY KEY (`id`),
  UNIQUE KEY `look_uuid` (`look_uuid`)
) ENGINE=InnoDB AUTO_INCREMENT=129207 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci