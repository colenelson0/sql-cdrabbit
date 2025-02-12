-- artist table

DROP TABLE IF EXISTS artist;

CREATE TABLE IF NOT EXISTS artist(
  artist_id INTEGER NOT NULL,
  artist_name TEXT NULL,
  artist_type TEXT NOT NULL,
  PRIMARY KEY (artist_id)
);

-- cd table

DROP TABLE IF EXISTS cd;

CREATE TABLE IF NOT EXISTS cd(
  cd_id INTEGER NOT NULL,
  title TEXT NOT NULL,
  artist_id INTEGER NOT NULL,
  genre TEXT NOT NULL,
  rel_year INTEGER NOT NULL,
  in_stock INTEGER NOT NULL,
  sales INTEGER NOT NULL,
  PRIMARY KEY (cd_id)
  FOREIGN KEY (artist_id) REFERENCES artist(artist_id)
);

-- Insert Data

-- artists

INSERT INTO artist VALUES
(1, "John Coltrane", "solo"),
(2, "Noisia", "group"),
(3, "Flash Memory", "solo"),
(4, "Muffin and the Cat Scratches", "group"),
(5, "Polyphemus Florentinus", "group"),
(6, "Wilford Pearce", "solo"),
(7, "G Jones", "solo"),
(8, "J Dilla", "solo"),
(9, "Paula Baltasar", "solo"),
(10, "False Noise", "solo"),
(11, "The Beatles", "group"),
(12, "Nero", "group"),
(13, "Michael", "solo"),
(14, "Metallica", "group"),
(15, "Pendulum", "group");

-- cds

INSERT INTO cd VALUES
(1, "The Very Best Of", 4, "rock", 2005, 37, 73),
(2, "Paths", 7, "electronic", 2023, 15, 25),
(3, "Wireless", 3, "electronic", 2025, 0, 0),
(4, "Split the Atom", 2, "electronic", 2010, 13, 37),
(5, "A Love Supreme", 1, "jazz", 1965, 29, 71),
(6, "Both Sides of the Moon", 6, "pop", 2001, 34, 46),
(7, "Floral Strobe", 10, "electronic", 2020, 5, 15),
(8, "A World Without Itself", 5, "rock", 1998, 0, 20),
(9, "Feed Me", 4, "rock", 1980, 25, 45),
(10, "Let's Rock n Roll!", 9, "rock", 1986, 46, 44),
(11, "Giant Steps", 1, "jazz", 1960, 20, 60),
(12, "A Flash Memory Christmas", 3, "pop", 2024, 0, 0),
(13, "Closer", 2, "electronic", 2022, 12, 18),
(14, "Abbey Road", 11, "rock", 1969, 39, 91),
(15, "Donuts", 8, "hip hop", 2006, 28, 62),
(16, "Untitled", 6, "pop", 2004, 44, 76),
(17, "Welcome Reality", 12, "electronic", 2011, 21, 29),
(18, "Michael", 13, "world", 2007, 30, 0),
(19, "Ride the Lightning", 14, "metal", 1984, 38, 82),
(20, "Hold Your Colour", 15, "electronic", 2005, 10, 30);