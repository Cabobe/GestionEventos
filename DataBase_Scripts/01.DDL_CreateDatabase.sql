-- Database: PostgresDB

-- DROP DATABASE IF EXISTS "PostgresDB";

CREATE DATABASE "PostgresDB"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Spanish_Colombia.1252'
    LC_CTYPE = 'Spanish_Colombia.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

COMMENT ON DATABASE "PostgresDB"
    IS 'Plataforma de gestión de eventos.';