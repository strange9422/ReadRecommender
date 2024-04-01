import re
import pandas as pd

import warnings

warnings.filterwarnings("ignore")


books = pd.read_csv('Preprocessed_data.csv')

df = books.copy()
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)

df.drop(columns=['Unnamed: 0', 'location', 'isbn',
                 'img_s', 'city', 'age',
                 'state', 'Language', 'country',
                 'year_of_publication'], axis=1, inplace=True)  # remove useless cols

df.drop(index=df[df['Category'] == '9'].index, inplace=True)  # remove 9 in category

df.drop(index=df[df['rating'] == 0].index, inplace=True)  # remove 0 in rating

df['Category'] = df['Category'].apply(lambda x: re.sub('[\W_]+', ' ', x).strip())

bk=pd.read_csv('Books.csv',delimiter=';', error_bad_lines=False, encoding='ISO-8859-1',warn_bad_lines=False)


def category_fiction():
    a = df.drop(columns=['user_id', 'img_l', 'rating'], axis=1)

    a = a.drop_duplicates(subset='book_title', keep=False)
    a.rename(columns={'book_title': 'Book-Title'}, inplace=True)
    a = a.merge(bk, on='Book-Title')
    a.drop_duplicates('Book-Title')

    a.rename(columns={'Book-Title': 'book_title'}, inplace=True)
    category_list = ['Vampires', 'Indian mythology','Historical fiction','FICTION', 'Fairy tales','Fantasy fiction English', 'Fantasy',
                     'Fantasy fiction American', 'Adventure fiction', 'Science fiction Australian',
                     'Mystery fiction', 'Detective and mystery fiction ', 'Fiction', 'Science fiction French',
                     'Historical fiction',  'German fiction', 'Romance fiction',
                     'Young adult fiction',
                     'English fiction',  'Young Adult Fiction', 'Argentine fiction',
                     'Political fiction', 'Fiction in English', 'Spanish fiction', 'Fiction Espionage',
                     'Swedish fiction', 'Medical fiction', 'Romance fiction Canadian', 'Fiction in English 1945 Texts',
                     'French Canadian fiction', 'Fantasy fiction American', 'Science fiction Canadian',
                     'Yiddish fiction', 'Superhero fiction', 'Science fiction Polish', ' Romance fiction',
                     'American wit and humor']
    dic = {}
    list_name = []
    for i in range(len(category_list)):
        name = a[a['Category'] == category_list[i]]['book_title'].tolist()
        for k in name:
             list_name.append(k)

    if len(list_name) > 50:
        for j in range(50):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]
    else:
        for j in range(len(list_name)):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]

    return dic


def category_Comics():
    a = df.drop(columns=['user_id', 'img_l', 'rating'], axis=1)

    a = a.drop_duplicates(subset='book_title', keep=False)
    a.rename(columns={'book_title': 'Book-Title'}, inplace=True)
    a = a.merge(bk, on='Book-Title')
    a.drop_duplicates('Book-Title')

    a.rename(columns={'Book-Title': 'book_title'}, inplace=True)

    category_list = ['Cartoons and comics', 'Comic books strips etc', 'Humor', 'Humorous stories', 'Comedians',
                     'Comics Graphic Novels', 'Cartoons and comics', 'Caricatures and cartoons']
    dic = {}

    list_name = []
    for i in range(len(category_list)):
        name = a[a['Category'] == category_list[i]]['book_title'].tolist()
        for k in name:
            list_name.append(k)

    if len(list_name) > 50:
        for j in range(50):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]
    else:
        for j in range(len(list_name)):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]

    return dic


def category_drama():
    a = df.drop(columns=['user_id', 'img_l', 'rating'], axis=1)

    a = a.drop_duplicates(subset='book_title', keep=False)
    a.rename(columns={'book_title': 'Book-Title'}, inplace=True)
    a = a.merge(bk, on='Book-Title')
    a.drop_duplicates('Book-Title')

    a.rename(columns={'Book-Title': 'book_title'}, inplace=True)

    category_list = ['English drama', 'Drama', 'American drama', 'Duitse drama', 'Motion picture actors and actresses',
                     'French drama', 'Greek drama', 'New Zealand drama', 'Dramatists', 'Australian drama',
                     'Domestic drama']
    dic = {}

    list_name = []
    for i in range(len(category_list)):
        name = a[a['Category'] == category_list[i]]['book_title'].tolist()
        for k in name:
            list_name.append(k)

    if len(list_name) > 50:
        for j in range(50):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]
    else:
        for j in range(len(list_name)):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]

    return dic


