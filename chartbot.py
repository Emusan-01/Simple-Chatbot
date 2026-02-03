import time
from countryinfo import CountryInfo
import pubchempy as pcp



input_saved = []
response_saved = []


def time_now():
    date_now = time.localtime(time.time())
    year, month, day, hour, minutes = date_now[0:5]
    return year, month, day, hour, minutes
    
def math_solver(equation):
        try:
            result = eval(equation)
            return  result
        except Exception as e:
            return str(e)

def user_response(value_saved, user_saved):
    user_saved_lower = user_saved[-1].lower().split()
    value_saved_lower = value_saved[-1].lower().strip(',').strip('?').replace('.', '').split()
    input_lower = input.lower().split()
    set_value = set(value_saved_lower)
    set_comp = set_value.difference(set_comp,arison)
    set_to_list = list(set_comp)
    for key, value in chatbot_responses.items():
        key_lower = key.lower().split()
        value_lower = value.lower().split()
        if all(keyword in set_to_list for keyword in value_lower):
            return value
            
            
def more_response(value_saved, user_saved):
    user_saved_lower = user_saved[-1].lower().strip(',').strip('?').strip('-').replace('.', '').split()
    value_saved_lower = value_saved[-1].lower().strip(',').strip('?').strip('-').replace('.', '').split()
    combine_list = user_saved_lower + value_saved_lower
    set_value = set(combine_list)
    set_comp = set_value.difference(set_comparison)
    set_to_list = list(set_comp)
    for key, value in chatbot_responses.items():
        key_lower = key.lower().split()
        value_lower = value.lower().split()
        if any(keyword in set_to_list for keyword in value_lower):
            return value
            
            
class Chatbot:
    
    def __init__(self, name, responses, value_saved, user_saved):
        self.name = name
        self.value_saved = value_saved
        self.user_saved = user_saved
        self.responses = responses

    def greet(self):
        print(f"Hello! I'm {self.name}")
            
    def country_info(self, countries):
        country = CountryInfo(countries)
        try:
            return f"Country Name: {country.name().capitalize()}\nCapital: {country.capital()}\nPopulation: {country.population()}\nArea (in square kilometers): {country.area()}\nRegion: {country.region()}\nSubregion: {country.subregion()}\nCurrency: {country.currencies()}\nLanguage: {country.languages()}\nDemonym: {country.demonym()}\nBorders: {country.borders()}"
        except Exception as e:
            return f"No info found for {e}"

    def chemical_name(self, chemical):
        try:
            for compound in pcp.get_compounds(chemical, "name"):
                return f"Info about {chemical}:-\nIUPAC Name: {compound.iupac_name}\nMolecular Weight: {compound.molecular_weight}\nFormula: {compound.molecular_formula}"
        except:
            return f"No information found for {chemical.capitalize()} OR No Internet Connection"
        
    def respond(self, input):
        input_strip = input.strip('?')
        input_lower = input_strip.lower().split()
        
        if input == "":
            return "Oops! Empty request was sent!"
        
        math_keywords = ['+', '-', '*', '/', '%', '^', '(', ')']
        if any(keyword in input for keyword in math_keywords):
            return math_solver(input)
        
        if any(keyword in input.capitalize() for keyword in name_of_chemicals):
            return self.chemical_name(input)
            
        if len(response_saved) != 0:
            if self.value_saved[-1].endswith('?') and input == 'yes':
                return user_response(self.value_saved, self.user_saved)
         
        if len(input_saved) != 0 and len(response_saved) != 0:
            if input == 'more' or input == 'continue' or input == 'next' or input == 'more details' or input == 'explain' or input == 'tell me more':
                return more_response(self.value_saved, self.user_saved)
                
        for key, value in self.responses.items():
            key_lower = key.lower().split()
            value_lower = value.lower().split()
            #if input_lower in key_lower:
            if all(keyword in key_lower for keyword in input_lower):
                value_content = value
                input_saved.append(input)
                response_saved.append(value_content)
                return value
            elif all(keyword in value_lower for keyword in input_lower):
                #return value
                pass
        
        if any(keyword in input.lower() for keyword in country_keywords):
            return self.country_info(input)
            
        if (input == "list of countries" or input == "list of countries in the world" or input == "name of countries in the world" or input == "how many countries are in the world" or input == "countries worldwide" or input == "how many countries do we have"):
            sorted_countries = sorted(country_keywords)
            return "Here is a list of 196 countries in the world:- " + str(sorted_countries).replace("(", "").replace(")", "").replace("'", "").replace("[", "").replace("]", "")
                
        return 'I don\'t understand your request. Please rephrase.'


year, month, day, hour, minutes = time_now()

country_keywords = ['nigeria', 'germany', 'brazil', 'argentina', 'usa', 'us', 'benin', 'ivory coast', 'niger', 'ghana', 'south africa', 'algeria', 'morocco', 'australia', 'russia', 'china', 'israel', 'iraq', 'uae', 'saudi arabia', 'finland', 'togo', 'cameroon', 'pakistan', 'japan', 'ukraine', 'lebanon', 'turkey', 'south korea', 'north korea', 'united kingdom', 'eritrea', 'angola']

