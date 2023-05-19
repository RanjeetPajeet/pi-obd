"""
# OBDAsync.py


"""
import obd
import pint
import time
import asyncio
import numpy as np
import pandas as pd
from datetime import datetime
from obd.utils import BitArray
from obd.OBDResponse import Status as OBDStatusResponse

from OBDModule.dtcs import DTCs
from OBDModule.mids import MIDs
from OBDModule.monitor_results import MonitorResults







class SonataAsync:
    def __init__(self):
        self._connection = None
        self._commands = [
            obd.commands.ABSOLUTE_LOAD,                 # Absolute load value
            obd.commands.ACCELERATOR_POS_D,             # Accelerator pedal position D
            obd.commands.ACCELERATOR_POS_E,             # Accelerator pedal position E
            obd.commands.AMBIANT_AIR_TEMP,              # Ambient air temperature
            obd.commands.BAROMETRIC_PRESSURE,           # Barometric Pressure
            obd.commands.CATALYST_TEMP_B1S1,            # Catalyst Temperature: Bank 1 - Sensor 1
            obd.commands.CATALYST_TEMP_B1S2,            # Catalyst Temperature: Bank 1 - Sensor 2
            obd.commands.COMMANDED_EQUIV_RATIO,         # Commanded equivalence ratio 
            obd.commands.CONTROL_MODULE_VOLTAGE,        # Control module voltage      
            obd.commands.COOLANT_TEMP,                  # Engine Coolant Temperature  
            obd.commands.DISTANCE_SINCE_DTC_CLEAR,      # Distance traveled since codes cleared  
            obd.commands.DISTANCE_W_MIL,                # Distance Traveled with MIL on          
            obd.commands.ENGINE_LOAD,                   # Calculated Engine Load      
            obd.commands.EVAPORATIVE_PURGE,             # Commanded Evaporative Purge 
            obd.commands.EVAP_VAPOR_PRESSURE,           # Evaporative system vapor pressure      
            obd.commands.FUEL_LEVEL,                    # Fuel Level Input            
            obd.commands.FUEL_RAIL_PRESSURE_ABS,        # Fuel rail pressure (absolute)          
            obd.commands.FUEL_STATUS,                   # Fuel System Status          
            obd.commands.INTAKE_PRESSURE,               # Intake Manifold Pressure    
            obd.commands.INTAKE_TEMP,                   # Intake Air Temp             
            obd.commands.LONG_FUEL_TRIM_1,              # Long Term Fuel Trim - Bank 1
            obd.commands.LONG_O2_TRIM_B1,               # Long term secondary O2 trim - Bank 1   
            obd.commands.O2_B1S2,                       # O2: Bank 1 - Sensor 2 Voltage          
            obd.commands.O2_S1_WR_CURRENT,              # O2 Sensor 1 WR Lambda Current          
            obd.commands.O2_SENSORS,                    # O2 Sensors Present          
            obd.commands.OBD_COMPLIANCE,                # OBD Standards Compliance    
            obd.commands.PIDS_A,                        # Supported PIDs [01-20]      
            obd.commands.PIDS_B,                        # Supported PIDs [21-40]      
            obd.commands.PIDS_C,                        # Supported PIDs [41-60]      
            obd.commands.RELATIVE_THROTTLE_POS,         # Relative throttle position  
            obd.commands.RPM,                           # Engine RPM                  
            obd.commands.RUN_TIME,                      # Engine Run Time             
            obd.commands.RUN_TIME_MIL,                  # Time run with MIL on        
            obd.commands.SHORT_FUEL_TRIM_1,             # Short Term Fuel Trim - Bank 1          
            obd.commands.SHORT_O2_TRIM_B1,              # Short term secondary O2 trim - Bank 1  
            obd.commands.SPEED,                         # Vehicle Speed               
            obd.commands.STATUS,                        # Status since DTCs cleared   
            obd.commands.STATUS_DRIVE_CYCLE,            # Monitor status this drive cycle        
            obd.commands.THROTTLE_ACTUATOR,             # Commanded throttle actuator 
            obd.commands.THROTTLE_POS,                  # Throttle Position           
            obd.commands.THROTTLE_POS_B,                # Absolute throttle position B
            obd.commands.TIME_SINCE_DTC_CLEARED,        # Time since trouble codes cleared       
            obd.commands.TIMING_ADVANCE,                # Timing Advance              
            obd.commands.WARMUPS_SINCE_DTC_CLEAR,       # Number of warm-ups since codes cleared 

            obd.commands.GET_DTC,                       # Get DTCs
            obd.commands.CLEAR_DTC,                     # Clear DTCs and Freeze data
            obd.commands.GET_CURRENT_DTC,               # Get DTCs from the current/last driving cycle

            obd.commands.MIDS_A,                        # Supported MIDs [01-20]
            obd.commands.MIDS_B,                        # Supported MIDs [21-40]
            obd.commands.MIDS_C,                        # Supported MIDs [41-60]
            obd.commands.MIDS_D,                        # Supported MIDs [61-80]
            obd.commands.MIDS_E,                        # Supported MIDs [81-A0]
            obd.commands.MIDS_F,                        # Supported MIDs [A1-C0]
            obd.commands.MONITOR_CATALYST_B1,           # Catalyst Monitor Bank 1
            obd.commands.MONITOR_EVAP_020,              # EVAP Monitor (0.020)
            obd.commands.MONITOR_EVAP_040,              # EVAP Monitor (0.040)
            obd.commands.MONITOR_EVAP_090,              # EVAP Monitor (0.090)
            obd.commands.MONITOR_EVAP_150,              # EVAP Monitor (Cap Off / 0.150)
            obd.commands.MONITOR_MISFIRE_CYLINDER_1,    # Misfire Cylinder 1 Data
            obd.commands.MONITOR_MISFIRE_CYLINDER_2,    # Misfire Cylinder 2 Data
            obd.commands.MONITOR_MISFIRE_CYLINDER_3,    # Misfire Cylinder 3 Data
            obd.commands.MONITOR_MISFIRE_CYLINDER_4,    # Misfire Cylinder 4 Data
            obd.commands.MONITOR_MISFIRE_GENERAL,       # Misfire Monitor General Data
            obd.commands.MONITOR_O2_B1S1,               # O2 Sensor Monitor Bank 1 - Sensor 1
            obd.commands.MONITOR_O2_B1S2,               # O2 Sensor Monitor Bank 1 - Sensor 2
            obd.commands.MONITOR_O2_HEATER_B1S1,        # O2 Sensor Heater Monitor Bank 1 - Sensor 1
            obd.commands.MONITOR_O2_HEATER_B1S2,        # O2 Sensor Heater Monitor Bank 1 - Sensor 2
            obd.commands.MONITOR_PURGE_FLOW,            # Purge Flow Monitor
            obd.commands.MONITOR_VVT_B1,                # VVT Monitor Bank 1
        ]

        self._watched_commands = []
        
        self._DTCs = None
        self._MIDs = None
        self._MonitorResults = None
    

    def connect(self) -> None:
        """
        Initializes a connection with the vehicle's OBD system.

        Returns
        -------
        `None`
        """
        self._connection = obd.Async()
        self._DTCs = DTCs(self._connection)
        self._MIDs = MIDs(self._connection)
        self._MonitorResults = MonitorResults(self._connection)
    

    def disconnect(self) -> None:
        """
        Disconnects from the vehicle's OBD system.

        Returns
        -------
        `None`
        """
        self._connection.close()
        self._connection = None
        self._DTCs = None
        self._MIDs = None
        self._MonitorResults = None

        
    def __repr__(self) -> str:
        string = f"\n>> OBD Connection (Port {self._connection.port_name()}):\n"
        string += f" > Status: {self._connection.status()}\n"
        string += f" > Protocol: {self._connection.protocol_name()} (ID = {self._connection.protocol_id()})\n"
        self._connection.print_commands()
        string += " > Supported Commands:\n"
        for command in self._commands:
            string += f"   - {command.name}\n"
        return string
    
    def __str__(self) -> str:
        return self.__repr__()
    

    @property
    def connection(self) -> obd.OBD:
        """
        OBD Connection object.
        """
        return self._connection
    
    @property
    def commands(self) -> list[obd.OBDCommand]:
        """
        List of OBDCommand objects that are supported by the vehicle.
        """
        return self._commands
    
    @property
    def DTCs(self) -> DTCs:
        """
        Collection of methods that retrieve Diagnostic Trouble Codes (DTCs)
        and information related to DTCs from the car.
        """
        return self._DTCs
    
    @property
    def MIDs(self) -> MIDs:
        """
        Collection of 6 methods that retrieve MIDs from the car (`A`, `B, `C`, `D`, `E`, and `F`).
        """
        return self._MIDs
    
    @property
    def MonitorResults(self) -> MonitorResults:
        """
        Collection of methods that return results of various OBD monitor tests.
        """
        return self._MonitorResults
    
    @property
    def watched_commands(self) -> list[obd.OBDCommand]:
        """
        List of OBDCommand objects that are currently being watched.
        """
        return self._watched_commands
        
    

    def watch(self, commands: list[obd.OBDCommand]) -> None:
        """
        Watches the given commands and calls the callback function whenever a new response is received.

        Parameters
        ----------
        `commands` : list[obd.OBDCommand]
            List of commands to watch.

        Returns
        -------
        `None`
        """
        for command in commands:
            if command not in self._watched_commands:
                self._watched_commands.append(command)
            self._connection.watch(command)
    


    def start_watching(self) -> None:
        """
        Starts watching the commands that were previously added using the `watch` method.

        Any queries to the previously watched commands after this call will return immediately with the last known response.

        Returns
        -------
        `None`
        """
        self._connection.start()




    def get_absolute_engine_load(self) -> float:
        """
        Gets the absolute load of the engine, as a percentage of the maximum possible load (0-100%).
        
        Absolute Load is a parameter that represents the current load on the engine as a percentage of the maximum possible load the engine can handle. 
        Engine load is a measure of how hard the engine is working, taking into consideration factors such as throttle position, engine speed, air intake, and other parameters.
        
        Absolute Load is calculated using various sensor inputs, including the Mass Air Flow (MAF) sensor, Manifold Absolute Pressure (MAP) sensor, and throttle position sensor.
        The ECU uses this information to determine the optimal fuel injection, ignition timing, and other engine control parameters to ensure the best performance, fuel efficiency, and emissions.
        """
        response = self._connection.query(obd.commands.ABSOLUTE_LOAD)
        return response.value.magnitude
    
    def get_accelerator_position_D(self) -> float:
        """
        Gets the accelerator pedal position D (one of two sensors). 
        
        It is measured from 0 to 100%, with 0% indicating that the pedal is not depressed at all (idle position) and 100% indicating that the pedal is fully depressed (maximum throttle).

        Returns
        -------
        `float`
            The accelerator pedal position, as a percentage from 0 to 100%.
        """
        response = self._connection.query(obd.commands.ACCELERATOR_POS_D)
        return response.value.magnitude
    
    def get_accelerator_position_E(self) -> float:
        """
        Gets the accelerator pedal position E (one of two sensors). 
        
        It is measured from 0 to 100%, with 0% indicating that the pedal is not depressed at all (idle position) and 100% indicating that the pedal is fully depressed (maximum throttle).

        Returns
        -------
        `float`
            The accelerator pedal position, as a percentage from 0 to 100%.
        """
        response = self._connection.query(obd.commands.ACCELERATOR_POS_E)
        return response.value.magnitude
    
    def get_ambient_air_temperature(self, as_fahrenheit: bool = False) -> float:
        """
        Gets the ambient air temperature.

        Parameters
        ----------
        `as_fahrenheit` : bool, optional
            Whether to return the temperature in degrees Fahrenheit or degrees Celsius (default).

        Returns
        -------
        `float`
            The ambient air temperature, in degrees Celsius or degrees Fahrenheit.
        """
        response = self._connection.query(obd.commands.AMBIANT_AIR_TEMP)
        value = response.value.magnitude
        if as_fahrenheit:
            value = (value * (9/5)) + 32
        return value
    
    def get_barometric_pressure(self, as_atm: bool = False, as_psi: bool = False) -> float:
        """
        Gets the barometric pressure (of the ambient air).

        This parameter is essential for the ECU to make accurate calculations and adjustments related to engine performance, fuel mixture, and ignition timing.

        Parameters
        ----------
        `as_atm` : bool, optional
            Whether to return the pressure in atmospheres (default is kilopascals / kPa).
        `as_psi` : bool, optional
            Whether to return the pressure in pounds per square inch (psi) (default is kilopascals / kPa).

        Returns
        -------
        `float`
            The barometric pressure, in kilopascals (kPa), atmospheres (atm), or pounds per square inch (psi).
        """
        response = self._connection.query(obd.commands.BAROMETRIC_PRESSURE)
        value = response.value.magnitude
        if as_atm:
            value = value / 101.325
        elif as_psi:
            value = value * 0.145038
        return value
    
    def get_catalyst_temperature_Bank1Sensor1(self, as_fahrenheit: bool = False) -> float:
        """
        Gets the catalyst temperature of bank 1, sensor 1.

        In a vehicle with multiple exhaust banks (usually in engines with more than four cylinders, like V6 or V8 engines), "Bank 1" refers to the exhaust bank containing cylinder number 1.
        In an inline engine (such as an inline-4 or inline-6), there is usually only one exhaust bank, and Bank 1 refers to that bank.
        
        "Sensor 1" typically refers to the pre-catalytic converter oxygen sensor (also known as an air-fuel ratio sensor or lambda sensor), which is located upstream of the catalytic converter. 
        This sensor monitors the oxygen content in the exhaust gases, allowing the ECU to adjust the air-fuel mixture for optimal combustion and emissions control.

        Parameters
        ----------
        `as_fahrenheit` : bool, optional
            Whether to return the temperature in degrees Fahrenheit or degrees Celsius (default).

        Returns
        -------
        `float`
            The catalyst temperature, in degrees Celsius or degrees Fahrenheit.
        """
        response = self._connection.query(obd.commands.CATALYST_TEMP_B1S1)
        value = response.value.magnitude
        if as_fahrenheit:
            value = (value * (9/5)) + 32
        return value
    
    def get_catalyst_temperature_Bank1Sensor2(self, as_fahrenheit: bool = False) -> float:
        """
        Gets the catalyst temperature of bank 1, sensor 2.

        In a vehicle with multiple exhaust banks (usually in engines with more than four cylinders, like V6 or V8 engines), "Bank 1" refers to the exhaust bank containing cylinder number 1.
        In an inline engine (such as an inline-4 or inline-6), there is usually only one exhaust bank, and Bank 1 refers to that bank.

        "Sensor 2" typically refers to the post-catalytic converter oxygen sensor (also known as a downstream oxygen sensor or lambda sensor), which is located downstream of the catalytic converter. 
        This sensor monitors the oxygen content in the exhaust gases after they have passed through the catalytic converter, allowing the ECU to determine the efficiency and proper operation of the catalytic converter.
        
        Parameters
        ----------
        `as_fahrenheit` : bool, optional
            Whether to return the temperature in degrees Fahrenheit or degrees Celsius (default).

        Returns
        -------
        `float`
            The catalyst temperature, in degrees Celsius or degrees Fahrenheit.
        """
        response = self._connection.query(obd.commands.CATALYST_TEMP_B1S2)
        value = response.value.magnitude
        if as_fahrenheit:
            value = (value * (9/5)) + 32
        return value
    
    def get_commanded_equivalence_ratio(self) -> float:
        """
        Gets the Commanded Equivalence Ratio.
        
        "Commanded Equivalence Ratio" refers to the air-fuel mixture ratio that the ECU is targeting for optimal combustion in the engine.
        The equivalence ratio is a dimensionless value that compares the actual air-fuel ratio to the ideal (or stoichiometric) air-fuel ratio.

        The stoichiometric air-fuel ratio is the ideal mixture where all the fuel is burned with the exact amount of air required for complete combustion, resulting in minimal emissions.
        For gasoline engines, the stoichiometric air-fuel ratio is typically around 14.7 parts air to 1 part fuel by weight (14.7 : 1).

        The equivalence ratio (`λ` or `lambda`) is calculated as follows:
            `Equivalence Ratio (`λ`) = Actual Air-Fuel Ratio / Stoichiometric Air-Fuel Ratio`
        A lambda value of 1 indicates a stoichiometric air-fuel mixture, while values below 1 indicate a rich mixture (more fuel than required), and values above 1 indicate a lean mixture (less fuel than required).
        
        The "Commanded Equivalence Ratio" is the target lambda value that the ECU sets based on various factors, such as engine load, speed, temperature, and more.
        The ECU uses this target lambda value to adjust the fuel injection and ignition timing to maintain the desired air-fuel mixture for optimal engine performance, efficiency, and emissions control.

        In certain conditions, such as during acceleration or when the engine is cold, the ECU may command a richer or leaner air-fuel mixture to ensure proper engine operation and protect the engine components from damage.
        
        Returns
        -------
        `float` or `str`
            The Commanded Equivalence Ratio, as a ratio.
        """
        response = self._connection.query(obd.commands.COMMANDED_EQUIV_RATIO)
        try:
            value = response.value.magnitude
        except:
            try: value = float(response.value)
            except: value = str(response.value)
        return value
    
    def get_control_module_voltage(self) -> float:
        """
        Gets the control module voltage.

        "Control Module Voltage" refers to the voltage supply provided to the ECU and other control modules in the vehicle.
        The ECU is an essential component responsible for managing various aspects of the engine's performance, including fuel injection, ignition timing, and emission control systems.

        Control Module Voltage is typically supplied by the vehicle's battery and charging system, usually through a voltage regulator to maintain a stable voltage level.
        This voltage is essential for the proper functioning of the ECU and other electronic control modules, as they rely on a stable power supply to operate correctly and process the sensor inputs and control outputs.
        If the voltage is too low or too high, it could indicate problems with the battery, charging system, voltage regulator, or wiring connections. 

        Returns
        -------
        `float`
            The control module voltage, in volts.
        """
        response = self._connection.query(obd.commands.CONTROL_MODULE_VOLTAGE)
        return response.value.magnitude
    
    def get_coolant_temperature(self, as_fahrenheit: bool = False) -> float:
        """
        Gets the engine coolant temperature.

        "Coolant Temperature" refers to the temperature of the engine coolant, which is the fluid responsible for absorbing and dissipating heat from the engine.
        Engine coolant, typically a mixture of water and ethylene glycol (antifreeze), circulates through the engine and radiator to regulate the engine's operating temperature within an optimal range.

        The Coolant Temperature parameter is measured by a sensor called the Engine Coolant Temperature (ECT) sensor, which is typically located near the thermostat housing or in the engine block.
        
        The ECU uses the coolant temperature data to make various adjustments to the engine's operation, such as:
            - Fuel injection
                - When the engine is cold, the ECU may increase the fuel mixture richness to improve cold-start performance and reduce emissions.
            - Ignition timing
                - The ECU may adjust ignition timing based on coolant temperature to optimize combustion efficiency and engine performance.
            - Cooling fan operation
                - The ECU uses coolant temperature to control when to activate or deactivate the electric cooling fan, maintaining the engine's optimal operating temperature.
            - Transmission operation
                - In some vehicles, the ECU may use coolant temperature data to manage transmission shift points, torque converter lockup, and other aspects of transmission performance.
        
        The coolant temperature should typically be within a specific range defined by the vehicle manufacturer, often between `190 °F` (`88 °C`) and `220 °F` (`104 °C`) for most vehicles when the engine reaches normal operating temperature.
        Abnormal coolant temperature readings may indicate issues such as a malfunctioning thermostat, a clogged radiator, or a failing water pump, which may require further investigation and repair.
        
        Parameters
        ----------
        `as_fahrenheit` : bool, optional
            Whether to return the temperature in degrees Fahrenheit or degrees Celsius (default).

        Returns
        -------
        `float`
            The coolant temperature, in degrees Celsius or degrees Fahrenheit.
        """
        response = self._connection.query(obd.commands.COOLANT_TEMP)
        value = response.value.magnitude
        if as_fahrenheit:
            value = (value * (9/5)) + 32
        return value
    
    def get_distance_with_MIL_on(self, as_meters: bool = False, as_feet: bool = False, as_miles: bool = False) -> float:
        """
        Gets the distance traveled with the "Malfunction Indicator Lamp" (MIL) on.

        Parameters
        ----------
        `as_meters` : bool, optional
            Whether to return the distance in meters (default is kilometers).
        `as_feet` : bool, optional
            Whether to return the distance in feet (default is kilometers).
        `as_miles` : bool, optional
            Whether to return the distance in miles (default is kilometers).

        Returns
        -------
        `float`
            The distance traveled with the MIL on, in kilometers, meters, feet, or miles.
        """
        response = self._connection.query(obd.commands.DISTANCE_W_MIL)
        value = response.value.magnitude
        if as_meters:
            value = value * 1000
        elif as_feet:
            value = value * 3280.84
        elif as_miles:
            value = value * 0.621371
        return value
    
    def get_engine_load(self) -> float:
        """
        Gets the calculated engine load.

        "Engine Load" refers to the percentage of the engine's maximum power output being used at a given time.
        It is a measure of how hard the engine is working under various operating conditions, taking into consideration factors such as throttle position, engine speed, air intake, and other parameters.

        Engine Load is typically calculated using various sensor inputs, including the Mass Air Flow (`MAF`) sensor, Manifold Absolute Pressure (`MAP`) sensor, and throttle position sensor.
        The ECU uses this information to determine the optimal fuel injection, ignition timing, and other engine control parameters to ensure the best performance, fuel efficiency, and emissions.
        
        ### Difference from Absolute Load
        Engine Load and Absolute Load are both measures of how hard an engine is working under various operating conditions, but they are calculated differently and represent different aspects of engine performance.

        Engine Load, sometimes called Relative Load or Calculated Load, is typically derived from the Manifold Absolute Pressure (MAP) sensor and other inputs, such as engine RPM and throttle position.
        Engine Load is expressed as a percentage of the current load relative to the maximum load at the current engine speed (RPM).
        This means the Engine Load value will vary depending on factors like vehicle speed, acceleration, and terrain.

        Absolute Load, on the other hand, represents the engine's current load as a percentage of the maximum possible load the engine can handle, regardless of engine speed (RPM).
        Unlike Engine Load, the Absolute Load value is not dependent on engine speed, making it a more consistent measure of engine performance across various operating conditions.

        Returns
        -------
        `float`
            The engine load, as a percentage from 0 to 100%.
        """
        response = self._connection.query(obd.commands.ENGINE_LOAD)
        return response.value.magnitude
    
    def get_engine_RPM(self, as_radians_per_second: bool = False) -> float:
        """
        Gets the engine RPM.

        Parameters
        ----------
        `as_radians_per_second` : bool, optional
            Whether to return the RPM in radians per second (default is revolutions per minute).

        Returns
        -------
        `float`
            The engine RPM, in revolutions per minute or radians per second.
        """
        response = self._connection.query(obd.commands.RPM)
        value = response.value.magnitude
        if as_radians_per_second:
            value = value * (np.pi / 30)
        return value
    
    def get_engine_run_time(self) -> float:
        """
        Gets the engine run time.

        Returns
        -------
        `float`
            The engine run time, in seconds.
        """
        response = self._connection.query(obd.commands.RUN_TIME)
        return response.value.magnitude
    
    def get_engine_run_time_with_MIL_on(self) -> float:
        """
        Gets the time the engine has ran with the Malfunction Indicator Lamp (`MIL`) on.

        Returns
        -------
        `float`
            The engine run time with the MIL on, in seconds.
        """
        response = self._connection.query(obd.commands.RUN_TIME_MIL)
        return response.value.magnitude
    
    def get_evaporative_purge(self) -> float:
        """
        Gets the Commanded Evaporative Purge.

        "Commanded Evaporative Purge" refers to the ECU's control of the purge valve in the evaporative emission control system (`EVAP`).
        The EVAP system is designed to prevent the release of fuel vapor emissions into the atmosphere, capturing fuel vapors in a charcoal canister and then purging them into the engine to be burned during the combustion process.

        The Commanded Evaporative Purge parameter represents the duty cycle or the percentage of time the purge valve is being opened by the ECU.
        This value ranges from 0% to 100%, where 0% means the purge valve is fully closed (no purging) and 100% means the purge valve is fully open (maximum purging).

        The ECU controls the purge valve based on various factors, including engine speed, load, temperature, and the fuel vapor pressure within the charcoal canister.
        The ECU uses inputs from various sensors to determine the optimal purge valve duty cycle, ensuring that the captured fuel vapors are efficiently burned in the engine without negatively affecting engine performance or emissions.
        
        Returns
        -------
        `float`
            The Commanded Evaporative Purge, as a percentage from 0 to 100%.
        """
        response = self._connection.query(obd.commands.EVAPORATIVE_PURGE)
        return response.value.magnitude
    
    def get_evaporative_system_vapor_pressure(self, as_kPa: bool = False, as_atm: bool = False, as_psi: bool = False) -> float:
        """
        Gets the evaporative system vapor pressure.

        "Evaporative System Vapor Pressure" refers to the pressure of the fuel vapor within the evaporative emission control system (`EVAP`).
        The EVAP system is designed to capture fuel vapors that would otherwise be released into the atmosphere and channel them back into the engine to be burned during the combustion process.

        The Evaporative System Vapor Pressure is typically measured by a sensor called the Fuel Tank Pressure (FTP) sensor or the EVAP system pressure sensor.
        This sensor is usually located in or near the fuel tank and measures the pressure difference between the fuel vapors inside the EVAP system and the atmospheric pressure outside the system.

        The ECU uses this pressure data to determine the proper functioning of the EVAP system, such as detecting leaks or ensuring the correct operation of the purge and vent valves.
        
        Parameters
        ----------
        `as_kPa` : bool, optional
            Whether to return the pressure in kilopascals (default is pascals).
        `as_atm` : bool, optional
            Whether to return the pressure in atmospheres (default is pascals).
        `as_psi` : bool, optional
            Whether to return the pressure in pounds per square inch (psi) (default is pascals).

        Returns
        -------
        `float`
            The evaporative system vapor pressure, in pascals (Pa), kilopascals (kPa), atmospheres (atm), or pounds per square inch (psi).
        """
        response = self._connection.query(obd.commands.EVAP_VAPOR_PRESSURE)
        value = response.value.magnitude
        if as_kPa:
            value = value / 1000
        elif as_atm:
            value = value / 101325
        elif as_psi:
            value = value * 0.000145038
        return value
    
    def get_fuel_level(self) -> float:
        """
        Gets the current fuel level of the vehicle, as a percentage of the maximum capacity.

        Returns
        -------
        `float`
            The fuel level, as a percentage from 0 to 100%.
        """
        response = self._connection.query(obd.commands.FUEL_LEVEL)
        return response.value.magnitude
    
    def get_fuel_rail_pressure(self, as_atm: bool = False, as_psi: bool = False) -> float:
        """
        Gets the fuel rail pressure (absolute).

        "Fuel Rail Pressure" refers to the pressure of the fuel inside the fuel rail, which is a part of the vehicle's fuel injection system.
        The fuel rail is a pipe that distributes fuel to the individual fuel injectors, which then spray the fuel into the engine's intake manifold or directly into the combustion chamber, depending on the type of fuel injection system.

        Fuel Rail Pressure is typically measured by a sensor called the Fuel Rail Pressure (FRP) sensor, which is located on or near the fuel rail.
        The ECU uses the fuel rail pressure data to control and adjust the operation of the fuel pump and fuel injectors, ensuring that the engine receives the appropriate amount of fuel for the current operating conditions, such as engine load, speed, and temperature.
        Maintaining the correct fuel pressure is critical for optimal engine performance, fuel efficiency, and emissions.

        Parameters
        ----------
        `as_atm` : bool, optional
            Whether to return the pressure in atmospheres (default is kilopascals / kPa).
        `as_psi` : bool, optional
            Whether to return the pressure in pounds per square inch (psi) (default is kilopascals / kPa).

        Returns
        -------
        `float`
            The fuel rail pressure, in kilopascals (kPa), atmospheres (atm), or pounds per square inch (psi).
        """
        response = self._connection.query(obd.commands.FUEL_RAIL_PRESSURE_ABS)
        value = response.value.magnitude
        if as_atm:
            value = value / 101.325
        elif as_psi:
            value = value * 0.145038
        return value
    
    def get_fuel_status(self) -> tuple[str, str]:
        """
        Gets the fuel system status.

        "Fuel Status" refers to the current operating mode of the engine's fuel control system.
        The fuel control system manages the air-fuel mixture for optimal engine performance, fuel efficiency, and emissions.

        The two main operating modes are "open loop" and "closed loop."
        - Open loop
            - In open loop mode, the ECU determines the air-fuel mixture based on pre-defined values stored in its memory (lookup tables), 
                without using feedback from the oxygen sensor(s). Open loop mode typically occurs during specific situations, such as:
                - Insufficient engine temperature: When the engine is cold (e.g., during a cold start or engine warm-up), 
                    the ECU operates in open loop mode, providing a richer air-fuel mixture to improve cold-start performance and reduce emissions.
                - Heavy acceleration or high load: Under certain high-load conditions, 
                    the ECU may switch to open loop mode to ensure adequate fuel delivery and prevent engine damage.
        - Closed loop
            -  In closed loop mode, the ECU actively uses feedback from the oxygen sensor(s) to continuously adjust the air-fuel mixture for optimal combustion.
                This mode is used when the engine is at normal operating temperature and under typical driving conditions.
                By monitoring the oxygen levels in the exhaust gases, the ECU can determine if the 
                air-fuel mixture is too rich (too much fuel) or too lean (not enough fuel) and make the necessary adjustments.

        Returns
        -------
        `tuple[str, str]`
            A tuple containing the status of the first and second fuel systems, respectively.
        
        ## Note
        Most cars only have one system, so the second element will likely be an empty string.

        The possible fuel statuses are:
        - ""
        - "Open loop due to insufficient engine temperature"
        - "Closed loop, using oxygen sensor feedback to determine fuel mix"
        - "Open loop due to engine load OR fuel cut due to deceleration"
        - "Open loop due to system failure"
        - "Closed loop, using at least one oxygen sensor but there is a fault in the feedback system"
        """
        response = self._connection.query(obd.commands.FUEL_STATUS)
        return response.value
    
    def get_intake_manifold_pressure(self, as_atm: bool = False, as_psi: bool = False) -> float:
        """
        Gets the intake manifold pressure.

        "Intake Manifold Pressure" refers to the pressure of the air inside the intake manifold, which is the component that channels the air-fuel mixture from the throttle body to the engine's combustion chambers.
        The intake manifold pressure is an important parameter that the ECU uses to calculate the engine load, determine the optimal air-fuel mixture, and adjust the ignition timing for optimal engine performance, fuel efficiency, and emissions.

        Intake Manifold Pressure is typically measured by a sensor called the Manifold Absolute Pressure (MAP) sensor, which is located on or near the intake manifold.
        The MAP sensor measures the pressure inside the manifold and converts it into an electrical signal that the ECU can interpret.
        The pressure in the intake manifold can vary depending on factors such as throttle position, engine speed, and load.

        Parameters
        ----------
        `as_atm` : bool, optional
            Whether to return the pressure in atmospheres (default is kilopascals / kPa).
        `as_psi` : bool, optional
            Whether to return the pressure in pounds per square inch (psi) (default is kilopascals / kPa).

        Returns
        -------
        `float`
            The intake manifold pressure, in kilopascals (kPa), atmospheres (atm), or pounds per square inch (psi).
        """
        response = self._connection.query(obd.commands.INTAKE_PRESSURE)
        value = response.value.magnitude
        if as_atm:
            value = value / 101.325
        elif as_psi:
            value = value * 0.145038
        return value
    
    def get_intake_air_temperature(self, as_fahrenheit: bool = False) -> float:
        """
        Gets the intake air temperature.

        "Intake Air Temperature" refers to the temperature of the air being drawn into the engine's intake manifold.
        This parameter is important because the air temperature can significantly affect the engine's performance, fuel efficiency, and emissions.

        The Intake Air Temperature is measured by a sensor called the Intake Air Temperature (IAT) sensor or the Manifold Air Temperature (MAT) sensor, which is usually located near the air filter or in the intake manifold itself.
        The IAT sensor measures the temperature of the incoming air and sends this information to the ECU.

        The ECU uses the intake air temperature data to adjust various engine parameters, such as the air-fuel mixture and ignition timing, to optimize engine performance under different operating conditions.
        For example, colder air is denser and contains more oxygen, which may require a richer air-fuel mixture to maintain optimal combustion, while warmer air is less dense and may require a leaner air-fuel mixture.
        
        Parameters
        ----------
        `as_fahrenheit` : bool, optional
            Whether to return the temperature in degrees Fahrenheit or degrees Celsius (default).

        Returns
        -------
        `float`
            The intake air temperature, in degrees Celsius or degrees Fahrenheit.
        """
        response = self._connection.query(obd.commands.INTAKE_TEMP)
        value = response.value.magnitude
        if as_fahrenheit:
            value = (value * (9/5)) + 32
        return value
    
    def get_long_term_fuel_trim_Bank1(self) -> float:
        """
        Gets the Long Term Fuel Trim of bank 1.

        "Long Term Fuel Trim of Bank 1" refers to the ECU's continuous adjustment of the air-fuel mixture for the engine cylinders in Bank 1 over an extended period of time.
        Engines with more than one cylinder bank, such as V-shaped or horizontally opposed engines, have separate fuel trims for each bank (Bank 1 and Bank 2).

        Fuel trims are the ECU's way of fine-tuning the air-fuel mixture to optimize engine performance, fuel efficiency, and emissions.
        Fuel trims are divided into two categories: short-term fuel trim (`STFT`) and long-term fuel trim (`LTFT`).
        While short-term fuel trim represents real-time adjustments based on immediate feedback from the oxygen sensor(s), 
        long-term fuel trim represents adjustments made over a longer period, based on the cumulative data from the short-term fuel trim.

        The long-term fuel trim values are expressed as a percentage, with a positive value indicating a lean condition (more air, less fuel) and a negative value indicating a rich condition (less air, more fuel).
        A value close to 0% indicates that the air-fuel mixture is close to the ideal stoichiometric ratio (14.7:1 for gasoline engines).
        However, slight deviations from 0% are normal, as the ECU constantly adjusts the fuel trims to maintain optimal engine performance.

        Returns
        -------
        `float`
            The Long Term Fuel Trim of Bank 1, as a percentage.
        """
        response = self._connection.query(obd.commands.LONG_FUEL_TRIM_1)
        return response.value.magnitude
    
    def get_long_term_O2_trim_Bank1(self) -> float:
        """
        Gets the long term secondary oxygen sensor trim of bank 1.

        "Long Term Secondary Oxygen Sensor Trim of Bank 1" refers to the adjustments made by the ECU to compensate for the efficiency 
        of the catalytic converter in Bank 1, based on the feedback from the secondary oxygen sensor (also known as the downstream or post-catalytic converter oxygen sensor).

        The secondary oxygen sensor monitors the oxygen content in the exhaust gases after they have passed through the catalytic converter.
        Its primary purpose is to assess the efficiency of the catalytic converter in reducing harmful emissions.
        The ECU uses the data from the secondary oxygen sensor to make adjustments to the air-fuel mixture and optimize the performance of the catalytic converter.

        Long Term Secondary Oxygen Sensor Trim is expressed as a percentage, with positive values indicating the ECU is compensating for a less efficient catalytic converter (adding more fuel), 
        and negative values indicating the ECU is compensating for an overly efficient catalytic converter (reducing fuel).

        A value close to 0% suggests that the catalytic converter is functioning within its normal efficiency range.

        Returns
        -------
        `float`
            The Long Term Secondary Oxygen Sensor Trim of Bank 1, as a percentage.
        """
        response = self._connection.query(obd.commands.LONG_O2_TRIM_B1)
        return response.value.magnitude
    
    def get_O2_Bank1Sensor2_voltage(self) -> float:
        """
        Gets the oxygen sensor voltage of bank 1, sensor 2.

        "Oxygen Sensor Voltage of Bank 1, Sensor 2" refers to the voltage signal generated by the secondary (downstream) oxygen sensor for the engine cylinders in Bank 1.
        The secondary oxygen sensor, also known as Sensor 2, is typically located after the catalytic converter in the exhaust system.

        The primary purpose of the secondary oxygen sensor is to monitor the efficiency of the catalytic converter, which is responsible for reducing harmful emissions.
        The sensor measures the oxygen content in the exhaust gases after they have passed through the catalytic converter.
        The oxygen sensor generates a voltage signal based on the difference in oxygen concentration between the exhaust gas and the ambient air.
        This voltage signal is sent to the ECU, which uses the data to assess the performance of the catalytic converter and make necessary adjustments to the air-fuel mixture and other parameters.

        Typically, a properly functioning catalytic converter will cause the oxygen levels in the exhaust gases to be relatively stable, resulting in a steady voltage signal from the secondary oxygen sensor.
        If the catalytic converter is not working efficiently, the oxygen levels in the exhaust gases will fluctuate, causing the voltage signal from the sensor to vary.

        Returns
        -------
        `float`
            The Oxygen Sensor Voltage of Bank 1, Sensor 2, in volts.
        """
        response = self._connection.query(obd.commands.O2_B1S2)
        return response.value.magnitude
    
    def get_O2_sensor1_WR_lambda_current(self, as_amperes: bool = False) -> float:
        """
        Gets the oxygen sensor 1 WR lambda current.

        "Oxygen Sensor 1 WR Lambda Current" refers to the current signal generated by a wideband oxygen sensor (also known as a wide-range or wide-ratio lambda sensor) for Sensor 1.
        Sensor 1 is typically the primary (pre-catalytic converter) oxygen sensor, located in the exhaust system before the catalytic converter.

        Wideband oxygen sensors are more advanced than traditional narrowband oxygen sensors, as they can accurately measure a broader range of air-fuel ratios.
        They provide more precise information about the air-fuel mixture, allowing the ECU to make better adjustments and optimize engine performance, fuel efficiency, and emissions.

        A wideband oxygen sensor measures the oxygen concentration in the exhaust gases by generating a current signal, which is proportional to the deviation of the air-fuel ratio from the stoichiometric value (14.7:1 for gasoline engines).
        The ECU uses this current signal to determine the air-fuel mixture and make necessary adjustments.

        Positive current values indicate a rich air-fuel mixture (more fuel, less air), while negative current values indicate a lean air-fuel mixture (less fuel, more air).
        A current value close to zero suggests that the air-fuel mixture is close to the stoichiometric ratio.

        Parameters
        ----------
        `as_amperes` : bool, optional
            Whether to return the current in amperes (default is milliamperes).

        Returns
        -------
        `float`
            The Oxygen Sensor 1 WR Lambda Current, in milliamperes or amperes.
        """
        response = self._connection.query(obd.commands.O2_S1_WR_CURRENT)
        value = response.value.magnitude
        if as_amperes:
            value = value / 1000
        return value
    
    def get_O2_sensors_present(self) -> str:
        """
        Gets the oxygen sensors present.

        Returns
        -------
        `str`
            The oxygen sensors present, formatted like 
                `"Bank 1: (True, True, False, False)"`

                `"Bank 2: (True, True, False, False)"`
        """
        response: tuple[tuple] = self._connection.query(obd.commands.O2_SENSORS)
        bank1 = response[1]
        bank2 = response[2]
        return f"Bank 1: {bank1}\nBank 2: {bank2}"
    
    def get_obd_compliance(self) -> str:
        """
        Gets the OBD standards compliance.

        Returns
        -------
        `str`
            The OBD standards compliance, formatted like `"OBD-II / EOBD"`
        """
        response = self._connection.query(obd.commands.OBD_COMPLIANCE)
        return response
    
    def get_PIDs_A(self) -> str:
        """
        Gets the supported PIDs [01-20].

        PIDs (Parameter IDs) A, B, and C refer to the groups of supported diagnostic parameters that the vehicle's ECU can report.
        PIDs are standardized sets of data that the ECU can provide, and they are organized in groups, with each group covering a specific range of parameters.

        PID A (01-20) covers the first set of 32 PIDs, ranging from 01 to 20.
        These PIDs typically include information related to the engine's performance, such as coolant temperature, engine RPM, vehicle speed, and calculated engine load.
        They also include data about the oxygen sensors and their output voltages.

        Returns
        -------
        `str`
            The supported PIDs [01-20].
        """
        response: BitArray = self._connection.query(obd.commands.PIDS_A)
        return str(response)
    
    def get_PIDs_B(self) -> str:
        """
        Gets the supported PIDs [21-40].

        PIDs (Parameter IDs) A, B, and C refer to the groups of supported diagnostic parameters that the vehicle's ECU can report.
        PIDs are standardized sets of data that the ECU can provide, and they are organized in groups, with each group covering a specific range of parameters.

        PID B (21-40) covers the second set of 32 PIDs, ranging from 21 to 40.
        These PIDs typically include additional engine parameters, such as fuel system status, fuel pressure, and intake manifold pressure.
        They also cover information about the evaporative emissions control system and the oxygen sensor fuel trim values.

        Returns
        -------
        `str`
            The supported PIDs [21-40].
        """
        response: BitArray = self._connection.query(obd.commands.PIDS_B)
        return str(response)
    
    def get_PIDs_C(self) -> str:
        """
        Gets the supported PIDs [41-60].

        PIDs (Parameter IDs) A, B, and C refer to the groups of supported diagnostic parameters that the vehicle's ECU can report.
        PIDs are standardized sets of data that the ECU can provide, and they are organized in groups, with each group covering a specific range of parameters.

        PID C (41-60) covers the third set of 32 PIDs, ranging from 41 to 60.
        These PIDs include parameters related to the monitoring of emission-related components, such as catalyst temperature, EGR system, and secondary air system.
        They also provide information about the vehicle's control module and diagnostic trouble codes (DTCs).

        Returns
        -------
        `str`
            The supported PIDs [41-60].
        """
        response: BitArray = self._connection.query(obd.commands.PIDS_C)
        return str(response)
    
    def get_relative_throttle_position(self) -> float:
        """
        Gets the relative throttle position.

        "Relative Throttle Position" refers to the current position of the throttle valve relative to its resting position (usually fully closed) when the accelerator pedal is not being pressed.
        The throttle position indicates the degree to which the throttle valve is open, allowing air to enter the engine, which directly impacts engine speed, power output, and fuel consumption.

        The Relative Throttle Position is measured by the Throttle Position Sensor (`TPS`) located on the throttle body.
        The TPS is a potentiometer that converts the mechanical movement of the throttle valve into an electrical signal that the ECU can interpret.

        The Relative Throttle Position is typically expressed as a percentage, with 0% representing the throttle valve's fully closed position and 100% representing the fully open position.

        Returns
        -------
        `float`
            The relative throttle position, as a percentage from 0 to 100%.
        """
        response = self._connection.query(obd.commands.RELATIVE_THROTTLE_POS)
        return response.value.magnitude
    
    def get_short_term_fuel_trim_Bank1(self) -> float:
        """
        Gets the short term fuel trim of bank 1.

        "Short Term Fuel Trim of Bank 1" refers to the real-time adjustments the ECU makes to the air-fuel mixture for the engine cylinders in Bank 1.
        Engines with more than one cylinder bank, such as V-shaped or horizontally opposed engines, have separate fuel trims for each bank (Bank 1 and Bank 2).

        Fuel trims are the ECU's way of fine-tuning the air-fuel mixture to optimize engine performance, fuel efficiency, and emissions.
        Fuel trims are divided into two categories: short-term fuel trim (STFT) and long-term fuel trim (LTFT).
        Short-term fuel trim represents real-time adjustments based on immediate feedback from the oxygen sensor(s), while long-term fuel trim represents adjustments made over a longer period, based on the cumulative data from the short-term fuel trim.

        The short-term fuel trim values are expressed as a percentage, with positive values indicating a lean condition (more air, less fuel) and negative values indicating a rich condition (less air, more fuel).
        A value close to 0% indicates that the air-fuel mixture is close to the ideal stoichiometric ratio (14.7:1 for gasoline engines).
        However, slight deviations from 0% are normal, as the ECU constantly adjusts the fuel trims to maintain optimal engine performance.

        Returns
        -------
        `float`
            The Short Term Fuel Trim of Bank 1, as a percentage from 0 to 100%.
        """
        response = self._connection.query(obd.commands.SHORT_FUEL_TRIM_1)
        return response.value.magnitude
    
    def get_short_term_O2_trim_Bank1(self) -> float:
        """
        Gets the short term secondary oxygen sensor trim of bank 1.

        "Short Term Secondary Oxygen Sensor Trim of Bank 1" refers to the real-time adjustments made by the ECU to compensate for the efficiency of the catalytic converter in Bank 1, 
        based on the feedback from the secondary oxygen sensor (also known as the downstream or post-catalytic converter oxygen sensor).

        The primary purpose of the secondary oxygen sensor is to monitor the efficiency of the catalytic converter, which is responsible for reducing harmful emissions.
        The sensor measures the oxygen content in the exhaust gases after they have passed through the catalytic converter.
        The ECU uses this data to make adjustments to the air-fuel mixture and optimize the performance of the catalytic converter.

        Short Term Secondary Oxygen Sensor Trim is expressed as a percentage, with positive values indicating the ECU is compensating for a less efficient catalytic converter (adding more fuel), 
        and negative values indicating the ECU is compensating for an overly efficient catalytic converter (reducing fuel).
        A value close to 0% suggests that the catalytic converter is functioning within its normal efficiency range.

        Returns
        -------
        `float`
            The Short Term Secondary Oxygen Sensor Trim of Bank 1, as a percentage from 0 to 100%.
        """
        response = self._connection.query(obd.commands.SHORT_O2_TRIM_B1)
        return response.value.magnitude
    
    def get_speed(self, as_feet_per_second: bool = False, as_kilometers_per_hour: bool = False, as_miles_per_hour: bool = False) -> float:
        """
        Gets the vehicle speed.

        Parameters
        ----------
        `as_feet_per_second` : bool, optional
            Whether to return the speed in feet per second (default is meters per second).
        `as_kilometers_per_hour` : bool, optional
            Whether to return the speed in kilometers per hour (default is meters per second).
        `as_miles_per_hour` : bool, optional
            Whether to return the speed in miles per hour (default is meters per second).

        Returns
        -------
        `float`
            The vehicle speed, in meters per second, feet per second, kilometers per hour, or miles per hour.
        """
        response = self._connection.query(obd.commands.SPEED)
        value = response.value.magnitude    # default return value is in kilometers per hour, need to convert to meters per second first
        value = value / 3.6
        if as_feet_per_second:
            value = value * 3.28084
        elif as_kilometers_per_hour:
            value = value * 3.6
        elif as_miles_per_hour:
            value = value * 2.23694
        return value
    
    def get_status_this_drive_cycle(self) -> list[bool, int]:
        """
        Gets the status this drive cycle.

        The `STATUS` command returns information about the Malfunction Indicator Lamp (`MIL`) or Check Engine Light (`CEL`),
        the number of trouble codes being thrown, and the type of engine.

        Returns
        -------
        list[bool, int]
            A list containing the following values:
            - `is_MIL_on`: Whether the MIL is on or off.
            - `DTC_count`: The number of DTCs being thrown.
        """
        response: OBDStatusResponse = self._connection.query(obd.commands.STATUS_DRIVE_CYCLE)
        is_MIL_on = response.MIL
        DTC_count = response.DTC_count
        return [is_MIL_on, DTC_count]
    
    def get_commanded_throttle_actuator(self) -> float:
        """
        Gets the Commanded Throttle Actuator.

        "Commanded Throttle Actuator" refers to the ECU's control of the throttle actuator, which is responsible for adjusting the position of the throttle valve in the throttle body.
        The throttle valve controls the amount of air entering the engine, directly impacting engine speed, power output, and fuel consumption.

        In modern vehicles equipped with electronic throttle control (also known as drive-by-wire), 
        the traditional mechanical linkage between the accelerator pedal and the throttle body is replaced with electronic sensors and actuators.
        When the driver presses the accelerator pedal, the pedal position sensor sends a signal to the ECU, which then commands the throttle actuator to adjust the throttle valve's position accordingly.

        The Commanded Throttle Actuator parameter represents the ECU's desired position of the throttle valve, typically expressed as a percentage.
        A value of 0% indicates that the throttle valve is fully closed (idle position), and a value of 100% indicates that the throttle valve is fully open (maximum air intake).

        Returns
        -------
        `float`
            The Commanded Throttle Actuator, as a percentage from 0 to 100%.
        """
        response = self._connection.query(obd.commands.THROTTLE_ACTUATOR)
        return response.value.magnitude
    
    def get_absolute_throttle_position(self) -> float:
        """
        Gets the throttle position.

        "Throttle Position" and "Throttle Position B" refer to the readings from two separate sensors that measure the position of the throttle valve in the throttle body.
        The throttle valve controls the amount of air entering the engine, directly impacting engine speed, power output, and fuel consumption.

        In modern vehicles equipped with electronic throttle control (also known as drive-by-wire), the throttle position is measured by one or more throttle position sensors (TPS) located on the throttle body.
        These sensors convert the mechanical movement of the throttle valve into an electrical signal that the ECU can interpret.

        - Throttle Position
            - This parameter represents the reading from the primary throttle position sensor (TPS). It indicates the current position of the throttle valve, typically expressed as a percentage.
                A value of 0% indicates that the throttle valve is fully closed (idle position), and a value of 100% indicates that the throttle valve is fully open (maximum air intake).
        - Throttle Position B
            - This parameter represents the reading from a secondary or redundant throttle position sensor (TPS B).
                It serves as a backup to the primary sensor and provides an additional layer of safety and reliability.
                The secondary sensor's reading should closely match the primary sensor's reading under normal operating conditions.
        
        The use of two throttle position sensors allows the ECU to compare the readings from both sensors and detect any discrepancies.
        If the readings from the two sensors do not match or fall outside of the expected range, the ECU may trigger a diagnostic trouble code (DTC) and enter a failsafe or "limp" mode to protect the engine from potential damage.
        
        Returns
        -------
        `float`
            The throttle position, as a percentage from 0 to 100%.
        """
        response = self._connection.query(obd.commands.THROTTLE_POS)
        return response.value.magnitude
    
    def get_absolute_throttle_position_B(self) -> float:
        """
        Gets the absolute throttle position B.

        "Throttle Position" and "Throttle Position B" refer to the readings from two separate sensors that measure the position of the throttle valve in the throttle body.
        The throttle valve controls the amount of air entering the engine, directly impacting engine speed, power output, and fuel consumption.

        In modern vehicles equipped with electronic throttle control (also known as drive-by-wire), the throttle position is measured by one or more throttle position sensors (TPS) located on the throttle body.
        These sensors convert the mechanical movement of the throttle valve into an electrical signal that the ECU can interpret.

        - Throttle Position
            - This parameter represents the reading from the primary throttle position sensor (TPS). It indicates the current position of the throttle valve, typically expressed as a percentage.
                A value of 0% indicates that the throttle valve is fully closed (idle position), and a value of 100% indicates that the throttle valve is fully open (maximum air intake).
        - Throttle Position B
            - This parameter represents the reading from a secondary or redundant throttle position sensor (TPS B).
                It serves as a backup to the primary sensor and provides an additional layer of safety and reliability.
                The secondary sensor's reading should closely match the primary sensor's reading under normal operating conditions.
        
        The use of two throttle position sensors allows the ECU to compare the readings from both sensors and detect any discrepancies.
        If the readings from the two sensors do not match or fall outside of the expected range, the ECU may trigger a diagnostic trouble code (DTC) and enter a failsafe or "limp" mode to protect the engine from potential damage.
        
        Returns
        -------
        `float`
            The throttle position B, as a percentage from 0 to 100%.
        """
        response = self._connection.query(obd.commands.THROTTLE_POS_B)
        return response.value.magnitude
    
    def get_timing_advance(self, as_radians: bool = False) -> float:
        """
        Gets the timing advance.

        "Timing Advance" refers to the number of degrees by which the ignition timing is advanced relative to the top dead center (TDC) of the piston in the engine's cylinder.
        In other words, it represents how many degrees before the piston reaches TDC that the spark plug is fired to ignite the air-fuel mixture in the combustion chamber.

        Ignition timing is a critical parameter that affects engine performance, fuel efficiency, and emissions.
        Properly timed ignition ensures that the combustion process occurs at the optimal moment to produce maximum power and minimize harmful emissions.

        The ECU dynamically adjusts the timing advance based on various factors, including engine speed (RPM), load, temperature, throttle position, and the octane rating of the fuel being used.
        For example, under light load and low RPM conditions, the ECU may advance the ignition timing to improve fuel efficiency, 
        while under heavy load and high RPM conditions, the ECU may retard the ignition timing to prevent engine knocking (abnormal combustion) and protect the engine from potential damage.

        The Timing Advance parameter is typically expressed in degrees of crankshaft rotation.
        A positive value indicates that the spark is occurring before TDC (advanced timing), while a negative value indicates that the spark is occurring after TDC (retarded timing).

        Parameters
        ----------
        `as_radians` : bool, optional
            Whether to return the advance in radians (default is degrees).

        Returns
        -------
        `float`
            The timing advance, in degrees or radians.
        """
        response = self._connection.query(obd.commands.TIMING_ADVANCE)
        value = response.value.magnitude
        if as_radians:
            value = value * 0.0174533
        return value