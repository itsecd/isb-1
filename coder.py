from Shifter import Shifter
from File import File
from sys import argv

def encode(text: str, key: int)->str:
    """Encodes the text given with the given key

    Args:
        text (str): data
        key (int): shift

    Returns:
        str: encoded data with shift
    """
    buffer = str()
    try:
        shifter = Shifter(key)
    except:
        print("Error occured around key argument")
        exit()
    
    for letter in text:
        buffer += shifter.shift_encode(letter)
        
    return buffer
        
def read_config()->int:
    
    """Reads config file (==./coder_data/config by default)"""
    config_fn = str()
    
    try:
        config_fn = argv[1]
    except:
        config_fn = "./coder_data/config"
    
    key_file = File(config_fn,"r")
    
    try:
        return int(key_file.read().split()[0])
    except:
        print("Configuration file error (can't spell to int)")
        exit()

if __name__=="__main__":
    """C0der for russian text. Key must be from 0 to 33. Made on linux system (*.txt not used)
        Argv = config_filename
    """
    key = int()
    
    src_text = str()
    
    output_text = str()
    
    key = read_config()
   
    try:
        src_file = File("./coder_data/source_text", "r")
        src_text = src_file.read()
    except:
        print("Input file error (isn't it's name *.txt?)")
        exit()
    
    output_text = encode(src_text, key)
    
    try:
        out_file = File("./coder_data/output_text", "w")
        out_file.write(output_text)
    except:
        print("Output file error (does it already exist?)")
        exit()