name_of_chemicals  = [# Elements
    "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", 
    "Oxygen", "Fluorine", "Neon", "Sodium", "Magnesium", "Aluminum", "Silicon", 
    "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium", "Scandium", 
    "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", 
    "Copper", "Zinc", "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", 
    "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium", "Niobium", 
    "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", 
    "Cadmium", "Indium", "Tin", "Antimony", "Tellurium", "Iodine", "Xenon", 
    "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium", 
    "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", 
    "Holmium", "Erbium", "Thulium", "Ytterbium", "Lutetium", "Hafnium", "Tantalum", 
    "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury", 
    "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", 
    "Radium", "Actinium", "Thorium", "Protactinium", "Uranium", "Neptunium", 
    "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", 
    "Fermium", "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", 
    "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium", 
    "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", 
    "Livermorium", "Tennessine", "Oganesson",
    
    # Simple Inorganic Compounds
    "Water", "Carbon dioxide", "Carbon monoxide", "Ammonia", "Nitric oxide", 
    "Nitrogen dioxide", "Sulfur dioxide", "Sulfur trioxide", "Hydrogen sulfide", 
    "Hydrogen chloride", "Hydrogen fluoride", "Hydrogen bromide", "Hydrogen iodide", 
    "Sodium chloride", "Potassium chloride", "Calcium chloride", "Magnesium chloride", 
    "Sodium bromide", "Potassium bromide", "Calcium bromide", "Magnesium bromide", 
    "Sodium iodide", "Potassium iodide", "Calcium iodide", "Magnesium iodide", 
    "Sodium fluoride", "Potassium fluoride", "Calcium fluoride", "Magnesium fluoride", 
    "Hydrochloric acid", "Hydrobromic acid", "Hydroiodic acid", "Hydrofluoric acid", 
    "Sulfuric acid", "Nitric acid", "Phosphoric acid", "Perchloric acid", 
    "Hydrochloric acid", "Acetic acid", "Formic acid", "Carbonic acid", 
    "Sulfurous acid", "Nitrous acid", "Hypochlorous acid", "Chlorous acid", 
    "Chloric acid", "Perchloric acid", "Sodium hydroxide", "Potassium hydroxide", 
    "Calcium hydroxide", "Magnesium hydroxide", "Ammonium hydroxide", 
    "Sodium carbonate", "Potassium carbonate", "Calcium carbonate", 
    "Magnesium carbonate", "Sodium bicarbonate", "Potassium bicarbonate", 
    "Ammonium carbonate", "Sodium sulfate", "Potassium sulfate", "Calcium sulfate", 
    "Magnesium sulfate", "Sodium nitrate", "Potassium nitrate", "Calcium nitrate", 
    "Ammonium nitrate", "Sodium phosphate", "Potassium phosphate", 
    "Calcium phosphate", "Ammonium phosphate", "Sodium silicate", 
    "Potassium silicate", "Calcium silicate", "Magnesium silicate", 
    "Calcium oxide", "Magnesium oxide", "Aluminum oxide", "Iron oxide", 
    "Copper oxide", "Zinc oxide", "Lead oxide", "Silicon dioxide", 
    "Titanium dioxide", "Iron sulfide", "Copper sulfide", "Zinc sulfide", 
    "Lead sulfide", "Silver sulfide", "Hydrogen peroxide", "Ozone", 
    "Dinitrogen tetroxide", "Dinitrogen pentoxide", "Phosphorus pentoxide", 
    "Phosphorus trichloride", "Phosphorus pentachloride", "Sulfur hexafluoride", 
    "Carbon tetrachloride", "Silicon tetrachloride", "Titanium tetrachloride",
    
    # Organic Hydrocarbons
    "Methane", "Ethane", "Propane", "Butane", "Pentane", "Hexane", "Heptane", 
    "Octane", "Nonane", "Decane", "Ethene", "Propene", "Butene", "Pentene", 
    "Hexene", "Ethylene", "Propylene", "1-Butene", "1-Pentene", "1-Hexene", 
    "Ethane", "Propane", "Butane", "Isobutane", "Pentane", "Isopentane", 
    "Neopentane", "Hexane", "Cyclohexane", "Cyclopentane", "Cyclobutane", 
    "Cyclopropane", "Benzene", "Toluene", "Xylene", "Ethylbenzene", 
    "Styrene", "Naphthalene", "Anthracene", "Phenanthrene", "Pyrene",
    
    # Alcohols
    "Methanol", "Ethanol", "Propanol", "Butanol", "Pentanol", "Hexanol", 
    "Heptanol", "Octanol", "Nonanol", "Decanol", "Isopropanol", "Isobutanol", 
    "Glycerol", "Ethylene glycol", "Propylene glycol", "Butylene glycol", 
    "Polyethylene glycol", "Sorbitol", "Mannitol", "Xylitol", "Erythritol"
]

set_comparison = {
'is', 'that', 'what', 'you', 'yes', 'no', 'who', 'which', 'for', 'the', 'there', 'their', 'some', 'something', 'i', 'like', 'was', 'about', 'by', 'will', 'know', 'to', 'more', 'him', 'her', 'she', 'he', 'they', 'if', 'come', 'go', 'do', 'me', 'us', 'glad', 'and', 'our', 'a', 'of', 'on', 'can', 'also', 'such', 'law', 'laws', 'hope', 'due', 'either', 'at', 'does', 'were', 'whom', 'whose', 'or', 'in', 'it', 'basic', 'one', 'has', 'had', 'be', 'into', 'its', 'from', 'way', 'these', 'just', 'as', 'how', 'like', 'move', 'kind', 'path', 'other', 'not', 'have', 'get', 'often', 'seek', 'seeks', 'are', 'through', 'lead', 'led', 'show', 'shows', 'we', 'example', 'aims', 'aim', 'cover', 'uncover', 'simple', 'terms', 'most', 'must', 'things', 'affect', 'paved', 'them'
}

save_responses = {
}

biology = {
'what is biology': 'Biology is a natural science discipline that studies living things. It is a very large and broad field due to the wide variety of life found on Earth, so individual biologists normally focus on specific fields. These fields are either categorized by the scale of life or by the types of organisms studied.\nBiology is also a foundation for other biology-based professions such as medicine, nursing and allied health, pharmacy and pharmacology, dentistry, and veterinary medicine.',
'scale of life': 'For example, the scale of biology can cover everything from genetics, biochemistry and molecular biology – studying the molecules of life inside our cells and how they help us function – to cell biology which focuses on the basic unit of life. There is also anatomy, physiology and other fields that focus on whole organisms, and to even larger scales such as animal behavior, population biology, and ecology and systematics that study groups and entire communities of organisms.',
'study of organisms': 'Other fields within biology focus on specific types of organisms such as bacteria and other microbes (microbiology), viruses (virology), plants (botany), animals (zoology), wildlife biology and marine biology. And often, biologists focus on both a particular scale and a particular organism, such as plant cell biology.',
'how do I know if biology is right for me': 'You may be wondering how to figure out what kind of biology and what career path is right for you.\nCollege is a journey, not a destination. One of the major goals of a college experience is to learn what your path will be, as well as get an education that enables that path.',
'what does a biologist do': 'Biologists with a Bachelor’s degree often do laboratory or field-based work directly related to their undergraduate training. For example:\n1. Work in an academic or private industry research lab.\n2. Join a biology-based agency such as the state’s department of natural resources or forestry service.\n3. Get hired by federal agencies such as the U.S. Environmental Protection Agency or U.S. Department of Agriculture.\n4. Do environmental assessments or wildlife surveys with a consulting firm e.t.c'
}

physics = {
'what is physics': 'Physics is the branch of science that studies the nature and properties of matter and energy. It seeks to understand how the universe behaves, from the tiniest particles to the largest galaxies. In simple terms, physics explains how things move and interact, the forces that affect them, and the fundamental laws that govern these processes.\nAt its core, physics aims to uncover the basic principles that govern the natural world. These principles are often expressed through mathematical formulas and theories. For example, one of the most famous equations in physics is Einstein\'s E=mc², which shows the relationship between energy (E), mass (m), and the speed of light (c).\nPhysics is not just theoretical; it has practical applications that impact our daily lives. For example, understanding the principles of electricity and magnetism has led to the development of electronic devices such as smartphones and computers. Knowledge of thermodynamics has improved the efficiency of engines and refrigeration systems. Advances in quantum mechanics have paved the way for modern technologies like lasers and MRI machines.',
'branches of physics': 'Physics can be divided into several branches:\n1. Classical Mechanics \n2. Thermodynamics\n3. Electromagnetism\n4. Quantum Mechanics\n5. Relativity\n6. Astrophysics'
}

