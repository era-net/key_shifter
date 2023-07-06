def load_song() -> list:
    '''This method breaks the song in different parts where the sections and also
    the chord and lyric parts get split up so it is easier to work with them.'''
    with open("original.txt", "r") as tf:
        # get all lines from file
        raw_lines = tf.read().splitlines()

        # exclude title section
        lines = raw_lines[2:]

        # get chunk separators as indices
        split_indices = []
        for i, line in enumerate(lines):
            if line == "":
                split_indices.append(i)
        
        # split song sections into chunks
        sections = []
        prev = 0

        # loop the 
        for index in split_indices:
            part = lines[prev:index]
            if part[0] == "":
                part.pop(0)
            sections.append(part)
            prev = index

        sections.append(lines[split_indices[-1]:])

        sections[-1].pop(0)

        # print(sections)

        # split chords and lyrics into chunks
        song_object = []
        for i in range(0, len(sections)-1):
            chords = sections[i][::2]
            lyrics = sections[i][1::2]
            song_object.append(list(map(list, zip(chords, lyrics))))
        
        return song_object

def shift(chord: str, target: str):
    chords = ["C","C*","D","D*","E","F","F*","G","G*","A","A*","H"]

song = load_song()
for i, section in enumerate(song):
    for n, item in enumerate(section):
        chords = item[0].split(" ")
        chord_str = ""
        for chord in chords:
            if chord != "":
                chord_str += chord
            else:
                chord_str += " "
        item[0] = chord_str