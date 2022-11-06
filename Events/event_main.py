Events = ["Hello @everyone, The registration for 'Jeopardy' would be closed by 11 p.m. today. The qualification round will start on 22 October, 2022 6:30 p.m. IST. The rules for the quiz are as follows:-Matches will be 2v2. If you have a third player in your team, he/she can be substituted for another member only in the next round (only if you qualify).The matches would be randomly generated.20 second timer per question to answer. You can either write/speak your answer within that timeframe. Staff decision will be final.You are advised to go through the earlier provided rules once.The timer will start only after reading the complete question. You can be penalised for cutting the quizmaster in between or any similar offence.Any points you choose, you have to answer.No negative points (unless it is a powerup or mentioned otherwise). Prizes!! Winning team will be getting ₹300 Amazon gift voucher. Runner-ups will be getting ₹150 Amazon gift voucher. P.S.:- Qualification round starts tommorow,i.e. 22nd October, 6:30 pm IST. ",
        "The Engineering Program and International Engineering Program present…; Research Across the University: A Night with Engineering Faculty; Tuesday, November 1st, 5:30 p.m. / Reber 101 (E-Knowledge Commons) We have a special event in store for you - we've invited faculty across every Engineering Department to speak with you all! Join us for a faculty panel discussing their research, career paths, research opportunities within their department, and more. Following this, you will all have an opportunity to network with our faculty over dinner in Kunkle Lounge! With such a wide range of invited faculty, you are guaranteed an engaging discussion. You won't want to miss this event!",
        "Engineers, Just a reminder about this event tonight! CareerPREP:  Using Technology in your Job Search; Tuesday, October 25; 6:30 – 7:30 p.m.; 220 Hammond Building; At this session, we will discuss employer use of applicant tracking systems and review ways to optimize resume submissions in order to stand out in those environments.  We will also discuss ways to build an effective LinkedIn profile and explore the many different functions of the platform that can aid in developing your network.; All majors welcome.  No RSVP required.  Casual attire.",
        "Legendary Rock Band JOURNEY Coming to the Bryce Jordan Center; One of the most legendary rock bands of all time, Journey, just announced the continuation of their highly successful tour with the 50th Anniversary Celebration Freedom Tour 2023 featuring, very special guest TOTO.  Journey, Diamond-selling Rock & Roll Hall of Famers will take the stage at the Bryce Jordan Center Friday, March 3, 2023 with their catalog of global chart-topping hits, including 'Don't Stop Believin', 'Any Way You Want It', 'Faithfully', 'Lights' and more.  ; Very special guest  TOTO, who have collectively streamed more than 3.3 billion plays on Spotify alone based on hits including “Rosanna”, “Africa” and “Hold the Line”, will join Journey on all dates. ; STUDENT PRESALE STARTS 10AM THURSDAY, OCTOBER 20TH; Penn State Student Tickest ONLY $39* with Code: YOUR PSU ID#",
        "Thursday 10/27/22 (Virtual) 7pm Day in the Life @ Lockheed Martin Panel Discussion (Virtual) Hear from a panel of Lockheed Martin employees and hiring managers (and alumni of your school) representing every LM Business Area in roles from Business to Engineering.  Join as they share the day to day of their roles, career paths, and job-hunting suggestions. Q&A to follow! Ryan J. – Missiles & Fire Control – Engineering Intern David N.  – Aeronautics – Aeronautical Engineer Steven L. – Space – Systems Engineer Olaolu I. – Enterprise Operations – Systems Integration Analyst Matt M. – Rotary & Mission Systems – Systems Integration / Test Engineering Asc. Mgr. Day in the Life @ Lockheed Martin Panel Discussion (Virtual) Zoom Thursday 10/27/22 – 7pm",
        "ICLC Garba cohosted with IGSA this year is on October 2nd in Alumni hall at 7pm. Event Details: For the event, we have Medley Entertainment coming to perform live music on stage. DJ Amir for Bollywood Night. And much more! If you’d like to be a paid member, DM us on our Insta! The membership is only $25. What ICLC Insider entails: - Potential meet and greet with an artist if the artist agrees - Free food at events - Invitation to socials - Raffle entries - And much more!!!",
        "WWE Returns to Penn State this November! WWE returns to Bryce Jordan Center on November 20 with Sunday Stunner!  Don’t miss your chance to see WWE in person and you have the first opportunity to purchase tickets.    See Matt Riddle vs. Seth “Freakin” Rollins in a Street Fight    Drew McIntyre vs. Sheamus    Plus more of your favorite Superstars including RAW Women’s Champion Bianca Belair,   Braun Strowman, SmackDown Women’s Champion Liv Morgan,   Damage CTRL’s Bayley, IYO SKY & Dakota Kai and many more!  Card subject to change.    Superstar Experience & Walk the Aisle VIP Packages also available.   STUDENT PRESALE HAPPENING NOW! Penn State Student's SAVE $26 with code: YOUR PSU ID#",
        "Hi All,  We are hosting the attached event on Wednesday, September 28th The shift would be 4:30p-9:30p and you will receive 2 free meal/free drink card if you pick up a shift on that night! The shift will be under Special Dinner for anyone would like to pick up!",
        "Hello Harsh, Do you want assistance with your resume from an industry professional or career services professional?  If so, you have an opportunity to have your resume reviewed prior to Fall Career Days!    Resume Review   Resume Review is an opportunity for employers and career staff to review the resumes of Penn State students who are preparing for Fall Career Days, offering them feedback for improvement. Students do not need to register in advance. Simply drop in on Monday, September 12th, from 2:00 pm to 4:30 pm at the Bank of America Career Services Building. Bring a copy of your resume. ",
        "Hey readers, join us for a discussion and review of 'Her fearful Symmetry' by Audrey Niffenegar on Saturday, Feb 23rd at 11:30am at Jo's house."]

def bot_create():
    import eventbot as eb
    eb.main()
    import event_category as ec

def main(): 
    import event_category as ec
    c = []
    for i in Events:
        k =  ec.mm(i)
        c.append(k)

    result = [0]*len(c)
    for i in range(len(result)): 
        result[i] = [Events[i],c[i]]


    return result