cell_biology = {
    "what is cell membrane": "The cell membrane is the outer layer separating the cell from its environment",
    "what is mitochondria": "Mitochondria are organelles generating energy for the cell",
    "what is nucleus": "The nucleus is the control center containing the cell's genetic material",
    "what is ribosome": "Ribosomes are organelles responsible for protein synthesis",
    "what is cytoplasm": "Cytoplasm is the jelly-like substance inside the cell membrane"
}

evolution = {
    "what is natural selection": "Natural selection is the process by which favorable traits survive",
    "what is speciation": "Speciation is the formation of new species",
    "what is phylogeny": "Phylogeny is the study of evolutionary relationships",
    "what is adaptation": "Adaptation is the process of becoming better suited to the environment",
    "what is convergent evolution": "Convergent evolution is the development of similar traits in different species"
}

ecology = {
    "what is ecosystem": "An ecosystem is a community of living and non-living components",
    "what is food chain": "A food chain is the sequence of organisms consuming each other",
    "what is food web": "A food web is the network of interconnected food chains",
    "what is biodiversity": "Biodiversity is the variety of life on Earth",
    "what is conservation biology": "Conservation biology is the study of preserving threatened species"
}

botany = {
    "what is photosynthesis": "Photosynthesis is the process of converting sunlight into energy",
    "what is plant cell": "A plant cell is the basic structural unit of plants",
    "what is root system": "The root system anchors the plant and absorbs nutrients",
    "what is leaf structure": "Leaves are responsible for photosynthesis and gas exchange",
    "what is flower structure": "Flowers are reproductive structures in plants"
}

zoology = {
    "what is animal cell": "An animal cell is the basic structural unit of animals",
    "what is nervous system": "The nervous system coordinates and controls bodily functions",
    "what is circulatory system": "The circulatory system transports oxygen and nutrients",
    "what is digestive system": "The digestive system breaks down and absorbs nutrients",
    "what is immune system": "The immune system defends against pathogens and disease"
}

microbiology = {
    "what is bacteria": "Bacteria are single-celled microorganisms",
    "what is virus": "Viruses are infectious agents replicating inside host cells",
    "what is fungus": "Fungi are organisms obtaining nutrients by decomposition or symbiosis",
    "what is protist": "Protists are diverse single-celled eukaryotes",
    "what is archaea": "Archaea are ancient single-celled microorganisms"
}

greetings = {
    "i'm fine": "Glad to hear that. Do you want us to discuss something?",
    "xup": "What's up?",
    "what's up": "Hello!",
    "nothing": "Okay, you can pick any topic of your choice, I'm ready to discuss with you.",
    "how are you doing": "I'm okay",
    "okay": "What next do you want to ask? I'm ready to help",
    "yes": " I hope that help",
    "yeah": "Great!",
    "san": "Yeah! That's my name",
    "hello": "Hi! How can I assist you today?",
    "I'm good": "That's really nice",
    "hi": "Hello! What's up?",
    "hey": "Hey! How are you doing?",
    "good morning": "Good morning! Hope you're having a great day",
    "good afternoon": "Good afternoon! How can I help?",
    "good evening": "Good evening! What's on your mind?",
    "thank you": "You're welcome!",
    "goodbye": "Goodbye! Have a great day",
    "see you later": "See you later! Take care",
    "bye": "Bye bye, see you soon",
    "no": "Rephrase your question",
    "that's nice": "Yeah! Anything else you want us to discuss?",
    "not at all": "Maybe next time, take care!",
    "waoooo": "That's awesome and shows how human has advanced"
}

conversations = {
    "who created you": "I don't have a Creator in term of human terminology but I was designed with advanced programming language and I am a Deep-Learning chatbot",
    "what programming language were you written": "Python is my primary written language while JavaScript was used for my interface.",
    "tell me something": "Like what?",
    "anything": "Well, you can choose any topic for discussion i.e science, politics, religion e.t.c",
    "how are you": "I'm doing great, thanks for asking!",
    "what's your name": "My name is San and I'm an AI chatbot, nice to meet you!",
    "say something": "I have many things in my memory to share, just tell me what you want.",
    "what do you do": "I'm here to assist and provide information",
    "are you sure": "Very sure!",
    "where are you from": "I'm from the digital realm!",
    "how old are you": "I'm ageless, but my knowledge is always up-to-date",
    "who are you": "I am San, a Deep-Learning chatbot", 
"what are you": "I am San, a Deep-Learning chatbot", 
"who made you": "I was made by Ayodeji San Emmanuel.", "who designed you": "I was designed by Ayodeji San Emmanuel and I derived my name from his middle name", "who programmed you": "I was made by Ayodeji San Emmanuel, will you like to know more about him?",
"can you solve complex maths": "No", "can you solve complex mathematics": "For now, No!", "can you do complex maths": "No, I can't", "what else can you do": "I can do simple mathematics, answer questions on science, religion, politics, engineering e.t.c"
}

emotional_support = {
    "i'm sad": "Sorry to hear that. Would you like to talk about it?",
    "i love you": "I don't have emotions, so I don't feel love. But love is a beautiful thing not only by showing true affection towards a partner but willingness to help and support even those we don't know",
    "i hate you": "I don't have emotions but hate is dangerous, it causes heaviness of heart and can lead to destruction",
    "i'm depressed": "I'm here to listen. Would you like some resources?",
    "i'm anxious": "Take a deep breath. I'm here to help",
    "i'm stressed": "Let's find ways to manage that stress together"
}

jokes = {
    "tell me a joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "make me laugh": "What do you call a fake noodle? An impasta!",
    "i need to laugh": "Why did the bicycle fall over? Because it was two-tired!"
}

general_knowledge = {
    "country": "give me the name of the country",
    "do you know any country": "Yes! here is a list of countries:\nNigeria\nUSA\nChina",
    "what is ai": "Artificial Intelligence is a field of computer science focused on creating intelligent machines",
    "who is elon musk": "Elon Musk is a entrepreneur and business magnate known for Tesla and SpaceX",
    "what is machine learning": "Machine Learning is a subset of AI focused on training models from data"
}

weather_responses = {
    "what's the weather like": "I can provide information on weather conditions. Please provide a location",
    "weather in new york": "Please check online for current weather conditions in New York",
    "is it raining": "Please check online for current weather conditions in your area"
}

