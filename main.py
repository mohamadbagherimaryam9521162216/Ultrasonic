from typing import List

import RPi.GPIO as GPIO
import time
import pandas as pd


# Data list
row_list=[]
header_list: List[str]=["num", "Measured_dis", "Real_dis","angle"]
data={'Measured_dis':[0],'Real_dis':[0],'angle':[0],'error':[0]}
record_list= pd.DataFrame(data)


#Motor's Pins
in1 = 17
in2 = 18
in3 = 27
in4 = 22

#Sensor's Pins
TRIG = 5
ECHO = 7

#Motor's Variables
step_sleep = 0.0015
step_count = 4096  # 5.625*(1/64) per step, 4096 steps is 360°
direction = False  # True for clockwise, False for counter-clockwise
step_sequence = [[1, 0, 0, 1],
                 [1, 0, 0, 0],
                 [1, 1, 0, 0],
                 [0, 1, 0, 0],
                 [0, 1, 1, 0],
                 [0, 0, 1, 0],
                 [0, 0, 1, 1],
                 [0, 0, 0, 1]]

# Sensor's Variables

# setting up Board
GPIO.setmode(GPIO.BCM)

# setting up Motor
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)

# setting up Sensor
GPIO.setup(TRIG , GPIO.OUT)
GPIO.setup(ECHO , GPIO.IN)

# initializing MOTOR
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)

# initializing Sensor
GPIO.output(TRIG, False)
time.sleep(2)
GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)


motor_pins = [in1, in2, in3, in4]
motor_step_counter = 0;


def cleanup():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    GPIO.cleanup()


# the meat
while True:
    angle=0
    i = 0
    angle=0
    for i in range(step_count):

        #To change direcetion after 360 degress
        if i == step_count-1:
            record_list=record_list.to_csv('data.csv')
        for pin in range(0, len(motor_pins)):
            GPIO.output(motor_pins[pin], step_sequence[motor_step_counter][pin])
        if direction == True:
            motor_step_counter = (motor_step_counter - 1) % 8
        elif direction == False:
            motor_step_counter = (motor_step_counter + 1) % 8
        if i % 64==0 :
            angle=angle+5.6
            GPIO.output(TRIG, False)
            time.sleep(2)
            GPIO.output(TRIG, True)
            time.sleep(0.00001)
            GPIO.output(TRIG, False)
            while GPIO.input(ECHO)==0:
               pulse_start=time.time()
            while GPIO.input(ECHO)==1:
               pulse_end = time.time()
            pulse_destination =   pulse_end -   pulse_start;
            distance= pulse_destination *17150
            distance=round(distance,2)
            print ("Distance", distance,"cm")
            real_distance =input("Enter real distance:")
            error=float(real_distance)-distance
            error=abs(error)
            record={'Measured_dis':distance,'Real_dis':real_distance,'angle':angle,'error':error}
            record_list=record_list.append(record,ignore_index=True)
        time.sleep(step_sleep)



GPIO.cleanup()

