with open ("test.csv", "a", newline='') as f:
    writer = csv.writer(f, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in range(1,100):
        a = str(i).zfill(8)
        b = str(i).zfill(8)
        c = str(i)
        d = str(i).zfill(15)
        e = str(i).zfill(8)
        writer.writerow(['"' + a + '"','"' + b + '"','"' + c + '"','"' + d + '"','"' + e + '"'])
