CREATE TABLE nw_industry(  
    industry_code VARCHAR(6) PRIMARY KEY,
    industry_text VARCHAR(80),
    display_level SMALLINT,
    selectable CHAR,
    sort_sequence SMALLINT
);

CREATE TABLE nw_level(  
    level_code VARCHAR(2) PRIMARY KEY,
    level_text VARCHAR(30),
    display_level SMALLINT,
    selectable CHAR,
    sort_sequence SMALLINT
);

CREATE TABLE nw_occupation(  
    soc_code VARCHAR(6) PRIMARY KEY,
    soc_text VARCHAR(100),
    display_level SMALLINT,
    selectable CHAR,
    sort_sequence SMALLINT
);

CREATE TABLE nw_ownership(  
    ownership_code VARCHAR(1) PRIMARY KEY,
    ownership_text VARCHAR(40),
    display_level SMALLINT,
    selectable CHAR,
    sort_sequence SMALLINT
);

CREATE TABLE nw_starea(  
    state_code VARCHAR(2),
    area_code VARCHAR(5),
    area_text VARCHAR(64),
    display_level SMALLINT,
    selectable CHAR,
    sort_sequence SMALLINT
);

CREATE TABLE nw_subcell_id(  
    subcell_id_code VARCHAR(2) PRIMARY KEY,
    subcell_id_text VARCHAR(40),
    display_level SMALLINT,
    selectable CHAR,
    sort_sequence SMALLINT
);

CREATE TABLE nw_datatype_id(  
    datatype_id_code VARCHAR(2) PRIMARY KEY,
    datatype_id_text VARCHAR(40),
    display_level SMALLINT,
    selectable CHAR,
    sort_sequence SMALLINT
);

CREATE TABLE nw_estimate_id(  
    estimate_id_code VARCHAR(2) PRIMARY KEY,
    estimate_id_text VARCHAR(40),
    display_level SMALLINT,
    selectable CHAR,
    sort_sequence SMALLINT
);

CREATE TABLE nw_series(  
    series_id VARCHAR(30),
    seasonality CHAR,
    state_code VARCHAR(2),
    area_code VARCHAR(5),
    ownership_code CHAR,
    estimate_id_code CHAR(2),
    industry_code VARCHAR(6),
    soc_code VARCHAR(6),
    subcell_id_code CHAR(2),
    datatype_id_code CHAR(2),
    level_code CHAR(2),
    footnote_codes VARCHAR(10),
    begin_year CHAR(4),
    begin_period CHAR(3),
    end_year CHAR(4),
    end_period CHAR(3)
);

CREATE TABLE nw_all_data(  
    series_id VARCHAR(30),
    "year" CHAR(4),
    "period" CHAR(3),
    "value" DECIMAL
);

ALTER TABLE nw_series
DROP COLUMN footnote_codes