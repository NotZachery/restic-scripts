Restic Backup Scripts
======================

This is a backup system which keeps versioned backups and de-duplicates them. Read more at https://restic.net/

How to install
----------------

1. Copy the files from git to the directories they represent, then copy `/etc/restic/env.sh.template` to `/etc/restic/env.sh`.

2. Edit `env.sh` and modify it for your current setup.

3. Edit `/usr/local/sbin/restic_backup.sh` and modify retention days, backup paths, and the backup tag
4. Run `sudo systemctl enable restic-backup.service restic-check.service restic-backup.timer restic-check.timer`
5. Run `sudo systemctl start restic-backup.service restic-backup.timer restic-check.timer`

Note: This will start an immediate backup.
Optionally you can also do the following to allow for email or discord notification failures for the backup system:

6. Edit `/usr/local/sbin/discord_notify.py` and add your channel bot webhook
7. Edit `/etc/systemd/system/status-email-user@.service` and add your email address
8. Run `sudo systemctl enable discord-notify@restic-backup.service discord-notify@restic-check.service`
9. Run `sudo systemctl enable status-email-user@restic-backup.service status-email-user@restic-check.service`


The discord unit file (aka: `discord-notify@.service`) can be used to send any systemd service failure to discord
which is useful for checking to see if backups failed or if another service is failing to start for one reason 
or another. You can use this to get better diagnostics on what is going on. You can do the same with `status-email-user@.service` for emails instead.
