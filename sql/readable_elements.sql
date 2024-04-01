-- main.readable_elements definition

-- Drop table

-- DROP TABLE main.readable_elements;

CREATE TABLE main.readable_elements (
	id bigserial NOT NULL,
	user_id int4 NULL,
	program_id int4 NULL,
	order_executed int4 NULL,
	"element" varchar NULL,
	CONSTRAINT readable_elements_pk PRIMARY KEY (id)
);