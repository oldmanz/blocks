from dataclasses import dataclass
import json
import random

@dataclass
class Side:
    value: str
    
    def __post_init__(self):
        self.value = self.value.strip().lower()
    
    
@dataclass
class Block:
    sides: list[Side]
    available: bool = True
    
    
@dataclass
class Blocks:
    blocks: list[Block]
    
    def __available_blocks(self):
        return [block for block in self.blocks if block.available]
    
    def get_value(self, value):
        for block in self.__available_blocks():
            for side in block.sides:
                if side.value == value:
                    block.available = False
                    return block
        return None
    
    def shuffle(self):
        random.shuffle(self.blocks)
    
    def reset(self):
        for block in self.blocks:
            block.available = True
            
            
            
def create_blocks():
    raw = [
        'a n j',
        'b k o',
        'c x b y',
        'd x c w',
        'e w v d',
        'f s w',
        'g x t',
        'h y u',
        'i z v',
        'j w o a',
        'k x b',
        'l k o p',
        'm z o',
        'n l m o',
        'o p l k',
        'p j k q',
        'q d m',
        'r h i s',
        's t h g',
        't f g u',
        'u v f e',
        'v d e w',
        'w x d c',
        'x b c y',
        'y z b a',
        'z m a n',        
        's i h r',
        'n a j',
        'e l y',
        'r j i q',
        'o b k',
        'l c p',
        'g u t f'
    ]
    blocks = []
    for l in raw:
        values = l.split(' ')
        sides = [Side(value) for value in values]
        block = Block(sides)
        blocks.append(block)
        
        
    return Blocks(blocks)
     
            
def get_words():
    with open('words_dictionary.json', 'r') as f:
        data = json.load(f)
        print(len(data))
        return data.keys()


def check_word(word, blocks, iteration=0):
    if iteration >= 40:
        return False
    word = word.lower()
    blocks.reset()
    for letter in word:
        if not blocks.get_value(letter):
            blocks.shuffle()
            return check_word(word, blocks, iteration + 1)
    return True
    


def find_longest_word():
    blocks = create_blocks()
    yes = []
    no = []
    words = get_words()
    for word in words:
        if check_word(word, blocks):
            yes.append(word)
        else:
            no.append(word)
    
    longest = max(yes, key=len)
    shortest = min(no, key=len)
    print('can:', len(yes), " - ", len(yes) / len(words) * 100)
    print('longest:', longest)
    print('cannot:', len(no), " - ", len(no) / len(words) * 100)
    print('shortest:', shortest)
    

    
        
        

find_longest_word()