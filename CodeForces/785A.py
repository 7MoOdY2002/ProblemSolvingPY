tetra = "Tetrahedron"
cube = "Cube"
octa = "Octahedron"
dode = "Dodecahedron"
ico = "Icosahedron"
ans = 0
n = int(input())
for i in range(n):
    string1 = str(input())
    if string1 == tetra:
        ans += 4
    elif string1 == cube:
        ans += 6
    elif string1 == dode:
        ans += 12
    elif string1 == octa:
        ans += 8
    else:
        ans += 20
print(ans)
