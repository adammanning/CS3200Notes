# Registration

## Algorithm for Registration
1. Form (inputs) / UI to gather attributes of the new user
1. AJAX: Submit data to API (POST/users)
1. Validate email uniqueness
	1. HTML Status Code (422) for failed email validation
	1. If validation fails: Send code 422 and inform the user
1. Encrypt (hash/pash) password
1. Save data to database
	1. Send code 201 OK for successful creation and inform the user
---