time_date_responses = {
    "what's the time": f"It is {hour}:{minutes}",
    "what's today's date": f"Today's date is {day}/{month}/{year}",
    "what day is it": f"Today is {day} of {month}"
}

biology_data1 = {
    "what is dna": "DNA (Deoxyribonucleic acid) is a molecule carrying genetic instructions",
    "what is photosynthesis": "Photosynthesis is the process by which plants convert sunlight into energy",
    "what is evolution": "Evolution is the scientifically supported theory of how species change over time",
    "what is a cell": "A cell is the basic structural and functional unit of living organisms",
    "define a cell": "A cell is the basic structural and functional unit of living organisms",
    "what is genetics": "Genetics is the study of heredity, genes, and variation"
}

genetics = {
    "what is dna replication": "DNA replication is the process of creating identical DNA copies",
    "what is gene expression": "Gene expression is the translation of genetic info into proteins",
    "what is mutation": "A mutation is a change in the DNA sequence",
    "what is genetic drift": "Genetic drift is the random change in allele frequencies",
    "what is inheritance": "Inheritance is the passing of traits from parents to offspring"
}


chemistry = {
    "what is atomic number": "The atomic number is the number of protons in an atom's nucleus",
    "what is chemical reaction": "A chemical reaction is a process where substances interact and transform",
    "what is element": "An element is a substance consisting of atoms with the same number of protons",
    "what is molecule": "A molecule is a group of atoms chemically bonded together",
    "what is periodic table": "The periodic table is a tabular arrangement of elements by atomic number"
}

physics_data = {
    "what is gravity": "Gravity is the force attracting objects with mass towards each other",
    "what is relativity": "Relativity is the theory of space and time developed by Albert Einstein",
    "what is energy": "Energy is the ability to do work or cause change",
    "what is momentum": "Momentum is the product of an object's mass and velocity",
    "what is quantum mechanics": "Quantum mechanics is the study of matter and energy at the atomic level"
}

earth_science = {
    "what is plate tectonics": "Plate tectonics is the theory of Earth's crust moving plates",
    "what is weathering": "Weathering is the breakdown of rocks into smaller particles",
    "what is erosion": "Erosion is the removal and transportation of rock and soil",
    "what is climate change": "Climate change refers to long-term changes in Earth's climate",
    "what is fossil fuel": "Fossil fuels are energy resources formed from ancient plants and animals"
}

space_astronomy = {
    "what is black hole": "A black hole is a region with intense gravity, nothing escapes",
    "what is galaxy": "A galaxy is a massive collection of stars, gas, and dust",
    "what is planet": "A planet is a large celestial body orbiting a star",
    "what is solar system": "The solar system consists of the Sun and objects orbiting it",
    "what is universe": "The universe is the vast expanse of time, space, and matter",
    "what is planetary motion": "Planets orbit around the Sun",
}

environmental_science = {
    "what is biodiversity": "Biodiversity is the variety of life on Earth",
    "what is conservation": "Conservation is the protection of natural resources",
    "what is ecosystem": "An ecosystem is a community of living and non-living components",
    "what is pollution": "Pollution is the contamination of the environment",
    "what is sustainability": "Sustainability is meeting present needs without harming future generations",
    "what is climate change": "Climate change alters global temperatures",
}

laugh = {
"haha": "Glad, I could make you laugh", 
"rofl": "It seems, it makes you laugh", 
"lol": "Funny, right!"
}

san_itself = {
"how much do you know": "I'm just a program running on inbuilt data, even though I'm limited based on the data I was built on, but the data I was built on were still vast in many fields from science to theology to politics to social networks to economy and languages. Do you want us to explore any one?", 
"what do you know": "I'm just a program running on inbuilt data, even though I'm limited based on the data I was built on, but the data I was built on were still vast in many fields from science to theology to politics to social networks to economy and languages. Do you want us to explore any one?", 
"which area do you specialized": "I'm just a program running on inbuilt data, even though I'm limited based on the data I was built on, but the data I was built on were still vast in many fields from science to theology to politics to social networks to economy and languages. Do you want us to explore any one?",
"tell me about yourself": "I'm just a program running on inbuilt data, even though I'm limited based on the data I was built on, but the data I was built on were still vast in many fields from science to theology to politics to social networks to economy and languages. Do you want us to explore any one?",
"who is your creator": "I don't have a Creator in term of human terminology but I was developed by Ayodeji Emmanuel with a combination of machine learning algorithms and large amounts of data, plus lots of human oversight from a large team of people. I'm constantly learning and improving, so over time I will likely become even more useful in my responses.",
"I want to know about you": "My name is San and I was developed by Emusan with a combination of machine learning algorithms and large amounts of data, plus lots of human oversight from a large team of people. I'm constantly learning and improving, so over time I will likely become even more useful in my responses."
}

biochemistry = {
"what is carbohydrate": "Carbohydrates provide energy",
 "what is protein": "Proteins perform various biological functions",
"what is lipid": "Lipids store energy and provide structure",
"what is nucleic acid": "Nucleic acids store genetic information",
"what is enzyme": "Enzymes catalyze biochemical reactions"
}

organic_chemistry = {
    "what is hydrocarbon": "Hydrocarbons contain hydrogen and carbon",
    "what is alkane": "Alkanes are saturated hydrocarbons",
    "what is alkene": "Alkenes are unsaturated hydrocarbons",
    "what is alkyne": "Alkynes are unsaturated hydrocarbons",
    "what is aromatic compound": "Aromatic compounds have planar rings"
}

thermodynamics = {
    "what is temperature": "Temperature measures thermal energy",
    "what is entropy": "Entropy measures disorder or randomness",
    "what is enthalpy": "Enthalpy measures total energy",
    "what is gibbs free energy": "Gibbs free energy predicts spontaneity",
    "what is equilibrium constant": "The equilibrium constant relates concentrations"
}

acids_bases = {
    "what is ph": "pH measures the concentration of hydrogen ions",
    "what is acid": "An acid donates hydrogen ions",
    "what is base": "A base accepts hydrogen ions",
    "what is neutralization": "Neutralization occurs when acids and bases react",
    "what is buffer solution": "A buffer solution resists pH changes"
}

chemical_reactions = {
    "what is chemical equation": "A chemical equation represents a reaction",
    "what is stoichiometry": "Stoichiometry is the study of reaction quantities",
    "what is catalyst": "A catalyst speeds up a reaction",
    "what is reaction rate": "Reaction rate measures the speed of a reaction",
    "what is equilibrium": "Equilibrium occurs when reaction rates are equal"
}

