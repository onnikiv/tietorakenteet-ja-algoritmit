reference_string = 'abcdefghijklmnopqrstuvwxyz'

def custom_encoder(input_string):
    positions = []
    for char in input_string.lower():
        if char != None:
            positions.append(reference_string.find(char))
    
    return positions

