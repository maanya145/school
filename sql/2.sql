CREATE TABLE Workers (
    WID VARCHAR(10),
    WNAME VARCHAR(50),
    WAGE INT,
    HOURS INT,
    TYPE VARCHAR(20),
    SITEID INT
);

INSERT INTO Workers (WID, WNAME, WAGE, HOURS, TYPE, SITEID) VALUES 
('W01', 'Ahmed J', 1500, 200, 'Unskilled', 103),
('W11', 'Naveen S', 520, 100, 'Skilled', 101),
('W02', 'Jacob B', 780, 95, 'Unskilled', 101),
('W15', 'Nihal K', 560, 110, 'Semiskilled', NULL),
('W10', 'Anju S', 1200, 130, 'Skilled', 103);


SELECT * FROM Workers;

select wname , wage*hours from workers where siteid=103;

select count(DISTINCT TYPE) FROM workers;

SELECT wname, siteid from workers where type='Unskilled' order BY `HOURS`;