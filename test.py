murid = {}
student = []

def biodata():
    nama = input("Siapakah nama anda: ")
    umur = input("berapakah umur anda: ")
    rumah = input("dimana anda tinggal: ")

    return nama, umur, rumah

def vertikal(students):
    for student in students:
        for key, value in student.items():
            print(key, value)

while True:
    murid = {}
    nama, umur, rumah = biodata()
    murid["nama"] = nama
    murid["umur"] = umur
    murid["rumah"] = rumah

    student.append(murid)
    # print(student)

    lagi = input("apakah masih mau mengisi biodata (y/n): ")
    if lagi == "y":
        continue
    else:
        break

vertikal(student)