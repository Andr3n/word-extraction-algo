from PIL import Image
from pathlib import Path

words_list_ru = ['и', 'в', 'не', 'на', 'я', 'быть', 'он', 'с', 'что', 'а', 'по', 'это', 'она', 'этот', 'к', 'но', 'они', 'мы', 'тут', 'из', 'у', 'который', 'то', 'за', 'свой',
 'сейчас', 'весь', 'год', 'от', 'так', 'о', 'для', 'ты', 'же', 'все', 'тот', 'мочь', 'вы', 'человек', 'такой', 'его', 'сказать', 'только', 'или', 'ещё', 'бы', 'себя', 'один', 'как', 'уже',
 'до', 'время', 'если', 'сам', 'когда', 'другой', 'вот', 'говорить', 'наш', 'мой', 'знать', 'стать', 'при', 'чтобы', 'дело', 'жизнь', 'кто', 'первый', 'очень', 'два', 'день', 'её', 'новый', 'рука', 'даже',
 'во', 'со', 'раз', 'где', 'там', 'под', 'можно', 'ну', 'какой', 'после', 'их', 'работа', 'без', 'самый', 'потом', 'надо', 'хотеть', 'ли', 'слово', 'идти', 'большой', 'должен', 'место', 'иметь', 'ничто']

words_list_en = ['i', 'v', 'ne', 'na', 'ja', "byt'", 'on', 's', 'chto', 'a', 'po', 'eto', 'ona', 'etot', 'k', 'no', 'oni', 'my', 'tut', 'iz', 'u', 'kotoryj', 'to', 'za', 'svoj',
 'sejchas', "ves'", 'god', 'ot', 'tak', 'o', 'dlja', 'ty', 'zhe', 'vse', 'tot', "moch'", 'vy', 'chelovek', 'takoj', 'ego', "skazat'", "tol'ko", 'ili', 'esche', 'by', 'sebja', 'odin', 'kak', 'uzhe',
 'do', 'vremja', 'esli', 'sam', 'kogda', 'drugoj', 'vot', "govorit'", 'nash', 'moj', "znat'", "stat'", 'pri', 'chtoby', 'delo', "zhizn'", 'kto', 'pervyj', "ochen'", 'dva', "den'", 'ee', 'novyj', 'ruka', 'dazhe',
 'vo', 'so', 'raz', 'gde', 'tam', 'pod', 'mozhno', 'nu', 'kakoj', 'posle', 'ih', 'rabota', 'bez', 'samyj', 'potom', 'nado', "hotet'", 'li', 'slovo', 'idti', "bol'shoj", 'dolzhen', 'mesto', "imet'", 'nichto']

# Making Path to dataset
path_to_dataset = Path(r'Path-to-dataset')

# Make folders name of sources
folder_names = ['folder1', 'folder2']

# Getting paths to images
list_images_path = []
for fname in folder_names:
    path_to_images = path_to_dataset / fname
    image_names = path_to_images.glob('*')
    preffix = f'_from_{fname}_'
    for iname in image_names:
        list_images_path.append(iname)


def one_word_extract(img_path, row=1, column=1, rotate_coef=0, cell_start=None, tw=119, cw=135, th=6.75, ch=55, save_images=False):
    """
    One word extract function
    Args:
        img_path - Path to image
        row [1, 25] - Row in document scan
        column [1, 4] - Column in document scan
        rotate_сoef - image tilt coef
        cell_start (x, y) - the point of the leftmost corner of the cell with the word
        tw - the width of the transition from the cell with the word to the next cell
        cw - cell width
        th - the height of the transition from the cell with the word to the next cell
        ch - cell height
        save_image - Flag to save image to computer
    """

    if not cell_start:
        raise(BaseException('Cell_start is empty'))
    elif str(type(cell_start)) != "<class 'list'>":
        raise(BaseException('Cell_start is not a list'))
    
    if rotate_coef == 0:
        img = Image.open(img_path)
    else:
        img = Image.open(img_path).rotate(rotate_coef)
    
    transition_width = tw
    cell_width = cw
    
    transition_height = th
    cell_height = ch

    x1 = cell_start[0] + int((transition_width + cell_width) * (column - 1))
    y1 = cell_start[1] + int((transition_height + cell_height) * (row - 1))
    x2 = x1 + cell_width
    y2 = y1 + cell_height


    area = (x1, y1, x2, y2)
    print(area)
    img_cropped = img.crop(area)

    if save_images:
        i_column = column - 1
        path_to_save = Path(r'path-to-save')
        img_cropped.save(path_to_save / (words_list_ru[row + i_column * 25 - 1] + f'_{index}' + '.jpg'))

# Extracting a word in the loop
for row in range(1, 26):
    cell_start = [515, 38]
    index = 2
    one_word_extract(list_images_path[index],
                     row=row,
                     column=3,
                     cell_start=cell_start,
                     rotate_koef=-0.25,
                     tw=235,
                     cw=270,
                     th=13.5,
                     ch=115,
                     save_images=True)