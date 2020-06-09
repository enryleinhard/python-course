murid = {}
student = []

while True:
    murid = {}
    nama = input("Siapakah nama anda: ")
    umur = input("berapakah umur anda: ")
    rumah = input("dimana anda tinggal: ")
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

for x in student:
    for key, value in x.items():
        print(key, value)