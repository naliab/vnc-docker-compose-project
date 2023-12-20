CREATE TABLE IF NOT EXISTS house_prices (
    id INTEGER NOT NULL,
    property_type TEXT NULL,
    price INTEGER NULL,
    location TEXT NULL,
    city TEXT NULL,
    baths INTEGER NULL,
    purpose TEXT NULL,
    bedrooms INTEGER NULL,
    Area_in_Marla FLOAT NULL,
    PRIMARY KEY (id)
);

COPY house_prices FROM '/house_prices.csv' CSV HEADER;