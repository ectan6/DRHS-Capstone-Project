-- main.competitions definition

-- Drop table

-- DROP TABLE main.competitions;

CREATE TABLE main.competitions (
	competition_id bigserial NOT NULL,
	"name" varchar NULL,
	"date" date NULL,
	CONSTRAINT competitions_pk PRIMARY KEY (competition_id)
);