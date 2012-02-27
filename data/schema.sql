
# $ mysql -u root < schema.sql
 
drop database if exists kanban_mail;
create database kanban_mail;
use kanban_mail;

CREATE TABLE item (
  id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  kind VARCHAR(20),
  created_on TIMESTAMP DEFAULT NOW(),
  last_touched_one TIMESTAMP DEFAULT NOW()
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
  sent_on TIMESTAMP
);


# Add item
INSERT INTO item (kind)
VALUES ("New");

# Add message
INSERT INTO message(item_id, sender, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Mint.com", "Your tax refund has arrived.", "Body..", "", "", "", "", NOW())
 

