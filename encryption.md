# Encryption
### Types of Encryption
- <strong>1-Way</strong>
	- Can be encrypted but not decrypted (hashing)
	- Hashing algorithm needs to be **consistent**

- <strong>2-Way</strong>
	- Can be encrypted and then decrypted
	- Used for communication

### Why do we encrypt data if everyone has access to the hashing algorithm(s)?
- We 'sprinkle some salt' into each password to make it much harder to guess
- Each encrypted password is stored with a unique salt
