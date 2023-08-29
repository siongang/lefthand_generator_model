from music21 import *
import os
import to_mid


# changes note to its enharmonic
def get_enharmonic_sharp(note_name):
    p = pitch.Pitch(note_name)
    enharmonic_sharp = p.getEnharmonic()
    return enharmonic_sharp.nameWithOctave

# returns an array of notes of the chords, fe: ['A4','C#4']
def get_notes (note_or_rest):
    chord_notes = []
    for note in note_or_rest.pitches:
        name = note.nameWithOctave
        if "-" in note.name:
            name = get_enharmonic_sharp(note.nameWithOctave)
        chord_notes.append(name)
    return chord_notes

# turns an xml file to txt file for data processing
def to_input_txt(input_path, output_path,name):
    # # Specify the path to the folder containing the MusicXML files
    # xml_folder_path = 'xml_folder/saved_xml/pop'  # Replace with the actual path


    # # Get a list of filenames in the folder
    # xml_filenames = [filename for filename in os.listdir(xml_folder_path) if filename.endswith('.musicxml')]




    # counter = 1
    # xml_filenames=['saved_xml/pop/Passacaglia.musicxml']


    # # changing musicxml files to txt
    # for file in xml_filenames:
    score = converter.parse(input_path)
    # Assume that the first part corresponds to the right hand and the second part corresponds to the left hand
    right_hand_part = score.parts[0]
    left_hand_part = score.parts[1]

    # Define a mapping of note names to your array representation
    note_mapping = {
        'rest': 'z'
    }

    # Function to convert a note or rest to your array representation
    def convert_to_array_element(note_or_rest):
        if isinstance(note_or_rest, chord.Chord): # If chord
            return get_notes(note_or_rest)
        elif isinstance(note_or_rest, note.Note): # if note
            return get_notes(note_or_rest)
        elif isinstance(note_or_rest, note.Rest): # if rest
            return 'z'
        else:
            return ""


    # MAKE MORE PRETTY
    # Convert right hand notes to array
    right_hand_array = []
    for element in right_hand_part.flat:
        duration = round(element.duration.quarterLength * 4)
        array_element = convert_to_array_element(element)
        if array_element:
            for i in range(int(duration)):
                right_hand_array.append(array_element)


    # Convert left hand notes to array
    left_hand_array = []
    for element in left_hand_part.flat:
        duration = round(element.duration.quarterLength * 4)
        array_element = convert_to_array_element(element)
        if array_element:
            for i in range(int(duration)):
                left_hand_array.append(array_element)
                

    # saving files
    train_right = []
    train_left = []

    # modifying the data so that chords are represented by one string
    # Make more pretty
    for el in right_hand_array:
        temp = ''
        for right in el:
            temp=temp+str(right)
        train_right.append(temp)

    for el in left_hand_array:
        temp = ''
        for left in el:
            temp=temp+str(left)
        train_left.append(temp)



    # Specify the path to the output text file
    output_file_path = f'{output_path}/right/{name}.txt'

    # Open the file in write mode and save the array
    with open(output_file_path, 'w') as f:
        for element in train_right:
            f.write(str(element)+'\n')

    print("Array saved to:", output_file_path)

    # Specify the path to the output text file
    output_file_path = f'{output_path}/left/{name}.txt'

    # Open the file in write mode and save the array
    with open(output_file_path, 'w') as f:
        for element in train_left:
            f.write(str(element)+'\n')


    print("Array saved to:", output_file_path)
    # to_mid.audio(right_hand_array, left_hand_array,input_path)
    # counter = counter + 1

    print(len(right_hand_array))
    print(len(left_hand_array))




