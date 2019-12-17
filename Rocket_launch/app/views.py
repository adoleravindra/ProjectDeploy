
"""from django.shortcuts import render
import time
import krpc
# Create your views here.
def launch_rocket(request):
    try:
        connection = krpc.connect()
        vessel = connection.space_center.active_vessel
        # Countdown Sequence
        countdown = ["5", "4", "3", "2", "1", "Lift Off"]
        for i in countdown:
            print(i)
            time.sleep(1)
        vessel.control.throttle = 1
        vessel.control.activate_next_stage()  # First stage
        # Flight State
        accentPhace = True
        cruisePhase = False
        insertionPhase = False

        while accentPhace or cruisePhase or insertionPhase:
            altitude = vessel.flight().mean_altitude
            heading = vessel.flight().heading
            if accentPhace:
                targetPitch = 90 * ((50000 - altitude) / 50000)
                pitchDiff = vessel.flight().pitch - targetPitch

                # Heading Control
                if heading < 180:
                    vessel.control.yaw = (pitchDiff / 90)

                else:
                    vessel.control.yaw = 0.5

                # Staging
                if vessel.thrust == 0.0:
                    vessel.control.activate_next_stage()  # Second Stage

                # Main Engine Cut Off
                if vessel.orbit.apoapsis > 690000:
                    vessel.control.throttle = 0
                    time.sleep(0.5)
                    vessel.control.activate_next_stage()

                    vessel.control.sas = True
                    time.sleep(0.1)
                    vessel.control.sas_mode = connection.space_center.SASMode.prograde

                    accentPhace = False
                    cruisePhase = True

            elif cruisePhase:
                if altitude > 80000:
                    cruisePhase = False
                    insertionPhase = True
                    vessel.control.sas = False
                    vessel.control.throttle = 1


            elif insertionPhase:
                targetPitch = 0
                pitchDiff = vessel.flight().pitch - targetPitch

                # Heading Control
                if heading < 180:
                    vessel.control.yaw = (pitchDiff / 90)
                    if vessel.flight().pitch < 1 and vessel.flight().pitch > -1:
                        vessel.control.sas = True
                    else:
                        vessel.control.sas = False
                else:
                    vessel.control.yaw = 0.5

        return render(request, "index.html", {"msg": "Rocket Launch Successfull"})

    except:
        render(request,"index.html",{"data":"Start Game First"})
"""
