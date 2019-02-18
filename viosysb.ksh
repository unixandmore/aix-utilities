#!/usr/bin/ksh93

DATE="$(date '+%Y_%m%d_%a')"
HOSTNAME="$(hostname)"
OTHERVG="${OTHERVG:-lparvg}"
NFSMNT="${NFSMNT:-/mnt/backup}"

print "DEBUG: ${OTHERVG} ${NFSMNT}/${HOSTNAME}_${DATE}.mksysb"
#su - padmin -c "ioscli savevgstruct ${OTHERVG}"
su - padmin -c "ioscli viosbr -backup --file /tmp/viosabr.backup"
#Mount the NFS repository for the backups (/nfsmnt)
su - padmin -c "ioscli backupios -file ${NFSMNT}/${HOSTNAME}_${DATE}.mksysb  -mksysb"
