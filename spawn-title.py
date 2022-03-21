import getopt
import sys
import random

class SpawnTitle:

    def __init__(self):
        self.title = 'PYTHON'
        self.side_spaces = 1
        self.char_border = '#'
        self.line_one  = ''
        self.line_two  = ''
        self.line_title = ''
        self.isActiveBorderStyle = False

    def create_border(self):
        total_char = len(self.title) + self.side_spaces * 2 + 2
        space_char = ''

        for index in range( total_char ):
            if self.isActiveBorderStyle :
                if index == 0 or index == total_char - 1:
                     self.line_two += self.char_border
                else:
                    self.line_two += ' '

            self.line_one += self.char_border
            
                

        for index in range(self.side_spaces):
            space_char += ' ' 

        self.line_title = self.char_border + space_char + self.title + space_char + self.char_border

        if self.isActiveBorderStyle :
            return f'{self.line_one}\n{self.line_two}\n{self.line_title}\n{self.line_two}\n{self.line_one}'
        else:
            return f'{self.line_one}\n{self.line_title}\n{self.line_one}'


    def set_rand_char_border(self):
        # Some ASCCII characters
        number = random.randint(33, 126)
        self.char_border = chr(number)

    def set_char_border(self, char):
        if len(char) == 1:
            self.char_border = char;
        else:
            print("[+] -c  Only a character")
            sys.exit()

    def set_title_spaces(self, total):
        if total.isnumeric():
            self.side_spaces = int(total)
        else: 
            print("[+] -s   Left and Right spaces for title")
            sys.exit()

    def set_text(self, text):
        self.title = text

    def set_style_border_two(self, boolean):
         self.isActiveBorderStyle  = boolean



def print_options():
    print("Welcome \n")    
    print("[+]  -r      Sets a random border")
    print("[+]  -b      Adds two more lines for the title")
    print("[+]  -t      Sets the title")
    print("[+]  -s      Sets total spaces")
    print("[+]  -c      Sets a character")
    print("[+]  -h      --Help")


def main():
    title = SpawnTitle()
    argsList = sys.argv[1:]

    if '-r' in argsList:
        argsList.remove('-r')
        title.set_rand_char_border()

    if '-b' in argsList:
        argsList.remove('-b')
        title.set_style_border_two(True)

    if '-h' in argsList:
        argsList.remove('-h')
        print_options()
        sys.exit()


    try:

        arguments, values = getopt.getopt(argsList, "t:s:c:b:")

        for arg, argValue in arguments:
            if arg in ['-t']:
                title.set_text(argValue)

            if arg in ['-s']:
                title.set_title_spaces(argValue)

            if arg in ['-c']:
                title.set_char_border(argValue)                      
        
        print(title.create_border())

    except getopt.GetoptError as error:
        print(error)

    

main()