import io
import re

def getText(name = 'pt-wordlist.txt'):
    text = io.open(name, encoding="utf8").read()
    text = text.split('\n')
    return text

def oxreg():
    return re.compile("^([A-zÀ-úç-]*-)*[A-zç]*((á|í|ú)s?|(é|ó)(s|i)?|ás?|é(ns|m|u)|ã(s|o|os)?|õ(s|e|es)?|(ú|í)(m|n)?|(i|u)(m|n)|r|l|z|x)(-(lo|la)s?)?$")

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