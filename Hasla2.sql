BEGIN TRANSACTION;
DROP TABLE IF EXISTS "Hasla";
CREATE TABLE IF NOT EXISTS "Hasla" (
	"ID"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"Username"	TEXT NOT NULL UNIQUE,
	"Password"	TEXT NOT NULL
);
INSERT INTO "Hasla" ("ID","Username","Password") VALUES (1,'adasiej_j','12345');
INSERT INTO "Hasla" ("ID","Username","Password") VALUES (2,'rrr','12345');
INSERT INTO "Hasla" ("ID","Username","Password") VALUES (3,'Adam','ertertr');
INSERT INTO "Hasla" ("ID","Username","Password") VALUES (4,'444rr','345342');
INSERT INTO "Hasla" ("ID","Username","Password") VALUES (5,'adasiek1','34564');
INSERT INTO "Hasla" ("ID","Username","Password") VALUES (6,'user5','5234234523');
COMMIT;
