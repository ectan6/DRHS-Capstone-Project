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