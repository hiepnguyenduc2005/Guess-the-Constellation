import random
import sys
import csv


def main():
    s = get_star()
    print(s)
    i = 1
    while i < 4:
        try:
            cons = input("IAU constellation: ").strip().title()
            c = get_constellation(cons)
            result = compare_pair(s, c)
            if result == "Correct":
                print(result)
                print("The answer is", final_result(s))
                break
            else:
                i += 1
                print(result)
                pass
        except:
            i += 1
            print("Invalid input")
            pass
    if i == 4:
        print("The answer is", final_result(s))


def get_star():
    stars = []
    with open("bright_star.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            stars.append(row)
    star = random.choice(stars)
    return star["star"]


def get_constellation(cons):
    constellation = f"{cons}\n"
    with open("constellation.txt", "r") as file:
        constellations = file.readlines()
    if constellation not in constellations:
        sys.exit("Invalid input")
    return cons


def compare_pair(star, constellation):
    stars = []
    with open("bright_star.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            stars.append(row)
    starr = {"star": star, "constellation": constellation}
    if starr in stars:
        return "Correct"
    else:
        return "Incorrect"


def final_result(star):
    stars = []
    with open("bright_star.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            stars.append(row)
    for starr in stars:
        if star == starr["star"]:
            return starr["constellation"]


if __name__ == "__main__":
    main()
