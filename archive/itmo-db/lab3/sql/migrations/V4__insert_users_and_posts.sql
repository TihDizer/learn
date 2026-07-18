WITH u as (
    INSERT INTO users (name)
    VALUES ( 'Anton') , ('Ivan')
    RETURNING id
)
INSERT INTO posts (text, owner_id)
SELECT CONCAT('My ', u.id, ' post'), u.id
FROM u;
