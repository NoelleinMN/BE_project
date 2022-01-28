# BE_project

## Repo for BE

- AWS microservice (Python)
- AWS API Gateway
- AWS Lambda
- SQL/NoSQL DB

### Notes

Seeded two customers w/crmId

Working API routes:

1. [Landing-ish page](https://6oabk6kpg9.execute-api.us-east-2.amazonaws.com/hi)
1. Return [all customers](https://6oabk6kpg9.execute-api.us-east-2.amazonaws.com/allCustomers)
1. [Search by branchId](https://6oabk6kpg9.execute-api.us-east-2.amazonaws.com/searchCustomer?branchId=9b35ca96-cb7e-456f-a9f6-51af365eea9b)

CLI commands:

1. `curl -v https://6oabk6kpg9.execute-api.us-east-2.amazonaws.com/hi` (remove -v for non-verbose, json-only response)
1. `curl -v -X "PUT" -H "Content-Type: application/json" -d "{\"branchId\": \"abcdef123456\"}" https://6oabk6kpg9.execute-api.us-east-2.amazonaws.com/newCustomer` (returns "not working yet")
1. `curl https://6oabk6kpg9.execute-api.us-east-2.amazonaws.com/searchCustomer?branchId=9b35ca96-cb7e-456f-a9f6-51af365eea9b` (returns single search result from query parameter)

To be implemented:

- [ ] Error handling for search
    - [ ] message of no match
    - [ ] try regex for partial match; check for multiple items returned
- [ ] Create record method
- [ ] Update record method
