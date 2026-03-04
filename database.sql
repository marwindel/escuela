-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.32-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.8.0.6908
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando estructura para tabla escuela.aula
CREATE TABLE IF NOT EXISTS `aula` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `grado` varchar(50) NOT NULL DEFAULT '0',
  `seccion` varchar(50) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla escuela.aula: ~0 rows (aproximadamente)
INSERT INTO `aula` (`id`, `grado`, `seccion`) VALUES
	(1, '1', 'B');

-- Volcando estructura para tabla escuela.materiales
CREATE TABLE IF NOT EXISTS `materiales` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(150) DEFAULT NULL,
  `cantidad` int(11) DEFAULT 0,
  `aula_id` int(11) DEFAULT 0,
  `registrado_por` varchar(150) DEFAULT NULL,
  `fecha_creacion` datetime DEFAULT NULL,
  `fecha_actualizacion` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla escuela.materiales: ~2 rows (aproximadamente)
INSERT INTO `materiales` (`id`, `descripcion`, `cantidad`, `aula_id`, `registrado_por`, `fecha_creacion`, `fecha_actualizacion`) VALUES
	(1, 'Pizarra', 2, 1, 'Jose PErez', '2026-03-01 16:10:49', '2026-03-01 16:10:49'),
	(2, 'pupitre', 24, 1, 'paso', '2026-03-02 17:37:36', '2026-03-02 17:37:36'),
	(3, 'marcadores', 4, 1, 'jose', '2026-03-03 21:51:02', '2026-03-03 21:51:02');

-- Volcando estructura para tabla escuela.usuario
CREATE TABLE IF NOT EXISTS `usuario` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL DEFAULT '0',
  `password` varchar(255) NOT NULL DEFAULT '0',
  `fecha_reg` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Volcando datos para la tabla escuela.usuario: ~1 rows (aproximadamente)
INSERT INTO `usuario` (`id`, `username`, `password`, `fecha_reg`) VALUES
	(1, 'marwin', '$2b$12$kfLxn3fa/DrqF0bQjxB0nuvi9z.dFXbZtfSTw.PlRWet1ANsNw1g6', '2026-02-09 22:04:00');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
