-- main.users definition

-- Drop table

-- DROP TABLE main.users;

CREATE TABLE main.users (
	user_id int4 NOT NULL,
	first_name varchar NULL,
	last_name varchar NULL,
	CONSTRAINT users_pk PRIMARY KEY (user_id)
);