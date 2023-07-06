def load_song(file: str) -> list:
    '''This method breaks the song in different parts where the sections and also
    the chord and lyric parts get split up so it is easier to work with them.'''
    if ".txt" not in file:
        file = file + ".txt"
    with open(file, "r") as tf:
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

        # loop the split indices and 
        for index in split_indices:
            part = lines[prev:index]
            part[0].replace("\t", " ")
            if part[0] == "":
                part.pop(0)
            sections.append(part)
            prev = index

        sections.append(lines[split_indices[-1]:])

        sections[-1].pop(0)

        # split chords and lyrics into chunks
        song_object = []
        for i in range(0, len(sections)):
            chords = sections[i][::2]
            lyrics = sections[i][1::2]
            song_object.append(list(map(list, zip(chords, lyrics))))
        
        return song_object

def shift_chord(chord: str, shift: int):
    chords = ["C","C*","D","D*","E","F","F*","G","G*","A","A*","H"]
    if "*" in chord:
        rel_chords = []
        for i, x in enumerate(chords):
            if chord[:2] == x:
                start = chords[i:]
                for s in start:
                    rel_chords.append(s)
                end = chords[:i]
                for e in end:
                    rel_chords.append(e)
        if "m" in chord:
            return rel_chords[shift] + "m"
        elif "7" in chord:
            return rel_chords[shift] + "7"
        else:
            return rel_chords[shift]
    else:
        rel_chords = []
        for i, x in enumerate(chords):
            if list(chord)[0].upper() == x:
                start = chords[i:]
                for s in start:
                    rel_chords.append(s)
                end = chords[:i]
                for e in end:
                    rel_chords.append(e)
        if "m" in chord:
            return rel_chords[shift] + "m"
        elif "7" in chord:
            return rel_chords[shift] + "7"
        else:
            return rel_chords[shift]
        
def shift_song(file: str, shift: int):
    song = load_song(file)
    for i, section in enumerate(song):
        for item in section:
            chords = item[0].split(" ")
            chord_str = ""
            for chord in chords:
                if chord != "":
                    chord_str += shift_chord(chord, shift)
                else:
                    chord_str += " "
            item[0] = chord_str
    
    for section in song:
        print("")
        for item in section:
            print(item[0])
            print(item[1])

shift_song("house_of_the_rising_sun", -5)