def category_romantic():
    a = df.drop(columns=['user_id', 'img_l', 'rating'], axis=1)

    a = a.drop_duplicates(subset='book_title', keep=False)
    a.rename(columns={'book_title': 'Book-Title'}, inplace=True)
    a = a.merge(bk, on='Book-Title')
    a.drop_duplicates('Book-Title')

    a.rename(columns={'Book-Title': 'book_title'}, inplace=True)

    category_list = ['Love stories', 'Valentine s Day', 'Love', 'Poets American', 'Children s poetry American',
                     'Love poetry',
                     'Love poetry German', 'Love poetry English''American poetry', 'Arabic poetry', 'Poetry',
                     'Children s poetry English',
                     'Love poetry', 'Australian poetry', 'French poetry', 'Christmas poetry', 'Bengali poetry ']
    dic = {}

    list_name = []
    for i in range(len(category_list)):
        name = a[a['Category'] == category_list[i]]['book_title'].tolist()
        for k in name:
            list_name.append(k)

    if len(list_name) > 50:
        for j in range(50):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]
    else:
        for j in range(len(list_name)):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]
    return dic


def category_horror():
    a = df.drop(columns=['user_id', 'img_l', 'rating'], axis=1)

    a = a.drop_duplicates(subset='book_title', keep=False)
    a.rename(columns={'book_title': 'Book-Title'}, inplace=True)
    a = a.merge(bk, on='Book-Title')
    a.drop_duplicates('Book-Title')

    a.rename(columns={'Book-Title': 'book_title'}, inplace=True)

    category_list = ['Ghosts', 'Horror stories', 'Horror',
                     'Ghost stories American ', 'Ghosts ', 'Ghost stories']
    dic = {}

    list_name = []
    for i in range(len(category_list)):
        name = a[a['Category'] == category_list[i]]['book_title'].tolist()
        for k in name:
            list_name.append(k)

    if len(list_name) > 50:
        for j in range(50):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]
    else:
        for j in range(len(list_name)):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]

    return dic


def category_crime():
    a = df.drop(columns=['user_id', 'img_l', 'rating'], axis=1)

    a = a.drop_duplicates(subset='book_title', keep=False)
    a.rename(columns={'book_title': 'Book-Title'}, inplace=True)
    a = a.merge(bk, on='Book-Title')
    a.drop_duplicates('Book-Title')

    a.rename(columns={'Book-Title': 'book_title'}, inplace=True)

    category_list = ['Serial murders', 'Crime', 'Murder', 'Criminals', 'Murderers',
                     'Crime and criminals']
    dic = {}

    list_name = []
    for i in range(len(category_list)):
        name = a[a['Category'] == category_list[i]]['book_title'].tolist()
        for k in name:
            list_name.append(k)

    if len(list_name) > 50:
        for j in range(50):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]
    else:
        for j in range(len(list_name)):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]

    return dic


def category_mystery():
    a = df.drop(columns=['user_id', 'img_l', 'rating'], axis=1)

    a = a.drop_duplicates(subset='book_title', keep=False)
    a.rename(columns={'book_title': 'Book-Title'}, inplace=True)

    a = a.merge(bk, on='Book-Title')
    a.drop_duplicates('Book-Title')

    a.rename(columns={'Book-Title': 'book_title'}, inplace=True)

    category_list = ['Mystery and detective stories', 'Detective and mystery stories American',
                     'Detective and mystery stories German',
                     'Detective and mystery fiction', 'Detective and mystery stories',
                     'Detective and mystery plays American',
                     'Detective and mystery stories English']
    dic = {}

    list_name = []
    for i in range(len(category_list)):
        name = a[a['Category'] == category_list[i]]['book_title'].tolist()
        for k in name:
            list_name.append(k)

    if len(list_name) > 50:
        for j in range(50):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]
    else:
        for j in range(len(list_name)):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]

    return dic


