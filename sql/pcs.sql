-- main.pcs definition

-- Drop table

-- DROP TABLE main.pcs;

CREATE TABLE main.pcs (
	id bigserial NOT NULL,
	user_id int4 NULL,
	program_id int4 NULL,
	skating_skills float4 NULL,
	transitions float4 NULL,
	performance float4 NULL,
	choreography float4 NULL,
	interpretation float4 NULL,
	CONSTRAINT pcs_pk PRIMARY KEY (id)
);


-- main.pcs foreign keys

ALTER TABLE main.pcs ADD CONSTRAINT pcs_programs_fk FOREIGN KEY (program_id) REFERENCES main.programs(program_id);
ALTER TABLE main.pcs ADD CONSTRAINT pcs_users_fk FOREIGN KEY (user_id) REFERENCES main.users(user_id);