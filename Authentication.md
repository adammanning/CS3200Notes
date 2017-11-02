# Authentication

## Steps to Authentication
1. Form to capture user information
	- Email and password
2. AJAX: Submit data to the API (POST/sessions)
3. Find user in the database by *email*
	- If exists:
		- Verify hashed password
			- If match:
				- Create a new session and send code 201 Created
			- else:
				- **FAIL**
	- else:
		- **FAIL**

## Fail
- Send code 401 Unauthenticated
- Inform the user
