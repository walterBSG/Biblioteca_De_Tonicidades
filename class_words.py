import io
import re
import os

def classText():
    filenames = next(os.walk('text'), (None, None, []))[2]
    for file in filenames:
        text = io.open('text/'+file, encoding="utf8").read().split('\n')
        ox = getOx(text)
        prop = getProp(text)
        par = getPar(text)
        with open('result/ox_'+file, 'w',encoding="utf8") as f:
            f.write("\n".join(ox))
        with open('result/prop_'+file, 'w',encoding="utf8") as f:
            f.write("\n".join(prop))
        with open('result/par_'+file, 'w',encoding="utf8") as f:
            f.write("\n".join(par))

def oxreg():
    return re.compile("(^([A-zÀ-úç-]*-)*[A-zç]*((á|í|ú)s?|(é|ó)(s|i)?|ás?|é(ns|m|u)|ã(s|o|os)?|õ(s|e|es)?|(ú|í)(m|n)?|(i|u)(m|n)|r|l|z|x)(-(lo|la)s?)?$|^[a-zA-Z\u00C0-\u00FF]$)")

def propreg():
    return re.compile("^[A-zÀ-úç-]*[À-ú][bcdfghjklmnpqrstvwxysç]+[aeiouy]+[bcdfghjklmnpqrstvwxysç]+[aeiouyãõ]+s?$")

def getOx(text):
    r = oxreg()
    ox = list(filter(r.match, text))
    return ox

def getProp(text):
    r = propreg()
    prop = list(filter(r.match, text))
    return prop

def getPar(text):
    ox = oxreg()
    prop = propreg()
    par = [w for w in text if not (ox.match(w) or prop.match(w))]
    return par

def getType(word):
    ox = oxreg()
    prop = propreg()
    if ox.match(word):
        return 'Oxitona'
    elif prop.match(word):
        return 'Proparoxitona'
    else:
        return 'Paroxitona'

def getTypes(text):
    return [getType(w) for w in text]

def getTuples(text):
    return [(word, getType(word)) for word in text]

def main():
    classText()

if __name__ == '__main__':
    main()