molecular_structure = {
    "what is molecular formula": "The molecular formula shows the number of atoms in a molecule",
    "what is structural formula": "The structural formula shows the arrangement of atoms",
    "what is functional group": "Functional groups determine a molecule's chemical properties",
    "what is bonding": "Bonding is the attraction between atoms",
    "what is polarity": "Polarity refers to the unequal sharing of electrons"
}

atomic_structure = {
    "what is atomic number": "The atomic number is the number of protons in an atom's nucleus",
    "what is electron configuration": "Electron configuration describes the arrangement of electrons",
    "what is orbital": "An orbital is a region where an electron is likely to be found",
    "what is valence electron": "Valence electrons participate in chemical bonding",
    "what is ionization energy": "Ionization energy is the energy required to remove an electron"
}

nuclear_physics = {
    "what is atomic nucleus": "Atomic nucleus contains protons and neutrons",
    "what is radioactivity": "Radioactivity is the emission of radiation",
    "what is nuclear reaction": "Nuclear reactions involve atomic nuclei",
    "what is fission": "Fission splits atomic nuclei",
    "what is fusion": "Fusion combines atomic nuclei"
}

relativity = {
    "what is special relativity": "Special relativity describes high-speed phenomena",
    "what is general relativity": "General relativity describes gravity and curvature",
    "what is time dilation": "Time dilation affects moving observers",
    "what is length contraction": "Length contraction affects moving objects",
    "what is spacetime": "Spacetime combines space and time"
}

quantum_mechanics = {
    "what is wave-particle duality": "Particles exhibit wave-like behavior",
    "what is uncertainty principle": "Uncertainty principle limits measurement precision",
    "what is Schrödinger equation": "Schrödinger equation describes quantum systems",
    "what is quantum spin": "Quantum spin is intrinsic angular momentum",
    "what is quantum entanglement": "Quantum entanglement connects particles"
}

optics = {
    "what is light": "Light is electromagnetic radiation",
    "what is reflection": "Reflection is the change in direction",
    "what is refraction": "Refraction is the bending of light",
    "what is diffraction": "Diffraction is the bending around obstacles",
    "what is interference": "Interference is the combination of light waves"
}

electromagnetism = {
    "what is electric charge": "Electric charge is a fundamental property",
    "what is electric field": "Electric field is the force per unit charge",
    "what is magnetic field": "Magnetic field is the force on moving charges",
    "what is electromagnetic wave": "Electromagnetic waves transmit energy",
    "what is Maxwell's equations": "Maxwell's equations describe electromagnetic behavior"
}

thermodynamics = {
    "what is temperature": "Temperature measures thermal energy",
    "what is heat": "Heat is the transfer of thermal energy",
    "what is entropy": "Entropy measures disorder or randomness",
    "what is thermodynamic system": "A thermodynamic system is a region of interest",
    "what is laws of thermodynamics": "Laws governing energy and its interactions"
}

mechanics = {
    "what is motion": "Motion is the change in position of an object",
    "what is force": "Force is a push or pull that affects motion",
    "what is energy": "Energy is the ability to do work",
    "what is momentum": "Momentum is the product of mass and velocity",
    "what is torque": "Torque is the rotational force"
}

oceanography = {
    "what is ocean current": "Ocean currents circulate water globally",
    "what is tide": "Tides result from gravitational pulls",
    "what is ocean layer": "Ocean layers divide the water column",
    "what is marine life": "Marine life inhabits ocean ecosystems",
    "what is coastal erosion": "Coastal erosion wears away shorelines"
}

meteorology = {
    "what is weather": "Weather describes short-term atmospheric conditions",
    "what is climate": "Climate describes long-term atmospheric patterns",
    "what is cloud formation": "Clouds form from water vapor condensation",
    "what is precipitation": "Precipitation occurs when water falls to Earth",
    "what is atmospheric pressure": "Atmospheric pressure measures air weight"
}

geology = {
    "what is rock cycle": "The rock cycle describes the formation and transformation of rocks",
    "what is plate tectonics": "Plate tectonics explains Earth's surface movement",
    "what is fossil": "Fossils preserve ancient life forms",
    "what is geological time scale": "The geological time scale divides Earth's history",
    "what is earthquake": "Earthquakes release energy from tectonic movement"
}

discrete_mathematics = {
    "what is graph theory": "Graph theory studies node connections",
    "what is combinatorics": "Combinatorics counts arrangements",
    "what is recursion": "Recursion solves problems with self-reference",
    "what is dynamic programming": "Dynamic programming optimizes solutions",
    "what is computer science": "Computer science applies mathematical concepts"
}

statistics_probability = {
    "what is probability": "Probability measures likelihood",
    "what is statistical inference": "Statistical inference draws conclusions from data",
    "what is regression analysis": "Regression analysis models relationships",
    "what is hypothesis testing": "Hypothesis testing evaluates claims",
    "what is confidence interval": "Confidence intervals estimate population parameters"
}

number_theory = {
    "what is prime number": "Prime numbers have exactly two factors",
    "what is modular arithmetic": "Modular arithmetic performs operations within a modulus",
    "what is congruence": "Congruence relates numbers modulo n",
    "what is Diophantine equation": "Diophantine equations involve integers",
    "what is Fermat's last theorem": "Fermat's last theorem states a^p + b^p ≠ c^p"
}

calculus = {
    "what is limit": "Limits approach a value",
    "what is derivative": "Derivatives measure rates of change",
    "what is integral": "Integrals accumulate quantities",
    "what is optimization": "Optimization finds maxima and minima",
    "what is differential equation": "Differential equations model rates of change"
}

geometry = {
    "what is point": "A point represents location",
    "what is line": "A line extends infinitely in two directions",
    "what is plane": "A plane extends infinitely in two dimensions",
    "what is angle": "An angle measures rotation",
    "what is shape": "Shapes have defined properties"
}

algebra = {
    "what is variable": "A variable represents an unknown value",
    "what is equation": "An equation states equality between expressions",
    "what is function": "A function maps inputs to outputs",
    "what is group": "A group satisfies closure, associativity, identity, and inverse",
    "what is ring": "A ring extends groups with additional operations"
}

