# $ mysql -u root < schema.sql

drop database if exists lean_mail;
create database lean_mail;
use lean_mail;

CREATE TABLE item (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  kind VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT NULL
);


CREATE TABLE message (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  item_id INT,
  sender VARCHAR(500),
  subject VARCHAR(500),
  body TEXT,
  cc VARCHAR(500),
  bc VARCHAR(500),
  headers VARCHAR(500),
  sent_on DATETIME DEFAULT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT NULL
);


# Add item
INSERT INTO item (kind)
VALUES ("New");

# Add message
INSERT INTO message(item_id, sender, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Mint.com", "Your tax refund has arrived.", "Body..", "", "", "", "")
