#////////////////////////////////////
#Mood Keywords Anaylsis Engine
#Created for LovePlus + GateBox Project
#Project under IMUS Laboratory
#////////////////////////////////////
import urllib.request
#Keywords decalration
Happy = ("happy, accidental, advantageous, appropriate, apt, auspicious, befitting, casual, convenient, correct, effective, efficacious, enviable, favorable, felicitous, fitting, fortunate, incidental, just, meet, nice, opportune, promising, proper, propitious, providential, right, satisfactory, seasonable, successful, suitable, timely, well-timed").split(", ")
Lucky = ("lucky, advantageous, bright, favorable, felicitous, fortunate, golden, halcyon, happy, hopeful, lucky, opportune, promising, propitious, prosperous, rosy, timely, well-timed").split(", ")
Sad = ("sad, bad, calamitous, dark, dejecting, deplorable, depressing, disastrous, discomposing, discouraging, disheartening, dismal, dispiriting, dreary, funereal, grave, grievous, hapless, heart-rending, joyless, lachrymose, lamentable, lugubrious, melancholic, miserable, moving, oppressive, pathetic, pitiable, pitiful, poignant, regrettable, saddening, serious, shabby, sorry, tear-jerking, tearful, tragic, unhappy, unsatisfactory, upsetting, wretched").split(", ")
Angry = ("angry, affronted, annoyed, antagonized, bitter, chafed, choleric, convulsed, cross, displeased, enraged, exacerbated, exasperated, ferocious, fierce, fiery, fuming, furious, galled, hateful, heated, hot, huffy, ill-tempered, impassioned, incensed, indignant, inflamed, infuriated, irascible, irate, ireful, irritable, irritated, maddened, nettled, offended, outraged, piqued, provoked, raging, resentful, riled, sore, splenetic, storming, sulky, sullen, tumultous/tumultuous, turbulent, uptight, vexed, wrathful").split(", ")
Tired = ("tired, annoy, bore, burn out, bush, collapse, crawl, debilitate, deject, depress, disgust, dishearten, dispirit, displease, distress, drain, droop, drop, enervate, ennui, exasperate, fag, fail, faint, fatigue, flag, fold, give out, go stale, grow weary, harass, irk, irritate, jade, nauseate, overburden, overstrain, overtax, overwork, pain, pall, peter out, poop out, prostrate, put to sleep, sap, sicken, sink, strain, tax, vex, weaken, wear, wear down, wear out, wilt, worry, yawn").split(", ")
Unhappy = ("bleak, bleeding, blue, bummed out, cheerless, crestfallen, dejected, depressed, despondent, destroyed, disconsolate, dismal, dispirited, down and out, down in the mouth, down, downbeat, downcast, dragged, dreary, gloomy, grim, heavy-hearted, hurting, in a blue funk, in pain, in the dumps, let-down, long-faced, low, melancholy, mirthless, miserable, mournful, oppressive, put away, ripped, saddened, sorrowful, sorry, teary, troubled").split(", ")
Fuck = ("fuck, motherfucker, asshole, assfuck, shit, shithole, fuckyou, ediot, fucking, stupid").split(", ") 
stressed = ("stress, accent, belabor, dwell, feature, harp, headline, italicize, emphasis, emphatic, repeat, spot, spotlight, underline, underscore").split(", ")
pleasure = ("pleasure, amusement, bliss, comfort, contentment, delectation, diversion, ease, enjoyment, entertainment, felicity, flash*, fruition, game, gladness, gluttony, gratification, gusto, hobby, indulgence, joie de vivre, joy, joyride, kicks, luxury, primrose path, recreation, relish, revelry, satisfaction, seasoning, self-indulgence, solace, spice, thrill, titillation, turn-on, velvet, zest").split(", ")
#("").split(", ")


def ExactIn(array, item):
    for i in range(0,len(array)):
        if array[i] == item:
            return True
    return False

class Analysis():
    def GetMood(sentence):
        words = Analysis.GetWords(sentence)
        hs = 0 #Happy Score
        ss = 0 #Sad Score
        angs = 0 #Angry Score
        tirs = 0 #Tired Score
        #print(words)
        for word in words:
            word = word.lower()
            if Analysis.CFC(word,Happy) or Analysis.CFC(word,Lucky) or Analysis.CFC(word,pleasure):
                hs += 1
            if Analysis.CFC(word,Sad) or Analysis.CFC(word,stressed):
                ss += 1
            if Analysis.CFC(word,Angry) or Analysis.CFC(word,Fuck):
                angs += 1
            if Analysis.CFC(word,Sad)or Analysis.CFC(word,Unhappy):
                tirs += 1
        total = hs + ss + angs + tirs
        print("Happy Percentage: ",end="")
        print(int((hs/total) * 100),end=" %\n")
        print("Sad Percentage: ",end="")
        print(int((ss/total) * 100),end=" %\n")
        print("Angry Percentage: ",end="")
        print(int((angs/total) * 100),end=" %\n")
        print("Tired Percentage: ",end="")
        print(int((tirs/total) * 100),end=" %\n")
    def CFC(word,array):
        #Wordform changing test
        if word in array:
            return True
        elif word.replace("ed","ing") in array:
            return True
        elif word.replace("ing","ed") in array:
            return True
        elif word.replace("ed","") in array:
            return True
        elif word.replace("ing","") in array:
            return True
        else:
            return False
    
    def GetWords(sentence):
        sentence = sentence.replace(", "," ")
        sentence = sentence.replace(". "," ")
        sentence = sentence.replace(","," ")
        sentence = sentence.replace(".","")
        sentence = sentence.replace('"',"")
        sentence = sentence.replace("'","")
        sentence = sentence.replace("?","")
        sentence = sentence.split(" ")
        return sentence

def main():
    Analysis.GetMood(input("Please enter a sentence:\n"))
print("[info]Text Mood Analysis Engine Initialated.")
print("[info]Input 'main()' to start demo.")
