-- main.programs definition

-- Drop table

-- DROP TABLE main.programs;

CREATE TABLE main.programs (
	program_id bigserial NOT NULL,
	user_id int4 NULL,
	competition_id int4 NULL,
	CONSTRAINT programs_pk PRIMARY KEY (program_id)
);


-- main.programs foreign keys

ALTER TABLE main.programs ADD CONSTRAINT programs_users_fk FOREIGN KEY (user_id) REFERENCES main.users(user_id);