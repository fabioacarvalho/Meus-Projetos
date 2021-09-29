drop database if exists toggle;
create database if not exists toggle;

create table categoria(
	idCategoria int primary key auto_increment,
    nomeCategoria varchar(45) not null
);

create table projeto(
	idProjeto int primary key auto_increment,
    nomeProjeto varchar(45) not null,
    idCategoria int,
    foreign key(idCategoria) references categoria(idCategoria)
);

create table usuario(
	idUsuario int primary key auto_increment,
    nomeUsuario varchar(50) not null,
    email varchar(50) not null,
    telefone varchar(15) not null,
    dataContrato varchar(10) not null,
    idProjeto int,
    foreign key(idProjeto) references projeto(idProjeto)
);

create table registro(
	idRegistro int primary key auto_increment,
    descricao varchar(60),
	timeStart datetime,
    timeEnd datetime
);

create table projetoRegistros(
	idRegistro int,
    idProjeto int,
    foreign key(idRegistro) references registro(idRegistro),
    foreign key(idProjeto) references projeto(idProjeto)
);