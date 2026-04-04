CREATE FUNCTION search(p text)
RETURNS TABLE(id int, name varchar, phone varchar)
AS $$
BEGIN
    RETURN QUERY
    SELECT *
    FROM phonebook
    WHERE name ILIKE '%' || p || '%'
       OR phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;


CREATE FUNCTION get_contacts(limit_count int, offset_count int)
RETURNS TABLE(id int, name varchar, phone varchar)
AS $$
BEGIN
    RETURN QUERY
    SELECT *
    FROM phonebook
    LIMIT limit_count OFFSET offset_count;
END;
$$ LANGUAGE plpgsql;