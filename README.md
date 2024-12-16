My Life
Video Demo: <URL HERE>
Description:
My Life is a personal Flask web application designed to organize and centralize key areas of my daily life. It incorporates secure login features, password management, a list of fun activities, and a dedicated section for piano and singing goals.

The project uses a SQLite database (vegan.db) to store user and app-related data, and it securely handles passwords using encryption. The app ensures privacy and user control with session management, secure hashing, and encryption libraries.

Features:
1. User Registration and Login
Secure Registration: Users can create an account with a username and password. Passwords are securely hashed using werkzeug.security before being stored in the database.
Login System: The app validates user credentials during login and creates a session for authorized access.
Session Management: Active user sessions are managed using Flask-Session, ensuring that only logged-in users can access app features.
Logout: Users can log out at any time to end their session securely.
Routes:

/register: Register a new account.
/login: Log into the app.
/logout: Log out and clear the session.
2. Password Manager
The app provides a simple and secure way to store and manage passwords for different accounts. Passwords are encrypted using the cryptography.fernet library, with the encryption key securely stored in a .env file. Users can:

Add new accounts with a webpage name, username, and password.
View decrypted passwords for their accounts.
Delete entries they no longer need.
Routes:

/passwords: View, add, and delete passwords.
3. Fun Activities
This feature helps me manage a list of activities that I enjoy or want to try in the future. Users can:

Add activities to the list.
View all their current and planned activities.
Delete activities they no longer want on the list.
Routes:

/fun: View, add, and delete activities.
4. Piano & Singing Goals
This section is dedicated to my musical journey, where I can keep track of songs I want to learn to play on the piano and sing, as well as organize music goals for the band I am creating. Users can:

Add a song name and artist to their list.
View their musical goals.
Delete songs from the list when completed.
Routes:

/piano_sing: View, add, and delete piano/singing goals.
Technology Stack:
Python and Flask: For the backend framework.
SQLite: A lightweight relational database to store user data and app content.
Werkzeug Security: For password hashing and verification.
Cryptography (Fernet): For encrypting and decrypting sensitive data like passwords.
Flask-Session: To manage user sessions and ensure secure user access.
Environment Variables: The .env file stores sensitive keys, such as the encryption key and secret key, for added security.
How It Works:
User Registration and Login:

New users register with a username and password, which are stored securely.
Existing users log in to access their dashboard.
Passwords:

Users can add passwords for various accounts.
Passwords are encrypted before being saved to the database.
When viewing the list, the app decrypts passwords to display them in plain text.
Fun Activities:

Users can add and track activities they enjoy or want to try.
Piano & Singing:

Users can manage a list of songs they want to learn, including the song's name and artist.
Delete Functionality:

Users can delete entries from any list (passwords, activities, or songs).
Database Structure (vegan.db):
The database includes three main tables:

users: Stores user credentials (ID, username, and hashed password).
passwords: Stores encrypted passwords (ID, user ID, webpage, username, and encrypted password).
fun: Stores activities (ID, activity name, and user ID).
piano_sing: Stores musical goals (ID, song name, artist, and user ID).
Security:
Passwords are hashed using werkzeug.security.
Sensitive passwords are encrypted using cryptography.fernet, with a secure key loaded from a .env file.
User sessions are securely managed to prevent unauthorized access.
