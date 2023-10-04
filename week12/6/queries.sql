-- -- part 1:
-- SELECT * FROM film WHERE release_year = 2006 AND rental_rate >= 4;

-- -- part 2:
-- SELECT * FROM film ORDER BY length LIMIT 10;

-- -- part 3:
-- SELECT country, COUNT(customer_id) FROM customer cu
-- JOIN address ad ON cu.address_id = ad.address_id
-- JOIN city ci ON ad.city_id = ci.city_id
-- JOIN country co ON ci.country_id = co.country_id
-- --GROUP BY country ORDER BY country;

-- -- part 4:                          # There was a problem in question
-- SELECT title, rental_rate, rental_duration   FROM film ORDER BY title;

-- -- part 5:
-- SELECT  CONCAT(first_name,' ', last_name) as full_name,
-- count(payment_id) as count_rented_movies FROM customer c
-- JOIN payment p ON c.customer_id = p.customer_id
-- GROUP BY c.customer_id ORDER BY count_rented_movies DESC
-- LIMIT 10;

-- -- part 6:
-- SELECT first_name, last_name FROM customer cu
-- JOIN address ad ON cu.address_id = ad.address_id
-- JOIN city ci ON ad.city_id = ci.city_id
-- JOIN country co ON ci.country_id = co.country_id
-- WHERE country = 'United States' AND first_name LIKE 'A%';

-- -- part 7:
-- SELECT title, rental_duration, replacement_cost FROM film
-- WHERE rental_duration > 5 AND replacement_cost <15;
