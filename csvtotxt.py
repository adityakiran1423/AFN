# script to take movies from .csv and put in .txt
import csv


def main():
    with open("MoviesData.csv", newline="") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", quotechar="|")
        f = open("movies.txt", "a")
        i = 0
        for row in reader:
            movie_name = row[0]
            f.write(str(i) + ", " + movie_name + "\n")
            # print(f"Appended {movie_name}")
            i += 1
    f.close()


main()
