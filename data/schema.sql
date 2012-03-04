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
  sent_to VARCHAR(500),
  subject VARCHAR(500),
  body TEXT,
  cc VARCHAR(500),
  bc VARCHAR(500),
  headers VARCHAR(500),
  sent_on DATETIME DEFAULT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT NULL
  
);


################################# ADD NEW ITEMS ##############################
INSERT INTO item (kind)
VALUES ("New");


# Add message 1
INSERT INTO message(item_id, sender, sent_to, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Mint.com", "cgabaldon@gmail.com", "Your tax refund has arrived.", "Body..", "", "", "", NOW());


# Add item 2
INSERT INTO item (kind)
VALUES ("New");

# Add message 2
INSERT INTO message(item_id, sender, sent_to, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Dwell", "cgabaldon@gmail.com", "This week from Dwell.", "Body..", "", "", "", NOW());

# Add item 3
INSERT INTO item (kind)
VALUES ("New");

# Add message 3
INSERT INTO message(item_id, sender, sent_to, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Amazon.com", "cgabaldon@gmail.com", "Amazon Instant Video: New Releases and the Weekend Movie Sale", "Body..", "", "", "",  NOW());

# Add item 4
INSERT INTO item (kind)
VALUES ("New");

# Add message 4
INSERT INTO message(item_id, sender, sent_to, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Warby Parker", "cgabaldon@gmail.com", "Your Warby Parker order no. 100194087 has been received and will ship out shortly", "Body..", "", "", "", NOW());


################################# ADD ACTION ITEMS ##############################
INSERT INTO item (kind)
VALUES ("Action");


# Add message 1
INSERT INTO message(item_id, sender, sent_to, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Amazon.com", "cgabaldon@gmail.com", "New Deals", "Body..", "", "", "", NOW());


# Add item 2
INSERT INTO item (kind)
VALUES ("Action");

# Add message 2
INSERT INTO message(item_id, sender, sent_to, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Dwell", "cgabaldon@gmail.com", "This week from Dwell.", "Body..", "", "", "", NOW());

# Add item 3
INSERT INTO item (kind)
VALUES ("Action");

# Add message 3
INSERT INTO message(item_id, sender, sent_to, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Amazon.com", "cgabaldon@gmail.com", "Amazon Instant Video: New Releases and the Weekend Movie Sale", "Body..", "", "", "",  NOW());



################################# ADD HOLD ITEMS ##############################
INSERT INTO item (kind)
VALUES ("Hold");


# Add message 1
INSERT INTO message(item_id, sender, sent_to, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Groupon", "cgabaldon@gmail.com", "50% off at the Potato Barn", "Body..", "", "", "", NOW());


# Add item 2
INSERT INTO item (kind)
VALUES ("Hold");

# Add message 2
INSERT INTO message(item_id, sender, sent_to, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Amazon Local", "cgabaldon@gmail.com", "New this week", "Body..", "", "", "", NOW());

# Add item 3
INSERT INTO item (kind)
VALUES ("Hold");

# Add message 3
INSERT INTO message(item_id, sender, sent_to, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Amazon.com", "cgabaldon@gmail.com", "Amazon Instant Video: New Releases and the Weekend Movie Sale", "Body..", "", "", "",  NOW());

# Add item 4
INSERT INTO item (kind)
VALUES ("Hold");

# Add message 4
INSERT INTO message(item_id, sender, sent_to, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Warby Parker", "cgabaldon@gmail.com", "We have shipped your glasses.", "Body..", "", "", "", NOW());

# Add item 5
INSERT INTO item (kind)
VALUES ("Hold");

# Add message 5
INSERT INTO message(item_id, sender, sent_to, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Warby Parker", "cgabaldon@gmail.com", "Your Warby Parker order no. 100194087 has been received and will ship out shortly", "Body..", "", "", "", NOW());


################################# ADD COMPLETED ITEMS ##############################
INSERT INTO item (kind)
VALUES ("Completed");


# Add message 1
INSERT INTO message(item_id, sender, sent_to, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Mint.com", "cgabaldon@gmail.com", "Your tax refund has arrived.", "Body..", "", "", "", NOW());


# Add item 2
INSERT INTO item (kind)
VALUES ("Completed");

# Add message 2
INSERT INTO message(item_id, sender, sent_to, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Dwell", "cgabaldon@gmail.com", "This week from Dwell.", "Body..", "", "", "", NOW());

# Add item 3
INSERT INTO item (kind)
VALUES ("Completed");

# Add message 3
INSERT INTO message(item_id, sender, sent_to, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Amazon.com", "cgabaldon@gmail.com", "Amazon Instant Video: New Releases and the Weekend Movie Sale", "Body..", "", "", "",  NOW());

# Add item 4
INSERT INTO item (kind)
VALUES ("Completed");

# Add message 4
INSERT INTO message(item_id, sender, sent_to, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Warby Parker", "cgabaldon@gmail.com", "Your Warby Parker order no. 100194087 has been received and will ship out shortly", "Body..", "", "", "", NOW());


# Add item 5
INSERT INTO item (kind)
VALUES ("Completed");

# Add message 5
INSERT INTO message(item_id, sender, sent_to, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Amazon.com", "cgabaldon@gmail.com", "Amazon Instant Video: New Releases and the Weekend Movie Sale", "Body..", "", "", "",  NOW());

# Add item 6
INSERT INTO item (kind)
VALUES ("Completed");

# Add message 6
INSERT INTO message(item_id, sender, sent_to, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Warby Parker", "cgabaldon@gmail.com", "Your Warby Parker order no. 100194087 has been received and will ship out shortly", "Body..", "", "", "", NOW());