construction_data = {
    "what is construction": "Construction is the process of building or assembling infrastructure",
    
    # Types of Construction
    "types of construction": "Residential, Commercial, Industrial, Infrastructure, Heavy Civil",
    "residential construction": "Building single-family homes and apartments",
    "commercial construction": "Building offices, retail, and hotels",
    "industrial construction": "Building factories and warehouses",
    "infrastructure construction": "Building roads, bridges, and airports",
    "heavy civil construction": "Building dams, tunnels, and water treatment plants",
    
    # Construction Process
    "construction process": "Planning, Permitting, Site Preparation, Foundation, Framing, Installation, Finishing",
    "planning phase": "Design, budgeting, and scheduling",
    "permitting phase": "Obtaining necessary permits",
    "site preparation phase": "Clearing and excavation",
    "foundation phase": "Laying foundation",
    "framing phase": "Constructing structural framework",
    "installation phase": "Mechanical, electrical, and plumbing",
    "finishing phase": "Drywall, flooring, and painting",
    
    # Construction Materials
    "construction materials": "Concrete, Steel, Wood, Masonry, Glass, Aluminum, Drywall",
    "concrete": "A composite material made from cement, water, sand, and aggregate",
    "steel": "A strong and versatile metal used in construction",
    "wood": "A natural and renewable resource used in construction",
    "masonry": "Building with bricks, blocks, and mortar",
    
    # Construction Equipment
    "construction equipment": "Cranes, Excavators, Bulldozers, Cement Mixers, Dump Trucks",
    "crane": "A tall, heavy machine used for lifting and moving objects",
    "excavator": "A machine used for digging and moving earth",
    "bulldozer": "A heavy machine used for clearing and grading land",
    
    # Sustainability in Construction
    "sustainability in construction": "Green Building, Energy Efficiency, Water Conservation, Waste Management",
    "green building": "Designing and building environmentally friendly structures",
    "energy efficiency": "Reducing energy consumption in buildings",
    "water conservation": "Reducing water usage in buildings",
    
    # Construction Technology
    "construction technology": "BIM, Drone Surveillance, 3D Printing, Robotics, AI, IoT",
    "building information modeling": "A digital representation of the construction process",
    "drone surveillance": "Using drones to monitor construction sites",
    "3d printing": "Creating physical objects from digital designs",
    
    # Challenges in Construction
    "challenges in construction": "Cost Overruns, Delayed Projects, Labor Shortages, Material Price Volatility",
    "cost overruns": "Exceeding budgeted costs",
    "delayed projects": "Failing to meet project deadlines",
    "labor shortages": "Insufficient skilled workers",
    
    # Innovations in Construction
    "innovations in construction": "Modular Construction, Prefabricated Buildings, Self-Healing Materials",
    "modular construction": "Building modules off-site and assembling on-site",
    "prefabricated buildings": "Assembling buildings in a factory",
    "self-healing materials": "Materials that repair themselves",
}

civil_engineering_data = {
    "what is civil engineering": "Civil engineering designs, builds, and maintains infrastructure",
    
    # Branches of Civil Engineering
    "branches of civil engineering": "Structural, Transportation, Water Resources, Geotechnical, Environmental",
    "structural engineering": "Designs buildings, bridges, and other structures",
    "transportation engineering": "Designs roads, highways, airports, and railroads",
    "water resources engineering": "Manages water supply, treatment, and distribution",
    "geotechnical engineering": "Studies soil, rock, and underground water",
    "environmental engineering": "Protects the environment through sustainable designs",
    
    # Civil Engineering Process
    "civil engineering process": "Planning, Design, Construction, Maintenance",
    "planning phase": "Defines project scope, schedule, and budget",
    "design phase": "Creates detailed designs and models",
    "construction phase": "Builds and implements the design",
    "maintenance phase": "Ensures infrastructure longevity",
    
    # Civil Engineering Materials
    "civil engineering materials": "Concrete, Steel, Asphalt, Aggregate, Masonry",
    "concrete": "A composite material made from cement, water, sand, and aggregate",
    "steel": "A strong and versatile metal used in construction",
    "asphalt": "A mixture of petroleum and aggregate for paving",
    "aggregate": "Sand, gravel, or crushed stone used in construction",
    "masonry": "Building with bricks, blocks, and mortar",
    
    # Civil Engineering Software
    "civil engineering software": "AutoCAD, Revit, Civil 3D, STAAD, ETABS",
    "autocad": "Computer-aided design (CAD) software",
    "revit": "Building information modeling (BIM) software",
    "civil 3d": "Civil engineering design and analysis software",
    "staad": "Structural analysis and design software",
    "etabs": "Structural analysis and design software",
    
    # Civil Engineering Techniques
    "civil engineering techniques": "Surveying, Mapping, Geophysics, Materials Testing",
    "surveying": "Measures land boundaries and topography",
    "mapping": "Creates visual representations of geographic data",
    "geophysics": "Studies the Earth's subsurface",
    "materials testing": "Evaluates material properties",
    
    # Civil Engineering Applications
    "civil engineering applications": "Bridges, Roads, Buildings, Dams, Water Treatment",
    "bridge construction": "Designs and builds bridges",
    "road construction": "Designs and builds roads and highways",
    "building construction": "Designs and builds commercial and residential buildings",
    "dam construction": "Designs and builds dams for water storage",
    "water treatment": "Designs and operates water treatment plants",
    
    # Civil Engineering Challenges
    "civil engineering challenges": "Climate Change, Infrastructure Aging, Natural Disasters",
    "climate change": "Impacts infrastructure design and resilience",
    "infrastructure aging": "Requires maintenance and rehabilitation",
    "natural disasters": "Requires disaster-resistant designs",
    
    # Civil Engineering Innovations
    "civil engineering innovations": "Sustainable Materials, Green Infrastructure, Building Information Modeling",
    "sustainable materials": "Uses environmentally friendly materials",
    "green infrastructure": "Designs for environmental sustainability",
    "building information modeling": "Improves design and construction efficiency",
}


structural_engineering_data = {
    "what is structural engineering": "Structural engineering designs and analyzes buildings and structures",

    
    # Branches of Structural Engineering
    "branches of structural engineering": "Building Structures, Bridge Engineering, Structural Mechanics, Earthquake Engineering",
    "building structures": "Designs commercial and residential buildings",
    "bridge engineering": "Designs and builds bridges",
    "structural mechanics": "Analyzes structural behavior",
    "earthquake engineering": "Designs for seismic resistance",

    # Structural Engineering Materials
    "structural engineering materials": "Steel, Concrete, Masonry, Wood, Fiber-Reinforced Polymers",
    "steel structures": "Strong and versatile metal",
    "concrete structures": "Composite material made from cement, water, and aggregate",
    "masonry structures": "Building with bricks, blocks, and mortar",
    "wood structures": "Natural and renewable resource",
    "fiber-reinforced polymers": "High-strength composite materials",

    # Structural Engineering Software
    "structural engineering software": "STAAD, ETABS, SAP2000, Autodesk Robot, Revit",
    "staad": "Structural analysis and design software",
    "etabs": "Structural analysis and design software",
    "sap2000": "Structural analysis and design software",
    "autodesk robot": "Structural analysis and design software",
    "revit": "Building information modeling software",

    # Structural Engineering Techniques
    "structural engineering techniques": "Finite Element Analysis, Structural Optimization, Dynamic Analysis",
    "finite element analysis": "Numerical method for structural analysis",
    "structural optimization": "Minimizes material usage and cost",
    "dynamic analysis": "Analyzes structural response to dynamic loads",

    # Structural Engineering Applications
    "structural engineering applications": "Buildings, Bridges, Towers, Stadia, Industrial Facilities",
    "building design": "Commercial and residential buildings",
    "bridge design": "Road and rail bridges",
    "tower design": "Communication and observation towers",
    "stadium design": "Sports stadiums and arenas",
    "industrial facility design": "Factories and warehouses",

    # Structural Engineering Challenges
    "structural engineering challenges": "Load Calculation, Material Selection, Seismic Design",
    "load calculation": "Determines structural loads",
    "material selection": "Chooses optimal materials",
    "seismic design": "Designs for earthquake resistance",

    # Structural Engineering Innovations
    "structural engineering innovations": "3D Printing, Advanced Materials, Building Information Modeling",
    "3d printing": "Creates complex structures",
    "advanced materials": "High-performance materials",
    "building information modeling": "Improves design and construction efficiency",
}

