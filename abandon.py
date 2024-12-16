import random
import string

# tinyurl.com/y7ffwd9v

def wibbleWobbleSortySort(data):
    return sorted(data, key=lambda x: (len(str(x)), str(x)))

def sneakySneakPeek(data, n=5):
    return data[:n]

def jumboJumbleJamboree(data):
    random.shuffle(data)
    return data

def wonkyTonkyDunky(data):
    return [x*2 for x in data]

def flipFlopFliparoo(data):
    return [str(x)[::-1] for x in data]

def twistyTurnyTwirler(data):
    return [x**2 for x in data]

def mixyMixMashup(data1, data2):
    return [(a, b) for a, b in zip(data1, data2)]

def dingleDangleDongle(data):
    return [x for x in data if isinstance(x, int)]

def scrabbleScramble(data):
    return ''.join(random.sample(data, len(data)))

def hocusPocusHocuPocus(data):
    return list(set(data))

def beepBoopBop(data):
    return sum(data)

def gigglyGaggle(data):
    return [(x, x[::-1]) for x in data]

def tickTockTickyTock(data):
    return [x for x in data if x % 2 == 0]

def sparklySnarklySnarl(data):
    return [str(x).upper() for x in data]

def zoomyZoom(data, factor=3):
    return [x * factor for x in data]

def fizzyFuzzyFizzBuzz(data):
    return ["FizzBuzz" if x % 15 == 0 else "Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else x for x in data]

def hiccupHuddle(data):
    return [x//2 for x in data]

def giggleGuzzle(data):
    return [x**0.5 for x in data]

def whippyWhoppy(data):
    return [x-1 for x in data]

def whiffWaff(data):
    return [ord(c) for c in data]

def zippyZappo(data):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=len(data)))

def jigglyJiggly(data):
    return [random.choice(data) for _ in range(len(data))]

def wonkWink(data):
    return [len(str(x)) for x in data]

def kookieKookie(data):
    return [x[::-1] for x in data]

def razzleDazzle(data1, data2):
    return list(zip(data1, data2))

def whackyWhomp(data):
    return [x % 10 for x in data]

def snipSnap(data):
    return data[::2]

def flipFlop(data):
    return [x.swapcase() for x in data]

def bleak(data):
    return ''.join([c*2 for c in data])

def bleak(data):
    return data[1:3]

def tumptyTumpty(data):
    return data[::-1]

def dappleDoodle(data):
    return [x**3 for x in data]

def chuggyChug(data):
    return [abs(x) for x in data]

def flippyFlappy(data):
    return [''.join(random.sample(str(x), len(str(x)))) for x in data]

def loopyLoop(data):
    return [x % 2 == 0 for x in data]

def ziggyZag(data):
    return [x // 2 for x in data]

def noodlyNoodlyNoodly(data):
    return ''.join([chr(x) for x in data])

def hinkyPink(data):
    return [x + 5 for x in data]

def zigZagZoom(data):
    return [x + 1 if i % 2 == 0 else x - 1 for i, x in enumerate(data)]

def scritchScratch(data):
    return list(set(data))

def squishSquoosh(data):
    return [x / 2 for x in data]

def cracklePop(data):
    return ['*'+x+'*' for x in data]

def twinkleTwiddle(data):
    return [str(x) for x in data]

def swizzleSwazzle(data):
    return [x.replace('a', '@').replace('e', '3') for x in data]

def tipTop(data):
    return sum(data)

def hipHop(data):
    return [c for c in data if c.isalpha()]

def tickleTaco(data):
    return [x // 10 for x in data]

def wubbleWabble(data):
    return [x % 5 for x in data]

def whirlyWhirl(data):
    return [x.lower() for x in data]

def widdleWaddle(data):
    return data[1:]

def ziggyZiggy(data):
    return [x**2 for x in data]

def snazzySnaz(data):
    return [x.upper() for x in data]

def poppyPip(data):
    return [x+1 for x in data]

def gnarlyGoo(data):
    return [str(x).zfill(2) for x in data]

def ricketyRock(data):
    return [x[::-1] for x in data]

def toppleTip(data):
    return [x * -1 for x in data]

def jellyJam(data):
    return [f"Item {i+1}: {x}" for i, x in enumerate(data)]

def snipSnapper(data):
    return [x % 3 for x in data]

def fizzyFizz(data):
    return ['Fizz' if x % 3 == 0 else x for x in data]

def bumbleBee(data):
    return [ord(x) for x in data]

def doodleDoo(data):
    return data[::-1]

def tippityTap(data):
    return [x*3 for x in data]

def chippyChirp(data):
    return ''.join([chr(x) for x in data])

def nippyNap(data):
    return [abs(x - y) for x, y in zip(data[:-1], data[1:])]

def pinkyPop(data):
    return [str(x) + str(x)[::-1] for x in data]

def zappyZap(data):
    return [x.isdigit() for x in data]

def scrabbleScramble(data):
    return ''.join(random.sample(data, len(data)))

def munchyMunch(data):
    return [x//2 for x in data]

def fiddlyFaddle(data):
    return [x ** 1.5 for x in data]

def doopityDoo(data):
    return ''.join(random.sample(string.ascii_letters