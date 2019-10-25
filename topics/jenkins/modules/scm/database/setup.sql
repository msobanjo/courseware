DROP TABLE IF EXISTS Books;

CREATE TABLE Books (
        ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Name varchar(255) NOT NULL,
        Author varchar(255) NOT NULL,
        Image varchar(255) NOT NULL
);

INSERT INTO Books (
        Name, Author, Image
) VALUES (
        "Way of the Wolf",
        "Jordan Belfort",
        "https://books.google.com/books/content/images/frontcover/5jYvDwAAQBAJ?fife=w200-h300"
);

INSERT INTO Books (
        Name, Author, Image
) VALUES (
        "The Beautiful Poetry of Donald Trump",
        "Robert Sears",
        "https://books.google.com/books/content/images/frontcover/68CnDwAAQBAJ?fife=w200-h300"
);

SELECT * FROM Books;