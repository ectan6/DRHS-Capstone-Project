-- main.score definition

-- Drop table

-- DROP TABLE main.score;

CREATE TABLE main.score (
	score_id int4 NOT NULL,
	jump_id varchar NULL,
	spin_id varchar NULL,
	order_executed int4 NULL,
	judge1_score int4 NULL,
	judge2_score int4 NULL,
	judge3_score int4 NULL,
	judge4_score int4 NULL,
	judge5_score int4 NULL,
	judge6_score int4 NULL,
	judge7_score int4 NULL,
	goe float4 NULL,
	has_underrotation bool NULL,
	has_edgecall bool NULL,
	CONSTRAINT score_pk PRIMARY KEY (score_id)
);


-- main.score foreign keys

ALTER TABLE main.score ADD CONSTRAINT score_jumps_fk FOREIGN KEY (jump_id) REFERENCES main.jumps(code);
ALTER TABLE main.score ADD CONSTRAINT score_spins_steps_fk FOREIGN KEY (spin_id) REFERENCES main.spins_steps(code);