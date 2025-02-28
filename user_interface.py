# Contains code for interacting with the ai and for facilitating data understanding
def get_translations(file_name):
    translations = {}
    with open(file_name, 'r') as file:
        for line in file:
            if line.strip() and line[0] != "#":
                # Process each line
                if "#" in line:
                    line = line[:line.index("#")]
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

def get_features(model, columns, print_features=False):
    feature_importances = model.feature_importances_
    feature_name_and_importance = []
    for i in range(len(feature_importances)):
        feature_name_and_importance.append((columns[i], feature_importances[i]))
        # print(f'{X.columns[i]}: {feature_importances[i]}')
    sorted_features = sorted(feature_name_and_importance, key=lambda x: x[1], reverse=True)
    if print_features:
        for feature in sorted_features:
            print(f'{feature[0]}: {feature[1]}')
    return sorted_features

