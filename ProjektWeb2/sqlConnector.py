from sqlalchemy import create_engine
db = create_engine('sqlite:///charterdb.sqlite')

# ispis u konzoli
db.echo = True
conn = db.connect() 
# Otvaramo transakciju

 

conn.execute("INSERT INTO 'category' (id, name, image) VALUES (1, 'Jahta motorna', 'static/img/jahta_head.jpg');")
conn.execute("INSERT INTO 'category' (id, name, image) VALUES (2, 'Gliser','static/img/gliser_head.jpg');")
conn.execute("INSERT INTO 'category' (id, name, image) VALUES (3, 'Jedrilica','static/img/jedrilica_head.jpg');")
conn.execute("INSERT INTO boat VALUES (1, 'Aicon 54', 18, 6, 3, 3, '2x800.0HP', 2650,  1, 2000, 1500,'static/img/54_1.jpeg' );")
conn.execute("INSERT INTO boat VALUES (2, 'Bluline 23', 15, 8, null, null, 'Yamaha 4T', 140,  2, 1800, 1500, 'static/img/23_1.jpeg' );")
conn.execute("INSERT INTO boat VALUES (3, 'Waw Marine 650', 12, 8, null, null, 'Duzuki 4T', 100,  2, 1200, 800, 'static/img/650_1.jpg' );")
conn.execute("INSERT INTO boat VALUES (4, 'Bavaria 41', 12, 8, 6, 2, 'Volvo 55', 210,  3, 3000, 1800, 'static/img/41_1.jpg' );")
conn.execute("INSERT INTO boat VALUES (5, 'Bavaria 45', 15, 10, 8, 4, 'Volvo 55', 210,  3, 3500, 2000, 'static/img/45_1.jpg' );")
conn.execute("INSERT INTO boat VALUES (6, 'Bavaria 46', 15, 10, 8, 4, 'Volvo 55', 210,  3, 3500, 2000, 'static/img/46_1.jpg' );")


conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (1, 5, 'static/img/45_1.jpg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (2, 5, 'static/img/45_2.jpg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (3, 5, 'static/img/45_3.jpg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (4, 5, 'static/img/45_4.jpg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (5, 5, 'static/img/45_5.jpg');")

conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (6, 1, 'static/img/54_1.jpeg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (7, 1, 'static/img/54_2.jpeg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (8, 1, 'static/img/54_3.jpeg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (9, 1, 'static/img/54_4.jpeg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (10, 1, 'static/img/54_5.jpeg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (11, 1, 'static/img/54_6.jpeg');")

conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (12, 2, 'static/img/23_1.jpeg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (13, 2, 'static/img/23_2.jpeg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (14, 2, 'static/img/23_3.jpeg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (15, 2, 'static/img/23_4.jpeg');")


conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (16, 3, 'static/img/650_1.jpg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (17, 3, 'static/img/650_2.jpg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (18, 3, 'static/img/650_3.jpg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (19, 3, 'static/img/650_4.jpg');")

conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (20, 4, 'static/img/41_1.jpg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (21, 4, 'static/img/41_2.jpg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (22, 4, 'static/img/41_3.jpg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (23, 4, 'static/img/41_4.jpg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (24, 4, 'static/img/41_5.jpg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (25, 4, 'static/img/41_6.jpg');")

conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (26, 6, 'static/img/46_1.jpg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (27, 6, 'static/img/46_2.jpg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (28, 6, 'static/img/46_3.jpg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (29, 6, 'static/img/46_4.jpg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (30, 6, 'static/img/46_5.jpg');")
conn.execute("INSERT INTO 'boat_image' (id, boat_id, image) VALUES (31, 6, 'static/img/46_6.jpg');")


 
# vratimo konekciju u "connection pool"
conn.close()