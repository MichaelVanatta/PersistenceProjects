CREATE INDEX index_soc_text ON nw_occupation (soc_text)
CREATE INDEX index_value ON nw_all_data ("value")

DROP MATERIALIZED VIEW "average_salary"

CREATE MATERIALIZED VIEW "average_salary" AS
SELECT o.soc_text, count(o.soc_text) AS records, round(avg("a"."value"), 2) AS average_value FROM nw_all_data AS "a"
JOIN nw_series AS s ON "a".series_id = s.series_id
INNER JOIN nw_occupation AS o ON s.soc_code = o.soc_code
WHERE s.area_code = '99999' AND "a"."value" IS NOT NULL
GROUP BY o.soc_text, o.soc_code
ORDER BY soc_text ASC

SELECT * from "average_salary"