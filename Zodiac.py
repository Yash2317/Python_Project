# An Apllication Which Tells Future based upon the Zodiac Sign

next = True  
while next == True:
    print('''Select You Zodiac Sign from bellow:
    1)Aries
    2)Taurus
    3)Gemini
    4)Cancer
    5)Leo
    6)Vigro
    7)Libra
    8)Scorpio  
    9)Sagittarius
    10)Capricon
    11)Aquarius
    12)Pisces
    ''')

    s = int(input("Pick your Zodiac sign number an Pres Enter\n"))

    if s==1:
        print("You might not get the things done that you want to do today, Aries, but don't sweat it. Go easy on yourself if you still have a few unchecked things on the list tonight. People may pop out of nowhere and demand your attention for much of the time. Listen, be present, and try not to think of the things that aren't getting done. Focus on those things that are getting done.")

    elif s==2:

        print("Today is a fantastic day, Taurus, so make the most of it. If you're emotionally and mentally prepared to go on a new, exciting life journey, the opportunity will present itself. The energy will be fast and furious. You can work harmoniously with electrical gadgets and new technologies. Break free of the mundane and seek less conventional ways of living.")
    elif s==3:
        print("You'll be tested today, Gemini, so brace yourself for the unexpected. A large piece of your life is coming into question at this time, and you're being forced to face the music. Is this something that really rings true with your inner being? If it is, you should be able to deal with this challenge. If you're struggling, perhaps you should take this as a sign that you need a major life change.")
    elif s==4:
        print("You have lots of energy at your disposal today, Cancer, but it's erratic and powerful. You have the stamina to make major changes, and the opportunity to break free from any restrictions that hold you back. Embrace the new, fresh aspects of your life that ring true to your freedom-loving nature. Give your soul room to breathe as you take a long walk in nature this afternoon.")
    elif s==5:
        print("It's time to take a bold step forward, Leo. Have confidence in yourself and all the careful planning you've been painstakingly doing for the past few months. Realize that much of this hard work is paying off, but only if you're willing to take the next step. The opportunity is there. All you need to do is jump on it. Act out of faith and confidence instead of fear and restriction.")
    elif s==6:
        print("You can't ask for a better day, Virgo. Positive energy is coming your way. You should look for the opportunities that are right in front of you. You may be going through some significant upheaval right now. Clear away all the things that have limited you in the past. The future is wide open. Empower yourself to make the changes necessary to build your life way you want it to be.")
    elif s==7:
        print("Be on your toes today, Libra, and expect the unexpected. People may be acting out in rash, outlandish ways, so go with the flow. As usual, you have a tremendous ability to roll with the punches and still come out unscathed. Just take care that someone else isn't grabbing the reins. Stay laid-back while maintaining control of your actions.")
    elif s==8:
        print("Be on your toes today, Libra, and expect the unexpected. People may be acting out in rash, outlandish ways, so go with the flow. As usual, you have a tremendous ability to roll with the punches and still come out unscathed. Just take care that someone else isn't grabbing the reins. Stay laid-back while maintaining control of your actions.")
    elif s==9:
        print("You may find people very stubborn today, so take care, Sagittarius. Arguments can explode out of nowhere, so have your helmet ready. Think before you act and don't feel pressured to get involved in something that makes you feel uncomfortable. Remember that it's OK to just walk away. No one will win the boxing match, so don't even get in the ring.")
    elif s==10:
        print("Initiate a major change in your life, Capricorn. Break free of the humdrum and launch into something exciting. Take part in an online class that expands your mind. Consider yoga, tarot, or any form of martial arts. You have a tremendous amount of energy today. It will help you maintain confidence and endurance as you do the groundwork to put this new life-enhancing endeavor in motion.")
    elif s==11:
        print("Action is the word of the day. Whether you're initiating it or feeling the brunt of it, you'll be caught up in the vortex of it. Try not to lose your tempter today, Aquarius, and don't be surprised if people act rashly and insensitively. Perhaps this is their way of saying they need you and that your energy and input are important. Have confidence in your words.")                    
    elif s==12:
        print(" Today may be filled with sudden changes and unexpected events, Pisces. The energy is electric and strong. People will act in erratic, powerful bursts. Try to stay centered and maintain your focus. Keep in mind that if you need to break free from certain limitations, now is the time to make that move. Have confidence in your actions and make it happen.")    
    else:
        print("Hey you are sure with thw number")
           
    next = True if input("\nShall we do it again? (y/n) ")=="y" else False 
