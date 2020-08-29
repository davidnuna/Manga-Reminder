class Manga(object):
    def __init__(self, name, chapter, website):
        self.name = name
        self.chapter = int(chapter)
        self.website = website

    def __str__(self):
        return str(self.name + ", " + str(self.chapter) + ", " + self.website + "\n")

    @staticmethod
    def read_from_file(line):
        manga_fields = line.split(",")
        return Manga(manga_fields[0], manga_fields[1], manga_fields[2])
    
    @staticmethod
    def write_to_file(manga):
        return str(manga.name + "," + str(manga.chapter) + "," + manga.website + "\n")


def read_file():
    mangas = []
    with open("mangas.txt", "r") as file:
        lines_in_file = file.readlines()
        for line in lines_in_file:
            line = line.strip()
            if line != "":
                mangas.append(Manga.read_from_file(line))

    return mangas


def update_file(mangas):
    with open("mangas.txt", "w") as file:
        for manga in mangas:
            new_line = Manga.write_to_file(manga)
            file.write(new_line)