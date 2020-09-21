s=True
while s==True:
    print('''
    1. Aries
    2. Taurus
    3. Gemini
    4. Cancer
    5. Leo
    6. Virgo
    7. Libra
    8. Scorpio
    9. Sagittarius
    10. Capricorn
    11. Aquarius
    12. Pisces
    13. To Exit
    ''')
    a=int(input("Enter your sign number\n"))
    if a<13:
        print("Your Horoscope for Today is....\n")
    if a==1:
        print("Acting impulsively is not only okay today, it's highly encouraged! Caution has its place in your life, but not right now, so throw it to the wind! You are in a safe place both emotionally and professionally, which means you should feel comfortable taking a bit more risk in your daily life. You still need to wear your seat belt, of course, but you don't necessarily have to edit yourself as much when you're in the presence of higher-ups. Say what you think and watch what happens!\n")
    elif a==2:
        print("Is someone in your life getting a bit too full of themselves? As much as you hate arrogance, you can't let them push your buttons. They would just love to get a reaction out of you, so why give them the satisfaction? They only want attention, and they don't care whether it's good attention or bad attention. Instead, try to see their behavior as funny. Laugh like you've just heard the funniest joke. That will make it clear to them that they can't get to you.\n")   
    elif a==3:
        print("You need to know where to go for the information that will help you most in life. Instead of asking friends for advice on how to fatten up your rapidly thinning piggy bank, ask an expert. Friends are who you should talk to about your love life, work hassles, and other personal issues. But when it comes to credit, investments, and your savings account, you don't want to mix those two worlds. Sharing too much about how much money you make or have could also create unnecessary friction.")
    elif a==4:
        print("Get out your finest fine-toothed comb because you'll need to go over some very fine print one more time. There are an awful lot of small details that could grow into big, embarrassing issues later on down the line if you don't nip them in the bud now. Probably the last thing you want to do is proofread or double-check your work one more time, but you should do it. It will save you a lot more of your time (and your pride) in the long run.")
    elif a==5:
        print("Despite the fact that you're feeling better than you have in a while, right now is not the time to go out and celebrate. You are not overly impulsive as a rule, but today you should behave even more conservatively than usual. Bide your time and the right opportunity to have a blast will present itself soon enough. Skip any splurges and stay close to home. You can have just as celebratory a time cuddled up with a good book or your partner as you can at a big party.") 
    elif a==6:
        print("Today is a great day to try a new food, hobby, sport, or adventure that you have always been just a little to scared to try before. Your fears are starting to vanish and your courage is growing, in part because your mind is hungry for new stimulation—even if that stimulation is based on fear! You will be totally fiery and full of energy, so put it to good use by pushing the envelope and pushing past one or two of the boundaries you've built for yourself.")
    elif a==7:
        print("If you are stuck in the middle of a dilemma right now, doing something that you think is right (even if you aren't totally sure it's right) is better than doing nothing at all. Stop trying to nail down every single detail. You can't eliminate every potential problem. It's time to start acting! Things are never going to be perfect, so if you're waiting until they are, you will be waiting a very long time—too long, in fact. You need to keep moving even if you don't know exactly where you're going.")
    elif a==8:
        print("If you are stuck in the middle of a dilemma right now, doing something that you think is right (even if you aren't totally sure it's right) is better than doing nothing at all. Stop trying to nail down every single detail. You can't eliminate every potential problem. It's time to start acting! Things are never going to be perfect, so if you're waiting until they are, you will be waiting a very long time—too long, in fact. You need to keep moving even if you don't know exactly where you're going.")
    elif a==9:
        print("The people you associate with today will be very important. Some people will seem to be right on your wavelength, but others may drive you absolutely crazy! As soon as you feel that someone is rubbing you the wrong way, distance yourself from them. You aren't in the right frame of mind to deal with feeding people's egos or sacrificing your own desires. What you need now is to be surrounded by people who get you, the people who use the same shorthand you use.")
    elif a==10:
        print("Are you running the risk of getting too big for your britches? Just in case, you should give yourself a reality check today before someone else does! Make an effort to get more grounded. Spend time with people who live a different lifestyle. Get a glimpse of what their biggest issues, goals, and concerns are. Just a little bit of effort will wake you up to the reality of your situation and make you much more grateful for what you have.")
    elif a==11:
        print("This might seem like a typical day early on, but as each hour goes by, you could start to see more and more mysterious actions and events cropping up. Who are the perpetrators? What are they up to!? If you look beneath the surface, you will start to see a pattern and an agenda. This is something exciting, and you should not ignore it. Try to get involved in their shenanigans and you will have a lot of fun. They could use a bright, witty person like you!")
    elif a==12:
        print("A relationship that you thought was broken beyond all repair still has some life in it. Figure out how you can put it on the road to recovery. There are two people involved in this messy situation, and each of you has your own apologies to make. Be a hero and be the first one to extend an olive branch. Call or e-mail them today. Let them know you're thinking about them and be honest about how you feel. Let down your guard and speak from the heart.")
    elif a==13:
        s=False
        print("Exited the program...")
    else:
        print("Invalid number...Try Again")
