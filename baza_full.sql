BEGIN TRANSACTION;
DROP TABLE IF EXISTS "Users";
CREATE TABLE IF NOT EXISTS "Users" (
	"ID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"Imie"	TEXT NOT NULL,
	"Nazwisko"	TEXT NOT NULL,
	"Password"	TEXT NOT NULL
);
INSERT INTO "Users" ("ID","Imie","Nazwisko","Password") VALUES (1,'Adam','Jurkiewicz','as');
INSERT INTO "Users" ("ID","Imie","Nazwisko","Password") VALUES (2,'Artur','Adamski','5234523452345234');
INSERT INTO "Users" ("ID","Imie","Nazwisko","Password") VALUES (3,'Adam','Jurkiewicz','fasdfasdfasdfasd');
DROP INDEX IF EXISTS "Nazwiska";
CREATE INDEX IF NOT EXISTS "Nazwiska" ON "Users" (
	"Nazwisko"	ASC
);
COMMIT;
