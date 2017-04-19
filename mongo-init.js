db = db.getSiblingDB('flash');

if (!db.getUser('flash')) {
	db.createUser({ user: 'flash', pwd: 'flash', roles: 
		["readWrite", "dbAdmin"] 
	}); 
}
 
