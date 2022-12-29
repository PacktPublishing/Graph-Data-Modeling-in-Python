USE steam_data;
CREATE TABLE steam_play (id VARCHAR(100), game_name VARCHAR(255), type VARCHAR(10), hours FLOAT(10, 1), misc_column INT);
CREATE TABLE steam_purchase (id VARCHAR(100), game_name VARCHAR(255), type VARCHAR(10), game_purchased_flag FLOAT(2, 1), misc_column INT);
/* Load data in */
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/steam_play.csv' INTO TABLE steam_play FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\r\n';
LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 5.7/Uploads/steam_purchase.csv' INTO TABLE steam_purchase FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\r\n';
