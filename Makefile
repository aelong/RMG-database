################################################################################
#
#   Makefile for RMG-database
#
################################################################################

test-database:
	nosetests --nocapture --nologcapture -v -d testing/databaseTest.py	
