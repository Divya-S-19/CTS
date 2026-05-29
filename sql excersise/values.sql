INSERT INTO Users
(user_id, full_name, email, city, registration_date)
VALUES
(1,'Alice Johnson','alice@example.com','New York','2024-12-01'),
(2,'Bob Smith','bob@example.com','Los Angeles','2024-12-05'),
(3,'Charlie Lee','charlie@example.com','Chicago','2024-12-10'),
(4,'Diana King','diana@example.com','New York','2025-01-15'),
(5,'Ethan Hunt','ethan@example.com','Los Angeles','2025-02-01'),
(6,'Sophia Brown','sophia@example.com','Chicago','2025-03-01'),
(7,'Michael Davis','michael@example.com','Boston','2025-03-10'),
(8,'Emma Wilson','emma@example.com','Seattle','2025-03-15'),
(9,'James Taylor','james@example.com','New York','2025-04-01'),
(10,'Olivia Martin','olivia@example.com','Chicago','2025-04-05');
INSERT INTO Events VALUES
(1,'Tech Innovators Meetup',
'A meetup for tech enthusiasts.',
'New York',
'2025-06-10 10:00:00',
'2025-06-10 16:00:00',
'upcoming',1),

(2,'AI & ML Conference',
'Conference on AI and ML advancements.',
'Chicago',
'2025-05-15 09:00:00',
'2025-05-15 17:00:00',
'completed',3),

(3,'Frontend Development Bootcamp',
'Hands-on training on frontend tech.',
'Los Angeles',
'2025-07-01 10:00:00',
'2025-07-03 16:00:00',
'upcoming',2),

(4,'Cloud Computing Summit',
'Latest trends in cloud technologies.',
'Boston',
'2025-08-10 09:00:00',
'2025-08-10 17:00:00',
'upcoming',7),

(5,'Data Science Workshop',
'Hands-on data science training.',
'Chicago',
'2025-04-15 09:00:00',
'2025-04-15 16:00:00',
'completed',6),

(6,'Cyber Security Forum',
'Security awareness and best practices.',
'Seattle',
'2025-09-05 10:00:00',
'2025-09-05 18:00:00',
'cancelled',8);
INSERT INTO Sessions VALUES
(1,1,'Opening Keynote','Dr. Tech',
'2025-06-10 10:00:00','2025-06-10 11:00:00'),

(2,1,'Future of Web Dev','Alice Johnson',
'2025-06-10 11:15:00','2025-06-10 12:30:00'),

(3,2,'AI in Healthcare','Charlie Lee',
'2025-05-15 09:30:00','2025-05-15 11:00:00'),

(4,3,'Intro to HTML5','Bob Smith',
'2025-07-01 10:00:00','2025-07-01 12:00:00'),

(5,4,'Cloud Basics','Michael Davis',
'2025-08-10 09:00:00','2025-08-10 10:30:00'),

(6,4,'AWS Deep Dive','Michael Davis',
'2025-08-10 11:00:00','2025-08-10 12:30:00'),

(7,5,'Python for Data Science','Sophia Brown',
'2025-04-15 09:00:00','2025-04-15 11:00:00'),

(8,5,'Machine Learning','Charlie Lee',
'2025-04-15 11:30:00','2025-04-15 13:00:00');
INSERT INTO Registrations VALUES
(1,1,1,'2025-05-01'),
(2,2,1,'2025-05-02'),
(3,3,2,'2025-04-30'),
(4,4,2,'2025-04-28'),
(5,5,3,'2025-06-15'),
(6,6,5,'2025-04-01'),
(7,7,4,'2025-07-01'),
(8,8,6,'2025-08-01'),
(9,9,1,'2025-05-05'),
(10,10,5,'2025-04-02'),
(11,1,5,'2025-04-03'),
(12,2,5,'2025-04-04');
INSERT INTO Feedback VALUES
(1,3,2,4,'Great insights!','2025-05-16'),
(2,4,2,5,'Very informative.','2025-05-16'),
(3,2,1,3,'Could be better.','2025-06-11'),
(4,6,5,5,'Excellent workshop','2025-04-16'),
(5,10,5,4,'Very useful session','2025-04-16'),
(6,1,5,5,'Loved the content','2025-04-16'),
(7,2,5,2,'Need more examples','2025-04-16'),
(8,9,1,4,'Good event','2025-06-11');
INSERT INTO Resources VALUES
(1,1,'pdf',
'https://portal.com/resources/tech_meetup_agenda.pdf',
'2025-05-01 10:00:00'),

(2,2,'image',
'https://portal.com/resources/ai_poster.jpg',
'2025-04-20 09:00:00'),

(3,3,'link',
'https://portal.com/resources/html5_docs',
'2025-06-25 15:00:00'),

(4,4,'pdf',
'https://portal.com/resources/cloud_guide.pdf',
'2025-07-20 10:00:00'),

(5,5,'image',
'https://portal.com/resources/ds_workshop.jpg',
'2025-04-01 12:00:00'),

(6,5,'link',
'https://portal.com/resources/ml_notes',
'2025-04-10 09:00:00');
SELECT COUNT(*) AS total_users FROM Users;
SELECT COUNT(*) AS total_events FROM Events;
SELECT COUNT(*) AS total_sessions FROM Sessions;
SELECT COUNT(*) AS total_registrations FROM Registrations;
SELECT COUNT(*) AS total_feedback FROM Feedback;
SELECT COUNT(*) AS total_resources FROM Resources;
SELECT * FROM Users;
SELECT * FROM Events;
SELECT * FROM Sessions;
SELECT * FROM Registrations;