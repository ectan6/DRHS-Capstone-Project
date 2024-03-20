-- main.ppc definition

-- Drop table

-- DROP TABLE main.ppc;

CREATE TABLE main.ppc (
	id bigserial NOT NULL,
	user_id int4 NULL,
	program_id int4 NULL,
	element_code varchar NULL,
	element_order int4 NULL,
	CONSTRAINT ppc_pk PRIMARY KEY (id)
);


-- main.ppc foreign keys

ALTER TABLE main.ppc ADD CONSTRAINT ppc_programs_fk FOREIGN KEY (program_id) REFERENCES main.programs(program_id);
ALTER TABLE main.ppc ADD CONSTRAINT ppc_users_fk FOREIGN KEY (user_id) REFERENCES main.users(user_id);