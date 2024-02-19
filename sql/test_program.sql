-- main.test_program definition

-- Drop table

-- DROP TABLE main.test_program;

CREATE TABLE main.test_program (
	program_id float4 NOT NULL,
	element_1 varchar NULL,
	counter int4 NULL,
	CONSTRAINT test_program_pk PRIMARY KEY (program_id)
);


-- main.test_program foreign keys

ALTER TABLE main.test_program ADD CONSTRAINT test_program_jumps_fk FOREIGN KEY (element_1) REFERENCES main.jumps(code);