def category_education():
    a = df.drop(columns=['user_id', 'img_l', 'rating'], axis=1)

    a = a.drop_duplicates(subset='book_title', keep=False)
    a.rename(columns={'book_title': 'Book-Title'}, inplace=True)
    a = a.merge(bk, on='Book-Title')
    a.drop_duplicates('Book-Title')

    a.rename(columns={'Book-Title': 'book_title'}, inplace=True)

    category_list = ['Arithmetic', 'Political Science', 'Psychology', 'Social Science', 'Science', 'Astronomy',
                     'Education', 'Business Economics',
                     'Chemistry', 'Law', 'Behavior', 'Chemistry Physical and theoretical', 'Mathematics',
                     'Foreign Language Study', 'Historical geography', 'Counting',
                     'Mathematical recreations', 'History Modern', 'Picture books', 'Vocabulary', 'Literature Modern',
                     'Children s literature American', 'Latin language',
                     'Mathematicians', 'Environmental geology', 'Economics', 'Sociology', 'Chinese language',
                     'Excavations Archaeology', 'Geology', 'Human ecology',
                     'Astrology', 'Psychoanalysis and philosophy', 'Astrophysics', 'Biology', 'Chemistry Forensic',
                     'Italian language', 'Conflict Psychology',
                     'Christianity and economics', 'Choice Psychology', 'Irish language', 'Ecology', 'Cosmology ',
                     'Business communication', 'Alienation Social psychology']
    dic = {}

    list_name = []
    for i in range(len(category_list)):
        name = a[a['Category'] == category_list[i]]['book_title'].tolist()
        for k in name:
            list_name.append(k)

    if len(list_name) > 50:
        for j in range(50):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]
    else:
        for j in range(len(list_name)):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]

    return dic


def category_sports():
    a = df.drop(columns=['user_id', 'img_l', 'rating'], axis=1)

    a = a.drop_duplicates(subset='book_title', keep=False)
    a.rename(columns={'book_title': 'Book-Title'}, inplace=True)

    a = a.merge(bk, on='Book-Title')
    a.drop_duplicates('Book-Title')

    a.rename(columns={'Book-Title': 'book_title'}, inplace=True)

    category_list = ['Sports Recreation', 'Track and field athletes', 'Games Activities', 'Games', 'Clue Game',
                     'Baseball', 'Boxers Sports', 'Soccer', 'Hiking', 'Puzzles', 'Adventure games', 'Football',
                     'Baseball stories', ' Mountaineering', 'Amusements',
                     'Chess', 'Tennis coaches', 'Soccer players', 'Bicycles', 'Amusement parks', 'Athletes',
                     'Board games', 'Wrestlers', ' Sega Genesis Game', 'Nintendo video games', 'Star Fox 64 Game',
                     'Call of Cthulu Game', 'Call of Cthulhu Game',
                     'Tongue twisters', 'Blackjack Game', 'Pitchers Baseball', 'Picture puzzles', 'Rugby football',
                     'Skis and skiing', 'Golf', 'Basketball', 'Mountaineers', 'Video games', 'Fantasy games',
                     'Mage Game', 'Basketball players', 'Vampire Game', 'Bingo']
    dic = {}

    list_name = []
    for i in range(len(category_list)):
        name = a[a['Category'] == category_list[i]]['book_title'].tolist()
        for k in name:
            list_name.append(k)

    if len(list_name) > 50:
        for j in range(50):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]
    else:
        for j in range(len(list_name)):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]

    return dic


def category_family():
    a = df.drop(columns=['user_id', 'img_l', 'rating'], axis=1)

    a = a.drop_duplicates(subset='book_title', keep=False)
    a.rename(columns={'book_title': 'Book-Title'}, inplace=True)

    a = a.merge(bk, on='Book-Title')
    a.drop_duplicates('Book-Title')

    a.rename(columns={'Book-Title': 'book_title'}, inplace=True)

    category_list = ['Family problems', 'Families', 'Family Relationships', 'Childbirth', 'Man woman relationships',
                     'Mental illness', 'Children', 'Brothers and sisters',
                     'Death', 'Child rearing', 'Autonomy in children', 'Boys', 'Divorce', 'Family life', 'House Home',
                     'Fathers and sons', 'Marriage service', 'Babysitters', 'Men',
                     'Adoption', 'Grandmothers', 'Family violence', 'Baby sitters Club Imaginary organization',
                     'Mothers and daughters', 'Women', 'African American families', 'Family',
                     'Divorced mothers', 'Child care', 'Pregnancy', 'Mother and child', 'Abandoned children', 'Twins',
                     'Baby sitters', 'Father and child', 'Etiquette for children and teenagers',
                     'Divorced people', 'Abused children', 'Infants', 'Prime ministers spouses', 'Babies', 'Mothers',
                     'Interpersonal relations', 'Fathers and daughters',
                     'Children and strangers', 'Family recreation', 'Foster home care', 'Feral children', 'Girls',
                     'Grandfathers', 'Family crises', 'Marriages of royalty and nobility',
                     'Child psychotherapy', 'Children and death', 'Marriage', 'FAMILY RELATIONSHIPS',
                     'Illegitimate children', 'Grandparents', 'Foster children ', 'Custody of children',
                     'Discipline of children', 'Arranged marriage', 'Dysfunctional families', 'Parent and teenager',
                     'Married people', 'Mothers and sons']
    dic = {}

    list_name = []
    for i in range(len(category_list)):
        name = a[a['Category'] == category_list[i]]['book_title'].tolist()
        for k in name:
            list_name.append(k)

    if len(list_name) > 50:
        for j in range(50):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]
    else:
        for j in range(len(list_name)):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]

    return dic


