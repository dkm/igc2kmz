#
# Regular cron jobs for the igc2kmz package
#
0 4	* * *	root	[ -x /usr/bin/igc2kmz_maintenance ] && /usr/bin/igc2kmz_maintenance
