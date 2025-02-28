# Contains code for interacting with the ai and for facilitating data understanding
def get_translations(file_name):
    translations = {}
    with open(file_name, 'r') as file:
        for line in file:
            # Process each line
            subdictionary = {}
            column, categories = line.strip().split(":")
            words = categories.strip().split(",")
            i = 0
            for word in words:
                # Process each word
                meaning, code = word.strip().split("=")
                subdictionary[code] = i
                subdictionary[i] = meaning
                i += 1
            translations[column] = subdictionary
    return translations