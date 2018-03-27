import sys
from . import main

rc = 1
try:
    main()
    rc = 0
except Exception as e:
    print >>sys.stderr, 'Error: %s' % e
sys.exit(rc)
