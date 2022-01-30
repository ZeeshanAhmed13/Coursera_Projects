
import sys
reload(sys)

for line in sys.stdin:
    try:
        count, word = line.strip().split('\t', 1)
        count = int(count)
        print '%s\t%d' % (word, count)
    except ValueError as e:
        continue
