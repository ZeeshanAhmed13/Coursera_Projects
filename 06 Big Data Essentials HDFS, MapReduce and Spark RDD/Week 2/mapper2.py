
import sys
reload(sys)

for line in sys.stdin:
    try:
        word, count = line.strip().split('\t', 1)
        count = int(count)
        print '%d\t%s' % (count, word)
    except ValueError as e:
        continue
