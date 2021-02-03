import os, sys, time

try:
    while True:
        os.system(' '.join(sys.argv[1:]))
        print('JUST FINISHED A TRAINING TASK. Waiting 10 secs.')
        time.sleep(10)
except KeyboardInterrupt:
    sys.exit(1)
