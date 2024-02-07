-- main.jumps definition

-- Drop table

-- DROP TABLE main.jumps;

CREATE TABLE main.jumps (
	code varchar NOT NULL,
	"element" varchar NULL,
	sov float4 NULL,
	under_or_e float4 NULL,
	under_and_e float4 NULL,
	CONSTRAINT jumps_pk PRIMARY KEY (code)
);