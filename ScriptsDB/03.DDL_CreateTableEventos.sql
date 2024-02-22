-- Table: GestionEventos.Eventos

-- DROP TABLE IF EXISTS "GestionEventos"."Eventos";

CREATE TABLE IF NOT EXISTS "GestionEventos"."Eventos"
(
    id_evento serial NOT NULL,
    nombre_evento character varying(30) COLLATE pg_catalog."default" NOT NULL,
    descripcion character varying(150) COLLATE pg_catalog."default",
    fecha_inicio date NOT NULL,
    hora_inicio character varying(8) NOT NULL,
    fecha_fin date NOT NULL,
    hora_fin character varying(8) NOT NULL,
    latitud character varying(30) COLLATE pg_catalog."default" NOT NULL,
    longitud character varying(30) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT "Eventos_pkey" PRIMARY KEY (id_evento)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS "GestionEventos"."Eventos"
    OWNER to usr_gestion;