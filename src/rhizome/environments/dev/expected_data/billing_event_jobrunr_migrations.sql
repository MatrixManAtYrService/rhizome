CREATE TABLE `jobrunr_migrations` (
  `id` char(36) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `script` varchar(64) COLLATE utf8_bin NOT NULL,
  `installedOn` varchar(29) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8_bin