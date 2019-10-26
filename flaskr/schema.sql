--DROP TABLE IF EXISTS User;

CREATE TABLE User (
  id int PRIMARY KEY AUTOINCREMENT,
  name varchar(255) NOT NULL,
  age int NOT NULL,
  profile_picture varchar(255) NOT NULL,
  product varchar(255) NOT NULL,
  gender varchar(255) NOT NULL,
  city varchar(255) NOT NULL,
  state varchar(255) NOT NULL,
  country varchar(255) NOT NULL,
  email varchar(255) NOT NULL,
  password varchar(255) NOT NULL,
  created_at datetime NOT NULL,
  updated_at datetime NOT NULL
);
