-- main.spins_steps definition

-- Drop table

-- DROP TABLE main.spins_steps;

CREATE TABLE main.spins_steps (
	spin_id varchar NOT NULL,
	"element" varchar NULL,
	levelb float4 NULL,
	level1 float4 NULL,
	level2 float4 NULL,
	level3 float4 NULL,
	level4 float4 NULL,
	CONSTRAINT spins_steps_pk PRIMARY KEY (spin_id)
);