def category_food():
    a = df.drop(columns=['user_id', 'img_l', 'rating'], axis=1)

    a = a.drop_duplicates(subset='book_title', keep=False)
    a.rename(columns={'book_title': 'Book-Title'}, inplace=True)

    a = a.merge(bk, on='Book-Title')
    a.drop_duplicates('Book-Title')

    a.rename(columns={'Book-Title': 'book_title'}, inplace=True)

    category_list = ['Cookery Asian', 'Cake', 'Food', 'Sugar free diet', 'Restaurants', 'Cooking French',
                     'Cooking Chinese', 'Cooking Indic', 'Cooks', 'Wine and wine making', 'Proteins',
                     'Cookbooks', 'Cooking American', 'Cookery Mexican', 'Cookery Italian', 'Cold dishes Cooking',
                     'Cooking Herbs', 'Diet', 'Community cookbooks', 'Bread', 'Low budget cooking',
                     'Spies', 'Cookery Herbs', 'Diet therapy', 'Cookery American ', 'Baking ', 'Cooking Asian',
                     'Cooking Japanese', 'Cooking Mushrooms', 'Cooking Seafood', 'Low calorie diet',
                     'Christmas cookery', 'Dinners and dining', 'Coffee cakes', 'Toasts']
    dic = {}

    list_name = []
    for i in range(len(category_list)):
        name = a[a['Category'] == category_list[i]]['book_title'].tolist()
        for k in name:
            list_name.append(k)

    if len(list_name) > 50:
        for j in range(50):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]
    else:
        for j in range(len(list_name)):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]

    return dic


def category_technology():
    a = df.drop(columns=['user_id', 'img_l', 'rating'], axis=1)

    a = a.drop_duplicates(subset='book_title', keep=False)
    a.rename(columns={'book_title': 'Book-Title'}, inplace=True)

    a = a.merge(bk, on='Book-Title')
    a.drop_duplicates('Book-Title')

    a.rename(columns={'Book-Title': 'book_title'}, inplace=True)

    category_list = ['Data structures Computer science','Technology Engineerings', 'Linux', 'Aerospace engineers', 'HTML Document markup language',
                     'PHP Computer program language', 'Computer network architectures', 'Information technology',
                     'Microsoft Windows Computer file',
                     'Java Computer program language', 'Androids', 'Computer Communication Networks',
                     'Computer animation', 'Computer software industry', 'ASP Computer network protocol',
                     'Operating systems Computers ', 'Computer graphics',
                     'Algorithms', 'JavaScript Computer program language', 'Software engineering', 'Computer Graphics ',
                     'Computer security', 'Text editors Computer programs', 'Communications software ',
                     'Computer capacity ', 'Assembler language Computer program language',
                     'DHTML Document markup language', 'Computer science', 'Java ', 'Perl Computer program language',
                     'Computer programming', 'BASIC Computer program language', 'Computer network resources',
                     'Database design', 'Data structures Computer science', 'Computers',
                     'Java Computer program language', 'Radio broadcasters', 'Animation Cinematography',
                     'Automobile racing', 'Electric engineers', 'Internet', 'Automobile dealers',
                     'Client server computing', 'Intelligence service',
                     'Microcomputers', 'Computer Graphics', 'Computer security', 'Text editors Computer programs',
                     'Communications software',
                     'Computer capacity', 'Automobile racing drivers', 'Computer technicians', 'Radio broadcasting ',
                     'Macintosh Computer', 'Electronic commerce', 'Software maintenance ',
                     'Assembler language Computer program language', 'Microsoft PowerPoint Computer file',
                     'Solaris Computer file', 'Local area networks Computer networks', 'DHTML Document markup language']
    dic = {}

    list_name = []
    for i in range(len(category_list)):
        name = a[a['Category'] == category_list[i]]['book_title'].tolist()
        for k in name:
            list_name.append(k)

    if len(list_name) > 50:
        for j in range(50):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]
    else:
        for j in range(len(list_name)):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]

    return dic


