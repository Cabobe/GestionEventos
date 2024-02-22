-- Table: GestionEventos.Eventos

-- DROP TABLE IF EXISTS "GestionEventos"."Eventos";

CREATE TABLE IF NOT EXISTS "GestionEventos"."Eventos"
(
    id_evento serial NOT NULL,
    nombre_evento character varying(30) COLLATE pg_catalog."default" NOT NULL,
    descripcion character varying(150) COLLATE pg_catalog."default",
    fecha character varying(12) COLLATE pg_catalog."default" NOT NULL,
    hora character varying(12) COLLATE pg_catalog."default" NOT NULL,
    latitud numeric NOT NULL,
    longitud numeric NOT NULL,
    CONSTRAINT "Eventos_pkey" PRIMARY KEY (id_evento)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS "GestionEventos"."Eventos"
    OWNER to usr_gestion;