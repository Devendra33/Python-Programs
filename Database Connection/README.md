# Database Connection
it is a syntax for python database connection.

# pre-req(on cmd)
pip3 install mysql-connector

# Dummy database!
create database TSP;
use TSP;
create table salesman(empid int primary key, name varchar(30), username varchar(30), password varchar(30));
insert into salesman values(201, "Rahul Singh", "rahul001", "12345");
insert into salesman values(202, "Kabir Kumar", "kabir007", "2580");
insert into salesman values(203, "Dev  Kumar", "dev11", "12345");
insert into salesman values(204, "Akshay Singh", "akki001", "123@1");
insert into salesman values(205, "Sanjay Gupta", "sanjay12", "54321");

select * from salesman;
