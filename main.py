"""
# main.py

Main file for the OBD interface.

## Most important methods:

    - car.DTCs.read()
    - car.DTCs.count()
    - car.DTCs.clear()

    - car.MonitorResults.catalyst_bank1()
    - car.MonitorResults.general_misfire()
    - car.MonitorResults.O2Sensor_bank1sensor1()
    - car.MonitorResults.O2Sensor_bank1sensor2()
    - car.MonitorResults.O2SensorHeater_bank1sensor1()
    - car.MonitorResults.O2SensorHeater_bank1sensor2()

    - car.connect()
    - car.disconnect()
    - car.get_absolute_engine_load()
    - car.get_catalyst_temperature_Bank1Sensor1()
    - car.get_catalyst_temperature_Bank1Sensor2()
    - car.get_coolant_temperature()
    - car.get_engine_load()
    - car.get_engine_RPM()
    - car.get_fuel_level()
    - car.get_fuel_rail_pressure()
    - car.get_intake_manifold_pressure()
    - car.get_O2_Bank1Sensor2_voltage()
    - car.get_O2_sensor1_WR_lambda_current()
    - car.get_relative_throttle_position()
    - car.get_absolute_throttle_position()
    - car.get_short_term_fuel_trim_Bank1()
    - car.get_short_term_O2_trim_Bank1()
    - car.get_speed()
    - car.get_timing_advance()
    
"""
import socket
import datetime
import pandas as pd
from github import Github
from OBDModule.OBD import Sonata


def is_connected_to_network():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False


# Github access token
# ACCESS_TOKEN = None
# if is_connected_to_network():
#     ACCESS_TOKEN = "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"
#     g = Github(ACCESS_TOKEN)


car = Sonata()
car.connect()


COLUMNS = [
    'timestamp',
    'speed',
    'engine_RPM',
    'engine_load',
    'absolute_engine_load',
    'relative_throttle_position',
    'absolute_throttle_position',
    'timing_advance'
    'fuel_rail_pressure',
    'intake_manifold_pressure',
    'coolant_temperature',
    'fuel_level',
    'catalyst_temperature_Bank1Sensor1',
    'catalyst_temperature_Bank1Sensor2',
    'O2_Bank1Sensor2_voltage',
    'O2_sensor1_WR_lambda_current',
    'short_term_fuel_trim_Bank1',
    'short_term_O2_trim_Bank1',
]

speed = 0
engine_RPM = 0
engine_load = 0
absolute_engine_load = 0
relative_throttle_position = 0
absolute_throttle_position = 0
timing_advance = 0
fuel_rail_pressure = 0
intake_manifold_pressure = 0
coolant_temperature = 0
fuel_level = 0
catalyst_temperature_Bank1Sensor1 = 0
catalyst_temperature_Bank1Sensor2 = 0
O2_Bank1Sensor2_voltage = 0
O2_sensor1_WR_lambda_current = 0
short_term_fuel_trim_Bank1 = 0
short_term_O2_trim_Bank1 = 0




def get_speed() -> None:
    """
    Get the speed of the car.
    """
    global speed
    speed = car.get_speed()


def get_engine_RPM() -> None:
    """
    Get the engine RPM of the car.
    """
    global engine_RPM
    engine_RPM = car.get_engine_RPM()
    

def get_engine_load() -> None:
    """
    Get the engine load of the car.
    """
    global engine_load
    engine_load = car.get_engine_load()


def get_absolute_engine_load() -> None:
    """
    Get the absolute engine load of the car.
    """
    global absolute_engine_load
    absolute_engine_load = car.get_absolute_engine_load()


def get_relative_throttle_position() -> None:
    """
    Get the relative throttle position of the car.
    """
    global relative_throttle_position
    relative_throttle_position = car.get_relative_throttle_position()


def get_absolute_throttle_position() -> None:
    """
    Get the absolute throttle position of the car.
    """
    global absolute_throttle_position
    absolute_throttle_position = car.get_absolute_throttle_position()


def get_timing_advance() -> None:
    """
    Get the timing advance of the car.
    """
    global timing_advance
    timing_advance = car.get_timing_advance()


