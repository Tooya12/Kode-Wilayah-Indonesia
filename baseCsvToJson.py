import csv
import ujson
from rich.progress import Progress
from rich import print

with Progress(transient=True) as progress:

    taskOne = progress.add_task("[yellow]Reading base.csv...", total=1)

    with open("dist/base.csv", newline="") as file:
        fileCsv = list(csv.reader(file))
        file.close()

    progress.update(taskOne, advance=1)

    provinsi = None
    kabupaten_kota = None
    kecamatan = None
    kelurahan_desa = None

    checkPoint = 0
    dictCsv = {}

    totalTaskTwo = len(fileCsv) * 2 + 2

    taskTwo = progress.add_task("[yellow]Processing base.csv to base.json...", total=totalTaskTwo)

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

    with open("base.json", "w") as file:
        file.write(json)
        file.close()

    progress.update(taskTwo, advance=1)
    print("[green]Success making base.json...")
