-- main.score definition

-- Drop table

-- DROP TABLE main.score;

CREATE TABLE main.score (
	id bigserial NOT NULL,
	jump_id varchar NULL,
	spin_id varchar NULL,
	order_executed int4 NULL,
	spin_level int4 NULL,
	CONSTRAINT score_pk PRIMARY KEY (id)
);


-- main.score foreign keys

ALTER TABLE main.score ADD CONSTRAINT score_jumps_fk FOREIGN KEY (jump_id) REFERENCES main.jumps(jump_id);
ALTER TABLE main.score ADD CONSTRAINT score_spins_steps_fk FOREIGN KEY (spin_id) REFERENCES main.spins_steps(spin_id);