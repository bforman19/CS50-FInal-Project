from flask import Blueprint, Flask, redirect, render_template, flash, request, redirect, url_for
import os
import random

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")

@auth.route('/calc', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':

        image_file= url_for('static', filename='pictures/Unknown.png')
        x= "hello"
        
        warm_shooting = [{"url": "https://www.youtube.com/embed/tZocxBsONqY?start=120&end=128", "title": "Spin and Fire", "description": "Go 3 yards away from the goal on the wing, and begin with your back to the net. With a ball in your stick outstretched, swing your inside leg towards the goal and shoot the ball.", "reps": "12 each side"},
        {"url": "https://www.youtube.com/embed/tZocxBsONqY?start=183&end=199", "title": "Need to fix time", "description": "Go 3 yards away from the goal on the wing, and pop away from the net, taking three steps away from the net. On your last step load your back foot, and then explode into a step down shot.", "reps": "12 each side"},
        {"url": "https://www.youtube.com/embed/lJk79OHBRRY?start=183&end=199", "title": "Knee Shots", "description": "Go five yards away from the net, and kneel with your body facing the goal. Load your stick back, and release, trying to generate as much power as possible without worrying about accuracy.", "reps": "12 each side."},
        {"url": "https://www.youtube.com/embed/nJeWuDnikww?start=220&end=226", "title": "On the Run Warmups", "description": "Go 5 yards away from the goal on the wing, and lightly run towards the middle, taking an on the run shot. Goal is to hit offside low", "reps": "10 each side"}]

        
        wall_ball = [{"url": "https://www.youtube.com/embed/jCP5ze6OyKw?start=51&end=58", "title": "Overhand Wall Ball", "description": "With an overhand release, pass the ball against the wall, trying to aim for the same spot every time.", "reps": "50 each side"},
            {"url": "https://www.youtube.com/embed/jCP5ze6OyKw?start=98&end=105", "title": "Across Your body", "description": "With an overhand release, pass the ball against the wall. Try to aim so that the ball will cross over to your other hand, so that way it will make it harder for you to catch.", "reps": "50 each side"},
           
            {"url": "https://www.youtube.com/embed/jCP5ze6OyKw?start=135&end=142", "title": "One Hand Catches", "description": "With an overhand release, pass the ball against the wall, trying to aim so that the ball goes across your body. Then, instead of catching it two hands, catch with one.", "reps": "50 each side"},
          
            {"url": "https://www.youtube.com/embed/jCP5ze6OyKw?start=160&end=167", "title": "BTB Throws", "description": "Bring the stick behind your head, and release BTB, or behind the back, snapping your thumb towards your ear.", "reps": "50 each side"},
         
            {"url": "https://www.youtube.com/embed/jCP5ze6OyKw?start=227&end=235", "title": "Quicksticks", "description": "With your hands chocked up on the stick a little, release the ball overhand but instead of cradling when you catch, go right into your next throw.", "reps": "50 each side"},
          
            {"url": "https://www.youtube.com/embed/jCP5ze6OyKw?start=267&end=275", "title": "Switch Quicksticks", "description": "With your hands chocked up on the stick a little, release the ball overhand but instead of cradling when you catch, go right into your next throw. With switch quicksticks, pass the ball to the opposite side of your body that it was previously on.", "reps": "50 each side"},
         
            {"url": "https://www.youtube.com/embed/jCP5ze6OyKw?start=300&end=310", "title": "Pass with a fake", "description": "With an overhand release, pass the ball against the wall, trying to aim for the same spot every time. When you catch, give a fake to the wall, reload, then release the ball again.", "reps": "50 each side"},
            
            {"url": "https://www.youtube.com/embed/jCP5ze6OyKw?start=334&end=340", "title": "Sidearm release drill", "description": "With a sidearm release, pass the ball against the wall, trying to aim for the same spot every time.", "reps": "50 each side"},

            {"url": "https://www.youtube.com/embed/fLQhNF0nHaU?start=59&end=64", "title": "Catch and Split", "description": "With a overhand release, pass the ball against the wall. Once you catch the ball, switch hands. Then repeat this process on the other hand", "reps": "50 each side"},

            {"url": "https://www.youtube.com/embed/fLQhNF0nHaU?start=200&end=210", "title": "Catch and Switch", "description": "With a overhand release, pass the ball against the wall, and as you catch, switch hands. Then repeat this process on the other hand", "reps": "50 each side"}]

            
        

        no_ball = [{"url": "https://www.youtube.com/embed/CSnJYMIkhFY?start=34&end=42", "title": "Three Cone Dodging", "description": "Put three cones zizgaged 10 yards away from the net. Explode out of a dodge from the farthest cone, and split dodge your way through the cones. After the last cone, take an on the run shot aiming for far pipe.", "reps": "5 each side"},
        {"url": "https://www.youtube.com/embed/lJiBEVuFOgw?start=70&end=93", "title": "No stick Cradling", "description": "Without a stick, take a ball and begin to mimick the cradling movement with the ball in your hands. After a couple sets you begin to move as you perform this movement.", "reps": "30s each side for 4 sets"},
        {"url": "https://www.youtube.com/embed/SGSYx_hbTS0?start=138&end=143", "title": "Power Shooting", "description": "With your body facing sidways, load your stick as far back as you can away from the net. With your legs planted, and your weight slightly shifted onto your back foot, explode towards the net and rotate your core along with your arms. Focus more on generating power versus accuracy.", "reps": "12 each side"},
        {"url": "https://www.youtube.com/embed/MsnwIXJXllo?start=126&end=140", "title": "ZigZag Drill", "description": "Can be performed with or without resistance band. Set out 6 cones in a zigzag format. Starting from one end of the cone, split your way through the barriers as quickly as possible, taking little jab steps when you reach each cone.", "reps": "10 reps"},
        {"url": "https://www.youtube.com/embed/1P_4Fx467PU?start=12&end=44", "title": "Z Drill", "description": "with 8 cones zigzaged in front of you, begin chopping your feet as you aproach the first cone. With the stick in either hand, jab your foot at the cone and fake your stick in the direction of the cone. Afterwards, go back to chopping your feet and repeat the process at each cone.", "reps": "10 reps"},
        {"url": "https://www.youtube.com/embed/YWRRQAJN9hQ?start=137&end=147", "title": "Swat the Fly", "description": "Can be performed with or without a feeder. Standing 2 yards away from the net, with a ball in your stick, extend outside hand out with your feet facing sideways. Load your back foot and snap your wrist towards the goal, shooting as hard as you can with 1 hand. Focus more on power and less on accuracy.", "reps": "10 reps"},
        {"url": "https://www.youtube.com/embed/qtwKIxyOdGk?start=186&end=196", "title": "Ground Ball", "description": "Can be performed with or without a helper. Standing a few yards away from a ball, aproach the ball and get your knuckles to the ground as you scoop through the ball and cradle once you have it in your stick.", "reps": "20 reps each hand"},
        {"url": "https://www.youtube.com/embed/S7xJti9m1uw?start=73&end=90", "title": "4 Way Sprint", "description": "Set up Four Cones 8 yards apart. Sprint from one to the next, creating a square with your movement. Try to hug the cones as much as possible.", "reps": "6 reps each direction."},
        {"url": "https://www.youtube.com/embed/S7xJti9m1uw?start=110&end=120", "title": "Backpedal, shuffle, sprint.", "description": "Set up Four Cones 8 yards apart. Backpadel from the first to the second, side shuffel from the second to the third, and sprint from the 3rd to the 4th.", "reps": "6 reps each direction."},
        {"url": "https://www.youtube.com/embed/S7xJti9m1uw?start=170&end=180", "title": "X Drill", "description": "Set up Four Cones 8 yards apart in a square. Try to make an X with your movement. Sprint from one cone straight ahead. Then sprint diagonally across. Then Sprint foward. Then sprint diagonally, and you should end up where you started.", "reps": "6 reps each direction."},
        {"url": "https://www.youtube.com/embed/S7xJti9m1uw?start=184&end=194", "title": "Pro Agility Shuffel", "description": "Set up 3 Cones 5 yards apart in a straight line. From a few yards away from the middle cone, jog towards the center. Then, sprint, when you reach the cone, sprint in one direction, touch the cone, sprint back 10 yards, touch that cone, then finish in the middle.", "reps": "6 reps each direction."},
        {"url": "https://www.youtube.com/embed/qtwKIxyOdGk?start=50&end=57", "title": "Ground Ball No Stick", "description": "Can be performed with or without a helper. Standing a few yards away from a ball, aproach the ball and get your knuckles to the ground as you mimick a ground ball. Pick up the ball with both hands and explode through the ball as you regain your posture.", "reps": "30 reps"}]

        
        little_ball = [{"url": "https://www.youtube.com/embed/DsH3Ym_7e8k?start=124&end=134", "title": "Low Angle Shooting", "description": "with balls at Gle, positition your body upfield. Make one or two fakes towards the net and finish in a corner.", "reps": "8 each side"},
                {"url": "https://www.youtube.com/embed/ocHH2x9xlUI?start=257&end=266", "title": "Split to Face Dodge", "description": "Starting at X, split dodge upfield and make your way a few yards past GLE. Then bounce out as if you are going to pass, and face dodge back towards the net. Shoot towards the net with your stick protected.", "reps": "8 each side"},
                {"url": "https://www.youtube.com/embed/lxAQwwTIYMI?start=42&end=50", "title": "One Handed BTBs", "description": "With both knees down and chest up, extend your stick with your outside arm. Then snap your thumb to your ear and release the ball behind your head, or BTB.", "reps": "10 each side"},
                {"url": "https://www.youtube.com/embed/lxAQwwTIYMI?start=155&end=202", "title": "Two Handed BTBs", "description": "With both knees down and chest up, extend your stick with both arms. Then snap your thumb to your ear and release the ball behind your head, or BTB.", "reps": "10 each side"},
                {"url": "https://www.youtube.com/embed/ezr2-t-O3mA?start=36&end=60", "title": "Inside Roll", "description": "Starting at GLE, 4 yards away from the goal, aproach topside with one hand on the stick. Then, 5 yards upfield, inside roll back towards the net and finish with your stick protected.", "reps": "10 each side"},
                {"url": "https://www.youtube.com/embed/ezr2-t-O3mA?start=60&end=76", "title": "Question Mark", "description": "Starting at GLE, 4 yards away from the goal, aproach topside with one hand on the stick. Then, 5 yards upfield, punch your stick to the outside and get both hands on the stick as you pivoting to the sideline. Flip your hips back towards the goal, and shoot.", "reps": "10 each side"},
                {"url": "https://www.youtube.com/embed/nJeWuDnikww?start=342&end=262", "title": "Alley dodge into tight finish", "description": "Go 10-12 yards away from the goal on the wing, and dodge towards X. Instead of going behind the goal, come across it and finish in front.", "reps": "8 each side"},
                {"url": "https://www.youtube.com/embed/nJ7_LepBOpU?start=50&end=60", "title": "Turn and bury", "description": "Starting at GLE, 4 yards away from the goal, aproach topside with one hand on the stick. One or two yards upfield, turn your hips and bury the ball. Make sure to look where you shooting so you can place the ball more accuractly.", "reps": "12 each side"},
                {"url": "https://www.youtube.com/embed/t18hqY74HgU?start=0&end=10", "title": "Zig Zag from X", "description": "Set out three cones behind the goal in a zig zag format. Starting at X, 10 yards behind the goal, aproach the lowest cone. When you get there, roll back towards the middle and repeat this process with cones 2 and 3. After the 3rd cone, continue past the middle and curl around the crease going into a topside finish.", "reps": "6 each side"},
                {"url": "https://www.youtube.com/embed/ezr2-t-O3mA?start=103&end=120", "title": "Rocker Step", "description": "Starting at GLE, 4 yards away from the goal, aproach topside with one hand on the stick. Then, 5 yards upfield, chop your feet and fake your hips as if you were gonna do an inside roll. Instead, continue upfield and curl into your shot.", "reps": "10 each side"}]

        
        
        shooting = [{"url": "https://www.youtube.com/embed/6B9y-aQa0Hs?start=40&end=50", "title": "Step Downs", "description": "Go 8 yards away from the goal on the wing, and put down a cone. If by yourself, start with a ball, take two shuffles back, and redistribute your weight into a shot. With a partner shuffle back without ball and get a pass into your shot.", "reps": "8 each side"}, 
        {"url": "https://www.youtube.com/embed/6B9y-aQa0Hs?start=125&end=137", "title": "Step Split Hitches", "description": "Start at the top edges, and go into a 3 shot cycle. 1st shot is a step down, second shot is a topside hitch, and a third is a split down the alley.", "reps": "3 cycles each side"}, 
        {"url": "https://www.youtube.com/embed/TDqpPM_dx88?start=158&end=168", "title": "Split into Crow Hop", "description": "Start at the top edges, switch hands, and try to take a big crow hop into a shot. Aim low corners. Switch the side of the field for your other hand.", "reps": "10 each side"}, 
        {"url": "https://www.youtube.com/embed/TDqpPM_dx88?start=195&end=206", "title": "Down the Alleys", "description": "Start at the top. While keeping the stick in your outside hand, and explode down the alley while taking an on the run shot. Try to aim opposite pipe.", "reps": "8 each side"}, 
        {"url": "https://www.youtube.com/embed/TDqpPM_dx88?start=232&end=240", "title": "Split Middles", "description": "Start at the top edges, split to the middle, and take an on the run shot. Try to aim opposite pipe.", "reps": "8 each side"},
        {"url": "https://www.youtube.com/embed/tZocxBsONqY?start=244&end=252", "title": "Layup Shooting", "description": "Go 8 yards in front of the goal, and start with your feet planted towards the net. With just your outside hand on the stick, explode towards the wing and take a shot on the run.", "reps": "10 each side"},
        {"url": "https://www.youtube.com/embed/tZocxBsONqY?start=330&end=338", "title": "Hitch Shooting", "description": "Go to the wing, take a hitch, and either take an on the run shot topside or a stepdown shot.", "reps": "8 each side"},
        {"url": "https://www.youtube.com/embed/tZocxBsONqY?start=340&end=345", "title": "Face Dodges", "description": "Go to the wing, take a crow hop into a face dodge, and finish running towards the goal. Remember to keep your stick protected as you run.", "reps": "8 each side"},
        {"url": "https://www.youtube.com/embed/tZocxBsONqY?start=360&end=366", "title": "Hitch andn Split", "description": "Go to the wing, take a crow hop into a hitch, take one step topside, and plant your feet. Then, split back down the alley and take an on the run shot", "reps": "8 each side"},
        {"url": "https://www.youtube.com/embed/tZocxBsONqY?start=404&end=410", "title": "Game Splits", "description": "Similate a game dodge with a split from the top of the box, down the alley into your shot. You can also similate a potential slide with a bounce out, into a redodge.", "reps": "5 each side"},
        {"url": "https://www.youtube.com/embed/o1SBiX23JYo?start=150&end=160", "title": "Up the Hash Shooting", "description": "Can be done with or without a feeder. Start around gle, and with yoru stick outstretched towards the sideline, run up the hash and shoot as you run upfeild", "reps": "10 each side" },
        {"url": "https://www.youtube.com/embed/ocHH2x9xlUI?start=236&end=242", "title": "Split to Hitch", "description": "Starting at X, split dodge upfield and make your way a few yards past GLE. Then bounce out as if you are going to pass, and hitch. Step a few more feet upfield and take a step down shot.", "reps": "8 each side"},
        {"url": "https://www.youtube.com/embed/nJeWuDnikww?start=277&end=284", "title": "Front and Center Step Downs", "description": "Go 10-12 yards away from the goal straight in front, and take a step down shot. Pick one corner and try to aim all your shots in that vicinity.", "reps": "10 each side"},
        {"url": "https://www.youtube.com/embed/TDqpPM_dx88?start=245&end=255", "title": "finishers", "description": "Start a few feet in front of the net. Toss up a ball, make at least 2 fakes, and finish in a corner. Try to vary your fakes and which corner you shoot into.", "reps": "8 each side"}]

        wall=request.form.get("wall")
        net=request.form.get("net")
        time=request.form.get("time")
        balls=request.form.get("balls")
        
        choose=[]
        workout=[]
        warm_up=[]
        taken_numbers=[]

        numbers=2
        
        total_numbers=0
        total_numbers2=0

        
        if (net=="net"):
            net_true=True
            for i in warm_shooting:
                choose.append(warm_shooting[i])
                total_numbers+=1
        
        if (wall=="wall"):
            wall_true=True
            for i in wall_ball:
                choose.append(wall_ball[i])
                total_numbers+=1

        if (net=="net"):
            for i in little_ball:
                choose.append(little_ball[i])
            if balls=="10-20" or balls=="20+":
                for i in shooting:
                    choose.append(shooting[i])
                    total_numbers+=1
        for i in no_ball:
            choose.append(no_ball[i])
            total_numbers+=1
        
        
        if (time=="30min"):
            numbers=numbers*3
        if (time=="60min"):
            numbers=numbers*5
        if (time=="90min"):
            numbers=numbers*7
        if(time=="120min"):
            numbers=numbers*10
    
    if net=="net" or wall=="wall":
        for i in range(3):
            random_number=random.randint(0,(total_numbers2-1))
            while random_number in taken_numbers:
                random_number=random.randint(0,(total_numbers2-1))
            warm_up.append(choose[random_number])
            taken_numbers.append(random_number)
    else:
        for i in range(3):
            random_number=random.randint(0, len(no_ball))
            while random_number in taken_numbers:
                random_number=random.randint(0, len(no_ball))
            warm_up.append(no_ball[random_number])
            taken_numbers.append(random_number)


        
    for i in range(numbers):
        random_number=random.randint(0,total_numbers)
        while random_number in taken_numbers:
            random_number=random.randint(0,total_numbers)
        workout.append(choose[random_number])
        taken_numbers.append(random_number)



            

        
        return render_template("calculated2.html", shooting=shooting)
    if (request.method == 'GET'):
        return render_template("calc.html", x="hello")
    