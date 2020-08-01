import sys


# Text File To Read:
filename = 'flexuretext.txt'


try:
    f = open(filename, 'r')  # open file and read contents

    times = []
    totaltime = 0

    for line in f:
        splitline = line.split("INTENSITY")  # separate strings where intensity is given
        splitline.pop(-1)  # remove last item in list (no intensity given here)

        i = 0
        for ea in splitline:
            ea1 = ea.strip()
            ea2 = ea1.strip("HR")
            ea3 = ea2.strip()
            trimmed = ea3[-10:]
            listed = trimmed.split()
            for grp in listed:
                no_decimal = grp.replace(".", "1")
                if no_decimal.isnumeric():
                    times.append(grp)
                else:
                    time = 0

        for t in times:
            i += 1
            print("process #" + str(i) + ":   " + t)

            totaltime += float(t)

        print("\ntotal workflow time = " + str(totaltime))

    f.close()

except:
    print("could not open file for reading")
