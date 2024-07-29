import pywhatkit
from prepro import extractNoWA

def automateWA(start, end, image_path, caption_path, WA_path):
    noWA = extractNoWA(WA_path)
    if start == 'ALL' or end == 'ALL':
        startIndex = 0
        endIndex = len(noWA) 
    elif isinstance(start, int) and isinstance(end, int):
        startIndex = start
        endIndex = end
        if endIndex > len(noWA):
            endIndex = len(noWA)
        if startIndex < 0:
            startIndex = 0
    else:
        startIndex = 0
        endIndex = len(noWA)
    
    a = '\\'
    caption_path = caption_path.replace('\\', a)
    with open (caption_path, encoding='utf-8') as f:
        caption = f.read()
    
    for num in noWA[startIndex:endIndex]:
        pywhatkit.sendwhats_image(num, image_path, caption, 14, True, 2)