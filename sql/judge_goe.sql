-- main.judge_goe definition

-- Drop table

-- DROP TABLE main.judge_goe;

CREATE TABLE main.judge_goe (
	id bigserial NOT NULL,
	user_id int4 NULL,
	program_id int4 NULL,
	element_number int4 NULL,
	goe float4 NULL,
	judge_1 int4 NULL,
	CONSTRAINT judge_goe_pk PRIMARY KEY (id)
);


-- main.judge_goe foreign keys

ALTER TABLE main.judge_goe ADD CONSTRAINT judge_goe_programs_fk FOREIGN KEY (program_id) REFERENCES main.programs(program_id);
ALTER TABLE main.judge_goe ADD CONSTRAINT judge_goe_users_fk FOREIGN KEY (user_id) REFERENCES main.users(user_id);