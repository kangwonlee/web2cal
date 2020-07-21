# https://stackoverflow.com/questions/3408097/
import icalendar
import sys


def main(argv=sys.argv):

    with open(sys.argv[1], 'rb') as f:
        cal = icalendar.Calendar.from_ical(f.read())
    
        for component in cal.walk():
            print(component.name)


if "__main__" == __name__:
    main(sys.argv)
