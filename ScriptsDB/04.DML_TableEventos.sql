--Consulta de seleccion de informacion
SELECT id_evento, nombre_evento, descripcion, fecha, hora, latitud, longitud
FROM "GestionEventos"."Eventos";

--Consulta de seleccion de informacion por id
SELECT row_id, id_evento, nombre_evento, descripcion, fecha, hora, latitud, longitud
FROM "GestionEventos"."Eventos" WHERE id_evento=1;

--Consulta de insercion de informacion
INSERT INTO "GestionEventos"."Eventos"(nombre_evento, descripcion, fecha, hora, latitud, longitud)
VALUES ('Entrevista', 'Entrevista laboral',	'2022-07-22', '11:00', '4.616425853054133', '-74.06891626731635');

--Consulta de actualizacion de informacion
UPDATE "GestionEventos"."Eventos"
SET 
nombre_evento="Entrevista"
WHERE id_evento=1;

--Consulta de eliminacion de informacion	
DELETE FROM "GestionEventos"."Eventos" WHERE id_evento=1;