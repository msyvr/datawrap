-- `customers` must must match the number of rows in staging.
-- Return records where not the case: the test will fail.
select *
from (
        select customers.customer_id
        from {{ ref('customers') }} cust
            left join {{ ref('stg_customers') }} stg_cust on cust.customer_id = stg_cust.customer_id
        where stg_cust.customer_id is null
        UNION ALL
        select stg_cust.customer_id
        from {{ ref('stg_customers') }} stg_cust
            left join {{ ref('customers') }} cust on stg_cust.customer_id = cust.customer_id
        where cust.customer_id is null
    ) tmp
