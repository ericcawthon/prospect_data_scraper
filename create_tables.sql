CREATE TABLE IF NOT EXISTS `prospects` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `rank` int(5) NOT NULL,
  `name` varchar(255) NOT NULL,
  `pos` varchar(10) NOT NULL,
  `team` varchar(10) NOT NULL,
  `bat_throw` varchar(10) NOT NULL,
  `future_grades` varchar(255) NOT NULL,
  `level` varchar(20) NOT NULL,
  `age` int(2) NOT NULL,
  `eta` varchar(250) NOT NULL,
  `last` varchar(5) NOT NULL,
  `inserted_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `prospects_future_grades` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `prospect_id` int(10) NOT NULL,
  `grade` int(2) NOT NULL,
  `label` varchar(5) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;