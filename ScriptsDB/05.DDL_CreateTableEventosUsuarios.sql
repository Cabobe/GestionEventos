-- Table: GestionEventos.EventosUsuarios

-- DROP TABLE IF EXISTS "GestionEventos"."EventosUsuarios";

CREATE TABLE IF NOT EXISTS "GestionEventos"."EventosUsuarios"
(
    id_evento integer NOT NULL,
    id_usuario integer NOT NULL,
    CONSTRAINT "EventoUsuario_pkey" PRIMARY KEY (id_evento, id_usuario),
    CONSTRAINT "EventoUsuario_fkey_id_evento" FOREIGN KEY (id_evento)
        REFERENCES "GestionEventos"."Eventos" (id_evento) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT "EventoUsuario_fkey_id_usuario" FOREIGN KEY (id_usuario)
        REFERENCES "GestionEventos"."Usuarios" (id_usuario) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS "GestionEventos"."EventosUsuarios"
    OWNER to usr_gestion;