def get_fuel_rail_pressure() -> None:
    """
    Get the fuel rail pressure of the car.
    """
    global fuel_rail_pressure
    fuel_rail_pressure = car.get_fuel_rail_pressure()


def get_intake_manifold_pressure() -> None:
    """
    Get the intake manifold pressure of the car.
    """
    global intake_manifold_pressure
    intake_manifold_pressure = car.get_intake_manifold_pressure()


def get_coolant_temperature() -> None:
    """
    Get the coolant temperature of the car.
    """
    global coolant_temperature
    coolant_temperature = car.get_coolant_temperature()


def get_fuel_level() -> None:
    """
    Get the fuel level of the car.
    """
    global fuel_level
    fuel_level = car.get_fuel_level()


def get_catalyst_temperature_Bank1Sensor1() -> None:
    """
    Get the catalyst temperature of the car.
    """
    global catalyst_temperature_Bank1Sensor1
    catalyst_temperature_Bank1Sensor1 = car.get_catalyst_temperature_Bank1Sensor1()


def get_catalyst_temperature_Bank1Sensor2() -> None:
    """
    Get the catalyst temperature of the car.
    """
    global catalyst_temperature_Bank1Sensor2
    catalyst_temperature_Bank1Sensor2 = car.get_catalyst_temperature_Bank1Sensor2()


def get_O2_Bank1Sensor2_voltage() -> None:
    """
    Get the O2 sensor voltage of the car.
    """
    global O2_Bank1Sensor2_voltage
    O2_Bank1Sensor2_voltage = car.get_O2_Bank1Sensor2_voltage()


def get_O2_sensor1_WR_lambda_current() -> None:
    """
    Get the O2 sensor current of the car.
    """
    global O2_sensor1_WR_lambda_current
    O2_sensor1_WR_lambda_current = car.get_O2_sensor1_WR_lambda_current()


def get_short_term_fuel_trim_Bank1() -> None:
    """
    Get the short term fuel trim of the car.
    """
    global short_term_fuel_trim_Bank1
    short_term_fuel_trim_Bank1 = car.get_short_term_fuel_trim_Bank1()


def get_short_term_O2_trim_Bank1() -> None:
    """
    Get the short term O2 trim of the car.
    """
    global short_term_O2_trim_Bank1
    short_term_O2_trim_Bank1 = car.get_short_term_O2_trim_Bank1()








start = datetime.datetime.now()
data = pd.DataFrame(columns=[COLUMNS])


FILENAME = f"{start.strftime('%Y-%m-%d_%H:%M:%S')}.txt"
with open(FILENAME, 'w') as f:
    f.write("timestamp,speed,rpm,calculated_engine_load,absolute_engine_load,relative_throttle_pos,absolute_throttle_pos,timing_advance,fuel_rail_pressure,intake_manifold_pressure,coolant_temperature,fuel_level,catalyst_temperature_bank1sensor1,catalyst_temperature_bank1sensor2,o2_bank1sensor2_voltage,o2_bank1sensor1_wr_lambda_current,short_term_fuel_trim_bank1,short_term_o2_trim_bank1\n")

file = open(FILENAME, 'a')



# # create a thread for each function
# threads: list[threading.Thread] = []
# threads.append(threading.Thread(target=get_speed), daemon=True)
# threads.append(threading.Thread(target=get_engine_RPM), daemon=True)
# threads.append(threading.Thread(target=get_engine_load), daemon=True)
# threads.append(threading.Thread(target=get_absolute_engine_load), daemon=True)
# threads.append(threading.Thread(target=get_relative_throttle_position), daemon=True)
# threads.append(threading.Thread(target=get_absolute_throttle_position), daemon=True)
# threads.append(threading.Thread(target=get_timing_advance), daemon=True)
# threads.append(threading.Thread(target=get_fuel_rail_pressure), daemon=True)
# threads.append(threading.Thread(target=get_intake_manifold_pressure), daemon=True)
# threads.append(threading.Thread(target=get_coolant_temperature), daemon=True)
# threads.append(threading.Thread(target=get_fuel_level), daemon=True)
# threads.append(threading.Thread(target=get_catalyst_temperature_Bank1Sensor1), daemon=True)
# threads.append(threading.Thread(target=get_catalyst_temperature_Bank1Sensor2), daemon=True)
# threads.append(threading.Thread(target=get_O2_Bank1Sensor2_voltage), daemon=True)
# threads.append(threading.Thread(target=get_O2_sensor1_WR_lambda_current), daemon=True)
# threads.append(threading.Thread(target=get_short_term_fuel_trim_Bank1), daemon=True)
# threads.append(threading.Thread(target=get_short_term_O2_trim_Bank1), daemon=True)


