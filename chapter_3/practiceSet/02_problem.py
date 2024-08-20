letter = ''' Dear <|Name|>,
            You are selected!
            <|Date|> ''';

print(letter.replace("<|Name|>", "Ankush").replace("<|Date|>", "24th September 2032"));