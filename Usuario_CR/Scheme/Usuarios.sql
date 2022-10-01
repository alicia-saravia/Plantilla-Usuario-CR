-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema registro_acceso
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema usuarios
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `usuarios` ;

-- -----------------------------------------------------
-- Schema usuarios
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `usuarios` DEFAULT CHARACTER SET utf8mb3 ;
USE `usuarios` ;

-- -----------------------------------------------------
-- Table `usuarios`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `usuarios`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `apellido` VARCHAR(45) NULL DEFAULT NULL,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  `creado_en` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `actualizado_en` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
