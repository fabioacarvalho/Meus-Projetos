-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `mydb` ;

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`servicos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`servicos` ;

CREATE TABLE IF NOT EXISTS `mydb`.`servicos` (
  `cod` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `unidade` VARCHAR(45) NOT NULL,
  `valor` FLOAT NOT NULL,
  PRIMARY KEY (`cod`),
  UNIQUE INDEX `cod_UNIQUE` (`cod` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`categoria`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`categoria` ;

CREATE TABLE IF NOT EXISTS `mydb`.`categoria` (
  `idcategoria` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `servicos_cod` INT NOT NULL,
  PRIMARY KEY (`idcategoria`, `servicos_cod`),
  UNIQUE INDEX `idcategoria_UNIQUE` (`idcategoria` ASC) VISIBLE,
  UNIQUE INDEX `nome_UNIQUE` (`nome` ASC) VISIBLE,
  INDEX `fk_categoria_servicos1_idx` (`servicos_cod` ASC) VISIBLE,
  CONSTRAINT `fk_categoria_servicos1`
    FOREIGN KEY (`servicos_cod`)
    REFERENCES `mydb`.`servicos` (`cod`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`medicoes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`medicoes` ;

CREATE TABLE IF NOT EXISTS `mydb`.`medicoes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `numero` VARCHAR(45) NULL,
  `data` DATE NULL,
  `servico` VARCHAR(45) NULL,
  `quantidade` VARCHAR(45) NULL,
  `unidade` VARCHAR(45) NULL,
  `valorUnitario` FLOAT NULL,
  `valorTotal` FLOAT NULL,
  `categoria_idcategoria` INT NOT NULL,
  `categoria_servicos_cod` INT NOT NULL,
  PRIMARY KEY (`id`, `categoria_idcategoria`, `categoria_servicos_cod`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_medicoes_categoria1_idx` (`categoria_idcategoria` ASC, `categoria_servicos_cod` ASC) VISIBLE,
  CONSTRAINT `fk_medicoes_categoria1`
    FOREIGN KEY (`categoria_idcategoria` , `categoria_servicos_cod`)
    REFERENCES `mydb`.`categoria` (`idcategoria` , `servicos_cod`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`obra`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`obra` ;

CREATE TABLE IF NOT EXISTS `mydb`.`obra` (
  `codCliente` INT NOT NULL,
  `cliente` VARCHAR(45) NOT NULL,
  `valorObra` FLOAT NOT NULL,
  `dataInicial` VARCHAR(45) NOT NULL,
  `tipo` VARCHAR(45) NOT NULL,
  `bdi` FLOAT NOT NULL,
  `medicoes_id` INT NOT NULL,
  `medicoes_id1` INT NOT NULL,
  `medicoes_id2` INT NOT NULL,
  PRIMARY KEY (`codCliente`, `medicoes_id`, `medicoes_id2`),
  UNIQUE INDEX `codCliente_UNIQUE` (`codCliente` ASC) VISIBLE,
  INDEX `fk_obra_medicoes1_idx` (`medicoes_id2` ASC) VISIBLE,
  CONSTRAINT `fk_obra_medicoes1`
    FOREIGN KEY (`medicoes_id2`)
    REFERENCES `mydb`.`medicoes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`cliente`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`cliente` ;

CREATE TABLE IF NOT EXISTS `mydb`.`cliente` (
  `cpf` INT NOT NULL,
  `nome` VARCHAR(60) NOT NULL,
  `endereco` VARCHAR(45) NOT NULL,
  `telefone` INT NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `cod` INT NOT NULL,
  PRIMARY KEY (`cod`),
  UNIQUE INDEX `cpf_UNIQUE` (`cpf` ASC) VISIBLE,
  UNIQUE INDEX `cod_UNIQUE` (`cod` ASC) VISIBLE,
  CONSTRAINT `fk_cliente_obra`
    FOREIGN KEY (`cod`)
    REFERENCES `mydb`.`obra` (`codCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`departamento`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`departamento` ;

CREATE TABLE IF NOT EXISTS `mydb`.`departamento` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `obra_codCliente` INT NOT NULL,
  `obra_medicoes_id` INT NOT NULL,
  `obra_medicoes_id2` INT NOT NULL,
  PRIMARY KEY (`id`, `obra_codCliente`, `obra_medicoes_id`, `obra_medicoes_id2`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `nome_UNIQUE` (`nome` ASC) VISIBLE,
  INDEX `fk_departamento_obra1_idx` (`obra_codCliente` ASC, `obra_medicoes_id` ASC, `obra_medicoes_id2` ASC) VISIBLE,
  CONSTRAINT `fk_departamento_obra1`
    FOREIGN KEY (`obra_codCliente` , `obra_medicoes_id` , `obra_medicoes_id2`)
    REFERENCES `mydb`.`obra` (`codCliente` , `medicoes_id` , `medicoes_id2`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`user`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`user` ;

CREATE TABLE IF NOT EXISTS `mydb`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(45) NULL,
  `cargo` VARCHAR(45) NULL,
  `admin` TINYINT NULL,
  `user_id` INT NOT NULL,
  `departamento_id` INT NOT NULL,
  PRIMARY KEY (`id`, `user_id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `fk_user_departamento1_idx` (`departamento_id` ASC) VISIBLE,
  CONSTRAINT `fk_user_departamento1`
    FOREIGN KEY (`departamento_id`)
    REFERENCES `mydb`.`departamento` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