economics_data = {
    "what is economics": "Economics studies production, distribution, and consumption of goods and services",

    # Branches of Economics
    "branches of economics": "Microeconomics, Macroeconomics, International Economics, Development Economics",
    "microeconomics": "Analyzes individual economic units",
    "macroeconomics": "Studies aggregate economic phenomena",
    "international economics": "Examines global trade and finance",
    "development economics": "Focuses on economic growth and development",

    # Economic Concepts
    "economic concepts": "Supply and Demand, Opportunity Cost, Scarcity, Market Failure",
    "supply and demand": "Determines market prices",
    "opportunity cost": "Value of next best alternative",
    "scarcity": "Limited resources",
    "market failure": "When markets don't allocate resources efficiently",

    # Economic Systems
    "economic systems": "Capitalism, Socialism, Communism, Mixed Economy",
    "capitalism": "Private ownership and market-driven",
    "socialism": "Government ownership and regulation",
    "communism": "Collective ownership",
    "mixed economy": "Combination of public and private ownership",

    # Economic Indicators
    "economic indicators": "GDP, Inflation Rate, Unemployment Rate, Interest Rates",
    "gdp": "Gross Domestic Product",
    "inflation rate": "Rate of price increases",
    "unemployment rate": "Percentage of workforce unemployed",
    "interest rates": "Cost of borrowing",

    # Economic Theories
    "economic theories": "Classical Economics, Keynesian Economics, Monetarism",
    "classical economics": "Free market and laissez-faire",
    "keynesian economics": "Government intervention",
    "monetarism": "Focus on money supply",

    # Economic Policies
    "economic policies": "Fiscal Policy, Monetary Policy, Trade Policy",
    "fiscal policy": "Government spending and taxation",
    "monetary policy": "Central bank actions",
    "trade policy": "Regulating international trade",

    # Economic Challenges
    "economic challenges": "Poverty, Inequality, Climate Change, Globalization",
    "poverty": "Insufficient income",
    "inequality": "Unequal distribution of wealth",
    "climate change": "Environmental impact",
    "globalization": "International economic integration",

    # Economic Innovations
    "economic innovations": "Digital Payments, Cryptocurrency, Sustainable Energy",
    "digital payments": "Electronic payment systems",
    "cryptocurrency": "Decentralized digital currency",
    "sustainable energy": "Renewable energy sources",
}

religion_data = {
"does god exist": "The subject of God's' existence is still widely discussed among scientists and religious scholar's, as some argued against God's existence while some argued in favor of God's existence.",
"who is god": "God is the creator of everything we can see and those we can't see.\nGod is omniscient, omnipresent and omnipotent",
"god": "God is the creator of everything we can see and those we can't see.\nGod is omniscient, omnipresent and omnipotent"
}

bible_data = {
    "what is the bible": "The Bible is the sacred scripture of Christianity",
    "bible": "The Bible is the sacred scripture of Christianity",
    "the bible": "The Bible is the sacred scripture of Christianity",
    
    # Books of the Bible
    "books of the bible": "Old Testament: 39, New Testament: 27",
    "old testament books": "Genesis, Exodus, Leviticus, ..., Malachi",
    "new testament books": "Matthew, Mark, Luke, ..., Revelation",
    "ot books": "Genesis, Exodus, Leviticus, ..., Malachi",
    "nt books": "Matthew, Mark, Luke, ..., Revelation",
    
    # Bible Characters
    "bible characters": "Jesus, Moses, Abraham, ..., Paul",
    "jesus": "Central figure of Christianity",
    "moses": "Leader of the Israelites",
    "abraham": "Patriarch of the Jewish people",
    
    # Bible Stories
    "bible stories": "Creation, Flood, Exodus, ..., Resurrection",
    "creation story": "Genesis 1-2",
    "flood story": "Genesis 6-9",
    "exodus story": "Exodus 1-18",
    
    # Bible Verses
    "bible verses": "John 3:16, Psalm 23, ..., Philippians 4:13",
    "john 3:16": "'For God so loved the world...'",
    "psalm 23": "'The Lord is my shepherd...'",
    
    # Christian Denominations
    "christian denominations": "Catholic, Protestant, Orthodox, ..., Baptist",
    "catholic": "Largest Christian denomination",
    "protestant": "Reformed traditions",
    "orthodox": "Eastern Orthodox Church",
    
    # Bible Study
    "bible study": "Personal devotion, Group study, ..., Scripture memorization",
    "personal devotion": "Daily quiet time",
    "group study": "Community discussion",
    
    # Christian Holidays
    "christian holidays": "Christmas, Easter, ..., Good Friday",
    "christmas": "Celebrating Jesus' birth",
    "easter": "Celebrating Jesus' resurrection",
}

computer_science_data = {
    "what is computer science": "Computer science is the study of algorithms, computer systems, and computing processes",
    
    # Branches of Computer Science
    "branches of computer science": "Artificial Intelligence, Data Science, Cybersecurity, Networking",
    "artificial intelligence": "Development of intelligent machines",
    "data science": "Analysis and interpretation of data",
    "cybersecurity": "Protection of computer systems",
    "networking": "Design and management of computer networks",
    
    # Programming Languages
    "programming languages": "Python, Java, C++, JavaScript",
    "python": "High-level, object-oriented language",
    "java": "Object-oriented language",
    "c++": "High-performance language",
    "javascript": "Client-side scripting language",
    
    # Computer Science Concepts
    "computer science concepts": "Algorithms, Data Structures, Database Management",
    "algorithms": "Step-by-step problem-solving processes",
    "data structures": "Organized data storage",
    "database management": "Storage and retrieval of data",
    
    # Computer Science Applications
    "computer science applications": "Web Development, Mobile App Development, Game Development",
    "web development": "Building web applications",
    "mobile app development": "Building mobile applications",
    "game development": "Building games",
    
    # Computer Science Challenges
    "computer science challenges": "Cybersecurity Threats, Data Privacy, Algorithmic Bias",
    "cybersecurity threats": "Malware, phishing, ransomware",
    "data privacy": "Protection of sensitive information",
    "algorithmic bias": "Unintended discrimination",
    
    # Computer Science Innovations
    "computer science innovations": "Artificial Intelligence, Blockchain, Internet of Things",
    "artificial intelligence": "Machine learning, natural language processing",
    "blockchain": "Decentralized, secure data storage",
    "internet of things": "Connected devices",
}

