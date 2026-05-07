CREATE DATABASE bdd_2;

CREATE TABLE pacientes(
	id SERIAL NOT NULL PRIMARY KEY,
	nome VARCHAR(50) NOT NULL,
	email VARCHAR(100) UNIQUE NOT NULL,
	senha VARCHAR(100) NOT NULL,
	endereco VARCHAR(100) NOT NULL,
	data_nascimento DATE NOT NULL,
	data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE medicos(
	id SERIAL NOT NULL PRIMARY KEY,
	nome VARCHAR(50) NOT NULL,
	num_registro INT UNIQUE NOT NULL,
	data_nascimento DATE NOT NULL
);

CREATE TABLE consulta(
	id_consulta SERIAL NOT NULL PRIMARY KEY,
	id_paciente INT,
	id_medico INT,
	data_hora_agendada TIMESTAMP,
	status_c VARCHAR(50) NOT NULL,
	observacao VARCHAR(100),

	FOREIGN KEY(id_paciente) REFERENCES pacientes(id),
	FOREIGN KEY(id_medico) REFERENCES medicos(id)
);

INSERT INTO pacientes(nome, email, senha, endereco, data_nascimento)
VALUES
	('João Silva', 'joaosilva@gmail.com', '123123', 'Rua Postgre, 456', '04-11-2000'),
	('Maria Clara', 'clarinha@gmail.com', '8950!', 'Rua 9 de julho, 33', '09-07-1905'),
	('Gustavo Silva', 'gustavo78@yahoo.com', 'g78d52', 'Rua Presidente Prudente, 836', '04-04-1994'),
	('Samuel Pontes', 'samuelpp@gmail.com', '8df48@f45', 'Rua dos Palmares, 09', '17-06-2001'),
	('Manuela Duarte', 'manuu123@gmail.com', 'm4nU#s3nh444', '', '12-12-2005'),
	('Ricardo Milos', 'causeUgotThat@gmail.com', '8943h!rheA', 'Avenida Três Poderes, 54', '04-02-2018');

INSERT INTO medicos(nome, num_registro, data_nascimento)
VALUES
	('Miguel Soares', '1234', '30-10-2000'),
	('Helena Barreto', '5678', '27-09-1999'),
	('Sofia da Silva', '9012', '24-08-1988');

INSERT INTO consulta(id_paciente, id_medico, data_hora_agendada, status_c, observacao)
VALUES
	(1, 1, '07-05-2026 14:30', 'Agendado', 'Trazer acompanhante'),
	(5, 3, '01-05-2026 17:00', 'Finalizado', ''),
	(3, 2, '25-04-2026 15:30', 'Finalizado', 'Marcar retorno'),
	(1, 1, '07-04-2026 13:30', 'Finalizado', 'Marcar retorno'),
	(6, 3, '14-03-2026 19:45', 'Finalizado', ''),
	(2, 3, '14-03-2026 17:45', 'Finalizado', 'Marcar retorno'),
	(4, 2, '19-12-2025 16:30', 'Finalizado', ''),
	(5, 1, '21-11-2025 13:45', 'Finalizado', 'Marcar retorno');
