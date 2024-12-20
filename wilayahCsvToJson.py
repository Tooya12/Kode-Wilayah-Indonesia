import csv
import ujson
import sys
from rich.progress import Progress
from rich import print
from time import sleep

try:
    print("1. permendagri-2019\n2. kepmendagri-2022")
    user = int(input("\nPilih angka: "))

except ValueError:
    print("Pilih dengan angka!")
    sys.exit(1)

if (user == 1):
    fileCsv = "dist/permendagri-2019.csv"
    output = "permendagri-2019.json"

elif (user == 2):
    fileCsv = "dist/kepmendagri-2022.csv"
    output = "kepmendagri-2022.json"

else:
    print("Pilih antara 1 atau 2!")
    sys.exit(1)

with Progress(transient=True) as progress:

    taskOne = progress.add_task("[yellow]Reading file...", total=1)

    with open(fileCsv, newline="") as file:
        fileCsv = list(csv.reader(file))
        file.close()

    progress.update(taskOne, advance=1)

    provinsi = None
    kabupaten_kota = None
    kecamatan = None
    kelurahan_desa = None

    checkPoint = 0
    dictCsv = {}

    totalTaskTwo = len(fileCsv) + 2

    taskTwo = progress.add_task("[yellow]Processing json...", total=totalTaskTwo)

    for itter in fileCsv:
        for repeat in range(2):

            if (repeat == 0):
                lenOfNumber = len(itter[0])

                if (lenOfNumber == 2):
                    provinsi = itter[1]

                    dictCsv.update({provinsi: {"value": itter[0]}})
                    progress.update(taskTwo, advance=1)

                if (lenOfNumber == 5):
                    kabupaten_kota = itter[1]

                    dictCsv[provinsi].update({kabupaten_kota: {"value": itter[0]}})
                    progress.update(taskTwo, advance=1)

                if (lenOfNumber == 8):
                    kecamatan = itter[1]

                    dictCsv[provinsi][kabupaten_kota].update({kecamatan: {"value": itter[0]}})
                    progress.update(taskTwo, advance=1)

                if (lenOfNumber == 13):
                    kelurahan_desa = itter[1]

                    dictCsv[provinsi][kabupaten_kota][kecamatan].update({kelurahan_desa: {"value": itter[0]}})
                    progress.update(taskTwo, advance=1)

    json = ujson.dumps(dictCsv, indent=4)
    progress.update(taskTwo, advance=1)

    with open(output, "w") as file:
        file.write(json)
        file.close()

    sleep(0.6)
    progress.update(taskTwo, advance=1)
    print("\n[green]Success making json...")