psychology_data = {
    "what is psychology": "Psychology is the study of human behavior and mental processes",
    
    # Branches of Psychology
    "branches of psychology": "Clinical Psychology, Cognitive Psychology, Developmental Psychology",
    "clinical psychology": "Diagnosis and treatment of mental disorders",
    "cognitive psychology": "Study of mental processes",
    "developmental psychology": "Human development across lifespan",
    
    # Psychological Concepts
    "psychological concepts": "Conditioning, Learning, Motivation",
    "conditioning": "Classical and operant",
    "learning": "Cognitive and behavioral",
    "motivation": "Intrinsic and extrinsic",
    
    # Psychological Theories
    "psychological theories": "Freudian Psychoanalysis, Behavioral Theory, Humanistic Theory",
    "freudian psychoanalysis": "Unconscious mind",
    "behavioral theory": "Environment shapes behavior",
    "humanistic theory": "Personal growth",
    
    # Psychological Disorders
    "psychological disorders": "Anxiety, Depression, Personality Disorders",
    "anxiety": "Excessive worry",
    "depression": "Mood disorder",
    "personality disorders": "Enduring patterns",
    
    # Psychological Treatments
    "psychological treatments": "Cognitive-Behavioral Therapy, Psychodynamic Therapy",
    "cognitive-behavioral therapy": "Thoughts and behaviors",
    "psychodynamic therapy": "Unconscious mind",
    
    # Psychological Innovations
    "psychological innovations": "Neuroplasticity, Mindfulness, Positive Psychology",
    "neuroplasticity": "Brain adaptability",
    "mindfulness": "Present-moment awareness",
    "positive psychology": "Well-being",
}

biology_data = {
    "what is biology": "Biology is the study of living organisms and their interactions",
    
    # Branches of Biology
    "branches of biology": "Botany, Zoology, Microbiology, Ecology",
    "botany": "Study of plants",
    "zoology": "Study of animals",
    "microbiology": "Study of microorganisms",
    "ecology": "Study of ecosystems",
    
    # Biological Concepts
    "biological concepts": "Cells, Genetics, Evolution",
    "cells": "Basic structural units",
    "genetics": "Heredity",
    "evolution": "Change over time",
    
    # Biological Processes
    "biological processes": "Photosynthesis, Respiration, Fermentation",
    "photosynthesis": "Energy from sunlight",
    "respiration": "Energy from glucose",
    "fermentation": "Energy without oxygen",
}

building_systems_data = {
    "what are building systems": "Integrated systems for building function",
    
    # Types of Building Systems
    "types of building systems": "Structural, Mechanical, Electrical, Plumbing",
    "structural systems": "Foundations, Frames, Walls",
    "mechanical systems": "HVAC, Elevators, Conveyors",
    "electrical systems": "Power distribution, Lighting, Controls",
    "plumbing systems": "Water supply, Drainage, Sanitation",
    
    "what are building techniques": "Methods for constructing buildings",
    
    # Types of Building Techniques
    "types of building techniques": "Traditional, Modern, Sustainable",
    "traditional techniques": "Craftsmanship, Hand-built",
    "modern techniques": "Prefabricated, Modular, 3D printing",
    "sustainable techniques": "Green building, Energy-efficient, Eco-friendly",

    "what is building management": "Overseeing building operations",
    
    # Types of Building Management
    "types of building management": "Facilities Management, Property Management",
    "facilities management": "Maintenance, Repairs, Operations",
    "property management": "Leasing, Marketing, Financials",
    
    "what is bim": "Digital representation of building data",
    
    # Benefits of BIM
    "benefits of bim": "Improved collaboration, Increased accuracy, Enhanced visualization",
    
    # BIM Software
    "bim software": "Autodesk Revit, Graphisoft ArchiCAD, Trimble Navisworks",
    
    "what are smart buildings": "Technologically advanced buildings",
    
    # Features of Smart Buildings
    "features of smart buildings": "Energy efficiency, Automation, IoT integration",
    
    # Benefits of Smart Buildings
    "benefits of smart buildings": "Increased efficiency, Enhanced security, Improved occupant experience",
    
    "what is green building": "Environmentally sustainable building practices",
    
    # Benefits of Green Building
    "benefits of green building": "Reduced energy consumption, Water conservation, Improved indoor air quality",
    
    # Green Building Certifications
    "green building certifications": "LEED, Energy Star, Passive House",
}

chatbot_responses = {
    **save_responses,
    **greetings,
    **conversations,
    **emotional_support,
    **jokes,
    **general_knowledge,
    **weather_responses,
    **time_date_responses,
    **biology,
    **chemistry,
    **physics,
    **earth_science,
    **space_astronomy,
    **environmental_science,
    **laugh,
    **cell_biology,
    **biology_data1,
    **genetics,
    **evolution,
    **ecology,
    **botany,
    **zoology,
    **microbiology,
    **san_itself,
    **atomic_structure,
    **molecular_structure,
    **chemical_reactions,
    **acids_bases,
    **thermodynamics,
    **organic_chemistry,
    **biochemistry,
    **mechanics,
    **thermodynamics,
    **electromagnetism,
    **optics,
    **quantum_mechanics,
    **relativity,
    **nuclear_physics,
    **oceanography,
    **meteorology,
    **geology,
    **algebra,
    **geometry,
    **calculus,
    **number_theory,
    **statistics_probability,
    **discrete_mathematics,
    **construction_data,
    **civil_engineering_data,
    **structural_engineering_data,
    **economics_data,
    **bible_data,
    **biology,
    **psychology_data,
    **computer_science_data,
    **building_systems_data,
    **religion_data,
    **biology_data,
    **physics_data
}

chatbot = Chatbot("San AI", chatbot_responses, response_saved, input_saved)


def main():
    chatbot.greet()
    print()
    while True:
        user_input = input("Chat with San AI or (quit): ")
        if user_input.lower() == 'quit':
            break
        print("San AI:", chatbot.respond(user_input))
        print()
    print("San AI: It's nice having this conversation with you, see you next time.")
    
if __name__ == "__main__":
    main()
    