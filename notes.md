###### Notes

Run processes in the background on startup in Cloud 9:
 - http://stackoverflow.com/questions/20439267/how-to-start-automatically-cloud9-ide-on-server-startup
 
Postgres in Cloud 9:
 - http://stackoverflow.com/questions/28177912/postgres-database-setup-on-cloud9-asks-for-sudo-password 
 - `sudo -s` then `sudo -u postgres psql`
 - More notes: http://stackoverflow.com/questions/11919391/postgresql-error-fatal-role-username-does-not-exist
 - createuser -d -P -s mike
 - createdb -O mike phishingdb