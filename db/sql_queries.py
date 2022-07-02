
# DROP TABLES

countries_table_drop = "DROP TABlE IF EXISTS countries;"

# CREATE TABLES

countries_table_create= ("""
CREATE TABLE IF NOT EXISTS countries
(
   
    dateFor TIMESTAMP,
    AB FLOAT,
    AR FLOAT,
    AG FLOAT,
    BC FLOAT,
    BH FLOAT,
    BN FLOAT,
    BT FLOAT,
    BV FLOAT,
    BR FLOAT,
    BZ FLOAT,
    CS FLOAT,
    CL FLOAT,
    CJ FLOAT,
    CT FLOAT,
    CV FLOAT,
    DB FLOAT,
    DJ FLOAT,
    GL FLOAT,
    GR FLOAT,
    GJ FLOAT,
    HR FLOAT,
    HD FLOAT,
    IL FLOAT,
    "IS" FLOAT,
    IF FLOAT,
    MM FLOAT,
    MH FLOAT,
    MS FLOAT,
    NT FLOAT,
    OT FLOAT,
    PH FLOAT,
    SM FLOAT,
    SJ FLOAT,
    SB FLOAT,
    SV FLOAT,
    TR FLOAT,
    TM FLOAT,
    TL FLOAT,
    VS FLOAT,
    VL FLOAT,
    VN FLOAT,
    B FLOAT,
    UNKNOWN FLOAT
    
);
""")

# QUERY LISTS

create_table_queries = [countries_table_create]
drop_table_queries = [countries_table_drop]