# # start all threads
# for thread in threads:
#     thread.start()


# # wait for all threads to finish
# for thread in threads:
#     thread.join()



def update() -> None:
    """
    Updates all columns in the dataframe by adding a new row of fresh data.
    """
    file.write(str((datetime.datetime.now() -start).total_seconds()) + ',')
    file.write(str(car.get_speed()) + ',')
    file.write(str(car.get_engine_RPM()) + ',')
    file.write(str(car.get_engine_load()) + ',')
    file.write(str(car.get_absolute_engine_load()) + ',')
    file.write(str(car.get_relative_throttle_position()) + ',')
    file.write(str(car.get_absolute_throttle_position()) + ',')
    file.write(str(car.get_timing_advance()) + ',')
    file.write(str(car.get_fuel_rail_pressure()) + ',')
    file.write(str(car.get_intake_manifold_pressure()) + ',')
    file.write(str(car.get_coolant_temperature()) + ',')
    file.write(str(car.get_fuel_level()) + ',')
    file.write(str(car.get_catalyst_temperature_Bank1Sensor1()) + ',')
    file.write(str(car.get_catalyst_temperature_Bank1Sensor2()) + ',')
    file.write(str(car.get_O2_Bank1Sensor2_voltage()) + ',')
    file.write(str(car.get_O2_sensor1_WR_lambda_current()) + ',')
    file.write(str(car.get_short_term_fuel_trim_Bank1()) + ',')
    file.write(str(car.get_short_term_O2_trim_Bank1()) + '\n')
    # global data
    # data.loc[len(data)] = [
    #     (datetime.datetime.now() -start).total_seconds(),
    #     car.get_speed(),
    #     car.get_engine_RPM(),
    #     car.get_engine_load(),
    #     car.get_absolute_engine_load(),
    #     car.get_relative_throttle_position(),
    #     car.get_absolute_throttle_position(),
    #     car.get_timing_advance(),
    #     car.get_fuel_rail_pressure(),
    #     car.get_intake_manifold_pressure(),
    #     car.get_coolant_temperature(),
    #     car.get_fuel_level(),
    #     car.get_catalyst_temperature_Bank1Sensor1(),
    #     car.get_catalyst_temperature_Bank1Sensor2(),
    #     car.get_O2_Bank1Sensor2_voltage(),
    #     car.get_O2_sensor1_WR_lambda_current(),
    #     car.get_short_term_fuel_trim_Bank1(),
    #     car.get_short_term_O2_trim_Bank1(),
    # ]



def save() -> None:
    """
    Saves the dataframe to a CSV file.
    """
    global data
    data.to_csv('data.csv', index=False)



def main() -> None:
    """
    Main function for the OBD interface.
    """
    global data
    while True:
        try:
            update()
            # time.sleep(0.05)        # 20 Hz
        except KeyboardInterrupt:
            save()
            file.close()
            car.disconnect()
            if is_connected_to_network():
                # ACCESS_TOKEN = "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"     # makaufmanUI
                ACCESS_TOKEN = "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"       # ranjeetpajeet
                g = Github(ACCESS_TOKEN)
                repo = g.get_repo('ranjeetpajeet/pi-obd')
                with open(FILENAME, 'r') as f:
                    data = f.read()
                repo.create_file(f"data/{FILENAME}", "new data", data)
            break



if __name__ == '__main__':
    main()
