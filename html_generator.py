# html generator

def generate_html_frame(section_title, section_text):
    '''
    str, str -> str

    Input title and text strings, then output HTML code framework as strings.

    '''

    html_text_1 = '''
        <div class="section">
            <div class="section-title">
                ''' + section_title
    html_text_2 = '''
            </div>
            <div class="section-text">
                ''' + section_text
    html_text_3 = '''
            </div>
        </div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(section_list):
    '''
    list -> str

    Input a list of lists with section titles and associated text. Return a formatted str
    of HTML.

    '''

    html_text = ""
    for section in section_list:
        section_title = section[0]
        section_text = section[1]
        html_text += generate_html_frame(section_title, section_text)
    return html_text


programming_topics = [['OOP', '''Object-Oriented Programming (OOP) in Python refers to a class-based (hierarchical) system that organizes data structures. OOP is useful for reducing repetitive code and increasing intuitive data organization.

Class inheritance functions identically in Python as in CSS where subclasses have precedence over superclasses and instances have precedence over classes.
'''], ['Classes and Objects', '''A class defines an archetype of an object. An object (or instance) of a class is a specific version of that class. A constructor is used to initialize a class; Python uses the __init__ function name within a class definition. __init__ defines the attributes of the class.'''], ['Methods and Objects', '''Instance variables exist within a particular instance of a class. Scott Adams, who belongs to the class Human, is the assigned male to the instance variable gender. This is separate from the class variable gender, which allows for several possible designations, including male and female. Class variables are assigned at the class level of code, not the function level within a class.

Methods are functions associated with a particular class. Instance methods are functions within a class definition that control that class's behavior. Method overriding happens when subclass methods are executed over superclass methods of the same name; this is another case of specificity gaining precedence over more general code.
'''], ['Collections and Abstraction', '''Class inheritance functions identically in Python as in CSS where subclasses have precedence over superclasses and instances have precedence over classes.''']]

print make_HTML(programming_topics)