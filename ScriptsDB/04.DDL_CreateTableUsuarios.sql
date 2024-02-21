-- Table: GestionEventos.Usuarios

-- DROP TABLE IF EXISTS "GestionEventos"."Usuarios";

CREATE TABLE IF NOT EXISTS "GestionEventos"."Usuarios"
(
    id_usuario serial NOT NULL,
    nombre_usuario character varying(30) COLLATE pg_catalog."default",
    email character varying(25) COLLATE pg_catalog."default",
    CONSTRAINT "Usuarios_pkey" PRIMARY KEY (id_usuario)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS "GestionEventos"."Usuarios"
    OWNER to usr_gestion;