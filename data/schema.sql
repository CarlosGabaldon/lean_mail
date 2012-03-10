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
VALUES(LAST_INSERT_ID(), "customerservice@warbyparker.com", "cgabaldon@gmail.com", "Your Warby Parker order has shipped!", 
"
Thank you for shopping at Warby Parker!

Your Warby Parker order has shipped.

Order Summary:
Name	Qty
Winston Revolver Black	1
Anti-Reflective Polycarbonate Lenses	1


You can track your shipment on the UPS website by clicking here: 1ZA0285E0249761730*

*The tracking number above will become active within 24 hours for orders shipped Monday-Friday. If you receive this email on a Saturday or Sunday, your tracking number will become active on Tuesday. 

An Important Note About Your Lenses:
Our lenses are built to last, and come standard with premium anti-scratch and anti-reflective coatings. However, polycarbonate lenses (and especially our high index lenses) are sensitive to heat and can develop bubbles or cracks when exposed to too much of it. Please avoid using hot water when cleaning your lenses, and be sure to use low heat when having your frames adjusted.

We hope you love your glasses and want to thank you for helping give the gift of sight -- for every pair of glasses you buy, we provide a pair to someone in need. Click here to learn where we donate glasses. 

- The Warby Parker Team
"
, "", "", "", NOW());

INSERT INTO item (kind)
VALUES ("New");


# Add message 2
INSERT INTO message(item_id, sender, sent_to, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Mint.com", "cgabaldon@gmail.com", "Your tax refund has arrived.", "Body..", "", "", "", NOW());


# Add item 3
INSERT INTO item (kind)
VALUES ("New");

# Add message 3
INSERT INTO message(item_id, sender, sent_to, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Dwell", "cgabaldon@gmail.com", "This week from Dwell.", "Body..", "", "", "", NOW());

# Add item 4
INSERT INTO item (kind)
VALUES ("New");

# Add message 4
INSERT INTO message(item_id, sender, sent_to, subject, body, cc, bc, headers, sent_on)
VALUES(LAST_INSERT_ID(), "Amazon.com", "cgabaldon@gmail.com", "Amazon Instant Video: New Releases and the Weekend Movie Sale", "Body..", "", "", "",  NOW());

# Add item 5
INSERT INTO item (kind)
VALUES ("New");

# Add message 5
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


