from gtts import gTTS
import os
tts=gTTS(text='''he salt which is white in colour is taken in a petri dish.
Pour dilute sulfuric acid from conical flask to a small quantity of the salt in a test tube.
Light brown gas with a pungent smell is evolved from the test tube.
The anion maybe Nitrate.
Pour Iron(II) Sulphate from beaker to the test tube containing salt solution.
Slowly pour drops of concentrated sulphuric acid from the container to the corners of the test tube.
A Brown ring is formed at the junction of the acid and the solution in the test tube.
Nitrate is confirmed.''',lang="en")
tts.save("hello.mp3")
#os.system("start hello.mp3")