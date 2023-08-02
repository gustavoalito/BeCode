# Exercices MySQL Basics

- Crée une base de données `becode`.
- Importe le fichier `students.sql` qui se trouve dans ce dossier.

Dans un second fichier .sql, tu stockeras les requêtes qui te permettront de réaliser ces actions :

- Affiche toutes les données.
  
  1. `SELECT * FROM students`
  1. `INNER JOIN school`
  1. `ON students.school=school.idschool`
  1. `ORDER BY nom`
  
- Affiche uniquement les prénoms.
  
  1. `SELECT prenom FROM students`
  
- Affiche les prénoms, les dates de naissance et l’école de chacun.
  
  1. `SELECT prenom, datenaissance, school FROM students`
  
- Affiche uniquement les élèves qui sont de sexe féminin.
  
  1. `SELECT * FROM students`
  1. `WHERE genre="F"`
  
- Affiche uniquement les élèves qui font partie de l’école d'Addy.
  
  1. `SELECT prenom, nom, school, @schoolid := school FROM students WHERE nom="Addy";`
  1. `SELECT prenom, nom, school FROM students`
  1. `WHERE school = @schoolid;`
  
- Affiche uniquement les prénoms des étudiants, par ordre inverse à l’alphabet
(DESC). Ensuite, la même chose mais en limitant les résultats à 2.

  1. `SELECT prenom FROM students`
  1. `ORDER BY prenom DESC;`
  1. `SELECT prenom FROM students`
  1. `ORDER BY prenom DESC`
  1. `LIMIT 2;`
  
- Ajoute Ginette Dalor, née le 01/01/1930 et affecte-la à Bruxelles, toujours en
SQL.

  1. `INSERT INTO students (nom, prenom, datenaissance, genre, school)`
  1. `VALUES ( "Dalor", "Ginette", "1930-01-01", "F", 1);`
  
- Modifie Ginette (toujours en SQL) et change son sexe et son prénom en “Omer”.
  
  1. `UPDATE students`
  1. `SET genre = "M", prenom = "Omer"`
  1. `ORDER BY idStudent DESC -- Ordering by the latest id`
  1. `LIMIT 1; -- Limiting to the 1st entry, which in this case, is the last id entry`
  
- Supprimer la personne dont l’ID est 3.
  
  `DELETE FROM students`
  `WHERE idStudent = 3;`
  
- Modifier le contenu de la colonne School de sorte que "1" soit remplacé par "Liege" et "2" soit remplacé par "Gent". (attention au type de la colonne!)
  
  `DESCRIBE students; -- to learn that the school column's type is tinyint`
  `ALTER TABLE students MODIFY COLUMN school VARCHAR(30); -- Chaning the type from tinyint to varchar`
  `DESCRIBE students; -- to confirm the change was carried out`
  `UPDATE students SET school = "Liège" WHERE school = "1";`
  `UPDATE students SET school = "Gent" WHERE school = "2";`
  
  - Faire d’autres manipulations pour voir si t’es bien compris.
