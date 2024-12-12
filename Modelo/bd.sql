DROP DATABASE restaurante;
CREATE DATABASE IF NOT EXISTS restaurante;

USE restaurante;

DROP TABLE IF EXISTS persona;
DROP TABLE IF EXISTS comanda;
DROP TABLE IF EXISTS mesa;
DROP TABLE IF EXISTS plato;
DROP TABLE IF EXISTS plato_comanda;

create table persona(id int primary key auto_increment, nombre varchar(100), cedula varchar(11), apellido varchar(100), telefono varchar(10), direccion varchar(100), email varchar(100), rol ENUM('cliente', 'mesero', 'registrador', 'chef') default 'cliente');
create table mesa(id int primary key auto_increment, comensales int, estado varchar(20));
create table plato(id int primary key auto_increment, nombre varchar(100), precio float(10, 2), descripcion varchar(200));
create table comanda(id int primary key auto_increment, mesa int, cliente int, estado varchar(20), foreign key (mesa) references mesa(id), foreign key (cliente) references persona(id));

create table plato_comanda(comanda_id int, plato_id int, cantidad int, foreign key (comanda_id) references comanda(id), foreign key (plato_id) references plato(id));