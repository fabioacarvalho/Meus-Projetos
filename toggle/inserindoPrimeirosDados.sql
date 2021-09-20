insert into categoria(nomeCategoria) values
	('Projeto Modelo'),
    ('Reunião com Cliente');

insert into projeto(nomeProjeto, idCategoria) values
	('Fulano de Mendes', 1),
    ('Ciclano da Silva', 2);
    
insert into usuario(nomeUsuario, email, telefone, dataContrato, idProjeto) values
	('Justin Bieber', 'justin@gmail.com', '5541987654321', '25/03/2021', 1),
	('Zeca Pagodinho', 'zeca@gmail.com', '5541987654321', '11/05/2019', 2);

insert into registro(descricao, timeStart, timeEnd) values
	('Projeto modelo iniciado', '2021-09-01 09:55:22', '2021-09-01 15:42:39'),
    ('Reuniao com cliente', '2021-09-06 08:00:22', '2021-09-01 10:25:44');

insert into projetoRegistros(idRegistro, idProjeto) values
	(1, 1),
    (2, 2);