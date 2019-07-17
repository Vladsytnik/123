---------------------------------------------------------------------
-- Core function to access the PAGC address standardizer
-- Author: Stephen Woodbridge <woodbri@imaptools.com>
---------------------------------------------------------------------

CREATE OR REPLACE FUNCTION standardize_address(
        lextab text,
        gaztab text,
        rultab text,
        micro text,
        macro text )
    RETURNS stdaddr
    AS  '$libdir/address_standardizer', 'standardize_address'
    LANGUAGE 'c' IMMUTABLE STRICT COST 200;

CREATE OR REPLACE FUNCTION standardize_address(
        lextab text,
        gaztab text,
        rultab text,
        address text )
    RETURNS stdaddr
    AS  '$libdir/address_standardizer', 'standardize_address1'
    LANGUAGE 'c' IMMUTABLE STRICT COST 200;

CREATE OR REPLACE FUNCTION parse_address(IN text,
        OUT num text,
        OUT street text,
        OUT street2 text,
        OUT address1 text,
        OUT city text,
        OUT state text,
        OUT zip text,
        OUT zipplus text,
        OUT country text)
    RETURNS record
    AS  '$libdir/address_standardizer', 'parse_address'
    LANGUAGE 'c' IMMUTABLE STRICT;