def category_medical():
    a = df.drop(columns=['user_id', 'img_l', 'rating'], axis=1)

    a = a.drop_duplicates(subset='book_title', keep=False)
    a.rename(columns={'book_title': 'Book-Title'}, inplace=True)

    a = a.merge(bk, on='Book-Title')
    a.drop_duplicates('Book-Title')

    a.rename(columns={'Book-Title': 'book_title'}, inplace=True)

    category_list = ['Psychology', 'Health Fitness', 'Body Mind Spirit', 'Exercise', 'Medical',
                     'Assertiveness Psychology', 'Mental illness', 'AIDS Disease', 'Medication abuse',
                     'Carbohydrates Refined', 'Forensic pathologists', 'Anecdotes',
                     'Homeopathy', 'Androgyny Psychology', 'Medicine Popular', 'Weight loss',
                     'Depressions', 'Biological Rhythms', 'Chickenpox', 'Neurosurgeons', 'Drug abuse',
                     'Human physiology', 'Depression glass', 'Change Psychology',
                     'Fitness walking', 'Blindness', 'Aging', 'Mental efficiency', 'Child development', 'Drugs',
                     'Alcoholics', 'Health', ' Folk medicine', 'Appetite disorders', 'Surgery Plastic', ' Diabetes',
                     'Relaxation', 'Blind', 'Alternative medicine', 'Abortion', 'Infants Newborn',
                     'Pharmacology', 'Hallucinogenic drugs', 'Pregnancy', 'Drug interactions',
                     'Self Actualization Psychology', 'Biotechnology', 'Asthma', 'Pharmacy', 'Study Aids',
                     'Female orgasm', 'Gender identity', 'Obesity', 'Bones', 'Body Human',
                     'Meditation', 'Child psychology', 'Depression', 'Chronic fatigue syndrome', 'Dental care', 'Heart',
                     'Maternal and infant welfare', 'Consciousness', 'Naturopathy', 'Loss Psychology', 'Digestion',
                     'Abnormalities Human', 'Pharmaceutical industry',
                     'Medical students', 'Forensic psychiatry', 'Human beings', 'Eating disorder', 'Ophthalmologists',
                     'Minerals in the body', 'Medical errors', 'Homosexuality', 'Nursing ethics', 'Blind deaf',
                     'DNA fingerprinting', 'Anatomy',
                     'Medical examiners Law', 'Biology', 'Alzheimer s disease', 'Anxiety',
                     'Headache', 'Deafblind people', 'Nurses', 'Abdomen', 'Body image',
                     'Pharmacists', 'Physicians',
                     'Cold Disease', 'Gynecologists', 'Cosmology', 'Crohn s disease', 'Gynecology',
                     'Children with disabilities', 'Detoxification Health', 'Cancer', 'Backache',
                     'Medicine Psychosomatic', 'Deaf', 'Anesthesia in dentistry', 'Anabolic steroids',
                     'Mood Psychology', 'Breast', 'Neurology']
    dic = {}

    list_name = []
    for i in range(len(category_list)):
        name = a[a['Category'] == category_list[i]]['book_title'].tolist()
        for k in name:
            list_name.append(k)

    if len(list_name) > 50:
        for j in range(50):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]
    else:
        for j in range(len(list_name)):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]

    return dic


def category_fantasy():
    a = df.drop(columns=['user_id', 'img_l', 'rating'], axis=1)

    a = a.drop_duplicates(subset='book_title', keep=False)
    a.rename(columns={'book_title': 'Book-Title'}, inplace=True)

    a = a.merge(bk, on='Book-Title')
    a.drop_duplicates('Book-Title')

    a.rename(columns={'Book-Title': 'book_title'}, inplace=True)

    category_list = ['Lesbians', 'Sex in literature', 'Sex role', 'Bondage Sexual behavior', 'First sexual experiences',
                     'Gay male couples', 'Sex', 'Sex Psychology', 'Lesbianism', ]
    dic = {}

    list_name = []
    for i in range(len(category_list)):
        name = a[a['Category'] == category_list[i]]['book_title'].tolist()
        for k in name:
            list_name.append(k)

    if len(list_name) > 50:
        for j in range(50):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]
    else:
        for j in range(len(list_name)):
            dic[list_name[j]] = a[a['book_title'] == list_name[j]]['img_m'].values[0]

    return dic



