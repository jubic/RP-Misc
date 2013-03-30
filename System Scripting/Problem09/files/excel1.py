def row_only(col, n):
    cell = []

    for i in range(n):
        cell = cell + [col + str(i+1)]
        
    return cell

if __name__ == "__main__":
    print row_only("G", 19)  # prints a list ["G1", "G2", "G3", "G4", ..., "G19"]
