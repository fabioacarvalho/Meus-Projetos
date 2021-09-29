select nomeUsuario, email, telefone, nomeProjeto from usuario u inner join projeto p on u.idProjeto = p.idProjeto;

select nomeProjeto, descricao, timeStart, timeEnd from projeto p inner join registro r inner join projetoRegistros pr on p.idProjeto = pr.idProjeto;

select nomeProjeto, descricao, timeStart, timeEnd, (timeEnd - timeStart) as tempo from projeto p inner join registro r inner join projetoRegistros pr on p.idProjeto = pr.idProjeto;
