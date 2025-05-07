def main():
    mass = int(input("m: "))
    energy = einstein(mass)
    print(f"E: {energy}")

def einstein(m):
    c = 300000000
    E = m * c ** 2
    return E

if __name__ == "__main__":
    main()
