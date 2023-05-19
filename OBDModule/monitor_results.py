"""
# monitor_results.py

Defines the MonitorResults class, 
which is used to store a collection of methods that return results of various OBD monitor tests.
"""

import obd
from obd.OBDResponse import MonitorTest
from obd.OBDResponse import Monitor as OBDMonitorResponse





class MonitorResults:
    """
    Collection of methods that return results of various OBD monitor tests.
    """
    def __init__(self, connection: obd.OBD) -> "MonitorResults":
        self.__connection = connection
    

    def catalyst_bank1(self) -> str:
        """
        Fetches Bank 1 Catalyst test results.

        "Bank 1 Catalyst Monitor" refers to a diagnostic monitor that assesses the performance and efficiency of the catalytic converter for the engine cylinders in Bank 1.
        The catalytic converter is an essential component of the vehicle's exhaust system that reduces harmful emissions by converting pollutants such as carbon monoxide (CO), hydrocarbons (HC), and nitrogen oxides (NOx) into less harmful substances like carbon dioxide (CO2), water (H2O), and nitrogen (N2).

        The Bank 1 Catalyst Monitor evaluates the efficiency of the catalytic converter by analyzing the signals from the oxygen sensors located before and after the converter (i.e., the primary or pre-catalytic converter oxygen sensor, also known as Sensor 1, and the secondary or post-catalytic converter oxygen sensor, also known as Sensor 2). 
        By comparing the readings from these two sensors, the ECU can determine how effectively the catalytic converter is reducing pollutants in the exhaust.

        If the catalytic converter is functioning efficiently, the primary oxygen sensor will show rapid fluctuations in oxygen levels, while the secondary oxygen sensor will show relatively stable oxygen levels. 
        If the catalytic converter is not performing efficiently, the secondary oxygen sensor may show rapid fluctuations similar to the primary sensor, indicating that the converter is not effectively reducing emissions.
        
        Returns
        -------
        `str`
            Bank 1 Catalyst Monitor test results.
        """
        response: OBDMonitorResponse = self.__connection.query(obd.commands.MONITOR_CATALYST_B1)
        tests: list[MonitorTest] = response.tests
        tests_str: str = "Catalyst [Bank 1] Monitor test results:\n" + str(response)
        return tests_str
    


    def EVAP_020(self) -> str:
        """
        Fetches EVAP Monitor (0.020) test results.

        "EVAP Monitor (0.020)," "EVAP Monitor (0.040)," "EVAP Monitor (0.090)," and "EVAP Monitor (Cap Off / 0.150)" refer to different types of 
        diagnostic tests or monitors performed by the ECU to assess the integrity of the evaporative emission control system (EVAP) and detect leaks of different sizes.

        The numbers in parentheses (0.020, 0.040, 0.090, 0.150) represent the size of the leak being tested, measured in inches.

        The EVAP system is designed to capture fuel vapors from the fuel tank and prevent them from being released into the atmosphere.
        The captured vapors are then directed to the engine to be burned during the combustion process.
        The EVAP system includes components such as the charcoal canister, purge valve, vent valve, and fuel tank pressure sensor.

        The EVAP monitors are designed to detect leaks in the EVAP system that could allow fuel vapors to escape into the atmosphere.
        The ECU performs these tests by pressurizing the EVAP system and monitoring the pressure changes over time. 

        The specific leak size being tested determines the type of EVAP monitor:
        - EVAP Monitor (0.020)
            - This monitor tests for very small leaks in the EVAP system, equivalent to a hole size of 0.020 inches in diameter.
        - EVAP Monitor (0.040)
            - This monitor tests for small leaks in the EVAP system, equivalent to a hole size of 0.040 inches in diameter.
        - EVAP Monitor (0.090)
            - This monitor tests for medium-sized leaks in the EVAP system, equivalent to a hole size of 0.090 inches in diameter.
        - EVAP Monitor (Cap Off / 0.150)
            - This monitor tests for large leaks in the EVAP system, equivalent to a hole size of 0.150 inches in diameter. 
                This test is also used to detect scenarios where the fuel cap is missing or not properly tightened.

        If the ECU detects a leak during any of these tests, it will trigger a diagnostic trouble code (DTC) and illuminate the check engine light.
        The specific DTC will indicate the type and size of the leak detected, allowing technicians to diagnose and repair the issue.

        Returns
        -------
        `str`
            EVAP Monitor (0.020) test results.
        """
        response: OBDMonitorResponse = self.__connection.query(obd.commands.MONITOR_EVAP_020)
        tests: list[MonitorTest] = response.tests
        tests_str: str = "EVAP (0.020) Monitor test results:\n" + str(response)
        return tests_str
    


    def EVAP_040(self) -> str:
        """
        Fetches EVAP Monitor (0.040) test results.

        "EVAP Monitor (0.020)," "EVAP Monitor (0.040)," "EVAP Monitor (0.090)," and "EVAP Monitor (Cap Off / 0.150)" refer to different types of 
        diagnostic tests or monitors performed by the ECU to assess the integrity of the evaporative emission control system (EVAP) and detect leaks of different sizes.

        The numbers in parentheses (0.020, 0.040, 0.090, 0.150) represent the size of the leak being tested, measured in inches.

        The EVAP system is designed to capture fuel vapors from the fuel tank and prevent them from being released into the atmosphere.
        The captured vapors are then directed to the engine to be burned during the combustion process.
        The EVAP system includes components such as the charcoal canister, purge valve, vent valve, and fuel tank pressure sensor.

        The EVAP monitors are designed to detect leaks in the EVAP system that could allow fuel vapors to escape into the atmosphere.
        The ECU performs these tests by pressurizing the EVAP system and monitoring the pressure changes over time. 

        The specific leak size being tested determines the type of EVAP monitor:
        - EVAP Monitor (0.020)
            - This monitor tests for very small leaks in the EVAP system, equivalent to a hole size of 0.020 inches in diameter.
        - EVAP Monitor (0.040)
            - This monitor tests for small leaks in the EVAP system, equivalent to a hole size of 0.040 inches in diameter.
        - EVAP Monitor (0.090)
            - This monitor tests for medium-sized leaks in the EVAP system, equivalent to a hole size of 0.090 inches in diameter.
        - EVAP Monitor (Cap Off / 0.150)
            - This monitor tests for large leaks in the EVAP system, equivalent to a hole size of 0.150 inches in diameter. 
                This test is also used to detect scenarios where the fuel cap is missing or not properly tightened.

        If the ECU detects a leak during any of these tests, it will trigger a diagnostic trouble code (DTC) and illuminate the check engine light.
        The specific DTC will indicate the type and size of the leak detected, allowing technicians to diagnose and repair the issue.

        Returns
        -------
        `str`
            EVAP Monitor (0.040) test results.
        """
        response: OBDMonitorResponse = self.__connection.query(obd.commands.MONITOR_EVAP_040)
        tests: list[MonitorTest] = response.tests
        tests_str: str = "EVAP (0.040) Monitor test results:\n" + str(response)
        return tests_str
    


    def EVAP_090(self) -> str:
        """
        Fetches EVAP Monitor (0.090) test results.

        "EVAP Monitor (0.020)," "EVAP Monitor (0.040)," "EVAP Monitor (0.090)," and "EVAP Monitor (Cap Off / 0.150)" refer to different types of 
        diagnostic tests or monitors performed by the ECU to assess the integrity of the evaporative emission control system (EVAP) and detect leaks of different sizes.

        The numbers in parentheses (0.020, 0.040, 0.090, 0.150) represent the size of the leak being tested, measured in inches.

        The EVAP system is designed to capture fuel vapors from the fuel tank and prevent them from being released into the atmosphere.
        The captured vapors are then directed to the engine to be burned during the combustion process.
        The EVAP system includes components such as the charcoal canister, purge valve, vent valve, and fuel tank pressure sensor.

        The EVAP monitors are designed to detect leaks in the EVAP system that could allow fuel vapors to escape into the atmosphere.
        The ECU performs these tests by pressurizing the EVAP system and monitoring the pressure changes over time. 

        The specific leak size being tested determines the type of EVAP monitor:
        - EVAP Monitor (0.020)
            - This monitor tests for very small leaks in the EVAP system, equivalent to a hole size of 0.020 inches in diameter.
        - EVAP Monitor (0.040)
            - This monitor tests for small leaks in the EVAP system, equivalent to a hole size of 0.040 inches in diameter.
        - EVAP Monitor (0.090)
            - This monitor tests for medium-sized leaks in the EVAP system, equivalent to a hole size of 0.090 inches in diameter.
        - EVAP Monitor (Cap Off / 0.150)
            - This monitor tests for large leaks in the EVAP system, equivalent to a hole size of 0.150 inches in diameter. 
                This test is also used to detect scenarios where the fuel cap is missing or not properly tightened.

        If the ECU detects a leak during any of these tests, it will trigger a diagnostic trouble code (DTC) and illuminate the check engine light.
        The specific DTC will indicate the type and size of the leak detected, allowing technicians to diagnose and repair the issue.

        Returns
        -------
        `str`
            EVAP Monitor (0.090) test results.
        """
        response: OBDMonitorResponse = self.__connection.query(obd.commands.MONITOR_EVAP_090)
        tests: list[MonitorTest] = response.tests
        tests_str: str = "EVAP (0.090) Monitor test results:\n" + str(response)
        return tests_str
    


    def EVAP_150(self) -> str:
        """
        Fetches EVAP Monitor (Cap Off / 0.150) test results.

        "EVAP Monitor (0.020)," "EVAP Monitor (0.040)," "EVAP Monitor (0.090)," and "EVAP Monitor (Cap Off / 0.150)" refer to different types of 
        diagnostic tests or monitors performed by the ECU to assess the integrity of the evaporative emission control system (EVAP) and detect leaks of different sizes.

        The numbers in parentheses (0.020, 0.040, 0.090, 0.150) represent the size of the leak being tested, measured in inches.

        The EVAP system is designed to capture fuel vapors from the fuel tank and prevent them from being released into the atmosphere.
        The captured vapors are then directed to the engine to be burned during the combustion process.
        The EVAP system includes components such as the charcoal canister, purge valve, vent valve, and fuel tank pressure sensor.

        The EVAP monitors are designed to detect leaks in the EVAP system that could allow fuel vapors to escape into the atmosphere.
        The ECU performs these tests by pressurizing the EVAP system and monitoring the pressure changes over time. 

        The specific leak size being tested determines the type of EVAP monitor:
        - EVAP Monitor (0.020)
            - This monitor tests for very small leaks in the EVAP system, equivalent to a hole size of 0.020 inches in diameter.
        - EVAP Monitor (0.040)
            - This monitor tests for small leaks in the EVAP system, equivalent to a hole size of 0.040 inches in diameter.
        - EVAP Monitor (0.090)
            - This monitor tests for medium-sized leaks in the EVAP system, equivalent to a hole size of 0.090 inches in diameter.
        - EVAP Monitor (Cap Off / 0.150)
            - This monitor tests for large leaks in the EVAP system, equivalent to a hole size of 0.150 inches in diameter. 
                This test is also used to detect scenarios where the fuel cap is missing or not properly tightened.

        If the ECU detects a leak during any of these tests, it will trigger a diagnostic trouble code (DTC) and illuminate the check engine light.
        The specific DTC will indicate the type and size of the leak detected, allowing technicians to diagnose and repair the issue.

        Returns
        -------
        `str`
            EVAP (Cap Off / 0.150) Monitor test results.
        """
        response: OBDMonitorResponse = self.__connection.query(obd.commands.MONITOR_EVAP_150)
        tests: list[MonitorTest] = response.tests
        tests_str: str = "EVAP Monitor (Cap Off / 0.150) test results:\n" + str(response)
        return tests_str
    


    def cylinder1_misfire(self) -> str:
        """
        Fetches Misfire Monitor [Cylinder 1] test results.

        "Misfire Monitors" refer to diagnostic monitors that continuously assess the performance of each individual cylinder in the engine for misfires.
        A misfire occurs when a cylinder fails to properly ignite the air-fuel mixture, resulting in incomplete or skipped combustion.

        The misfire monitors are designed to detect misfires in real-time and identify the specific cylinder(s) where the misfire is occurring.
        The ECU uses various sensors, such as the crankshaft position sensor and camshaft position sensor, to monitor the rotational speed and acceleration of the engine's crankshaft.
        By analyzing this data, the ECU can detect variations in crankshaft speed that are indicative of a misfire.

        Each misfire monitor corresponds to a specific cylinder in the engine:
        - Misfire Monitor Cylinder 1
            - This monitor tests for misfires in cylinder 1.
        - Misfire Monitor Cylinder 2
            - This monitor tests for misfires in cylinder 2.
        - Misfire Monitor Cylinder 3
            - This monitor tests for misfires in cylinder 3.
        - Misfire Monitor Cylinder 4
            - This monitor tests for misfires in cylinder 4.

        If the ECU detects a misfire in one or more cylinders, it will trigger a diagnostic trouble code (DTC) and may illuminate the check engine light.
        Misfires can be caused by various factors, including faulty spark plugs, ignition coils, fuel injectors, or mechanical issues within the engine.

        Returns
        -------
        `str`
            Misfire Monitor [Cylinder 1] test results.
        """
        # https://python-obd.readthedocs.io/en/latest/Responses/#monitors-mode-06-responses  -  for more info on MonitorTest
        response: OBDMonitorResponse = self.__connection.query(obd.commands.MONITOR_MISFIRE_CYLINDER_1)
        tests: list[MonitorTest] = response.tests
        tests_str: str = "Misfire Monitor [Cylinder 1] test results:\n" + str(response)
        return tests_str
    


    def cylinder2_misfire(self) -> str:
        """
        Fetches Misfire Monitor [Cylinder 2] test results.

        "Misfire Monitors" refer to diagnostic monitors that continuously assess the performance of each individual cylinder in the engine for misfires.
        A misfire occurs when a cylinder fails to properly ignite the air-fuel mixture, resulting in incomplete or skipped combustion.

        The misfire monitors are designed to detect misfires in real-time and identify the specific cylinder(s) where the misfire is occurring.
        The ECU uses various sensors, such as the crankshaft position sensor and camshaft position sensor, to monitor the rotational speed and acceleration of the engine's crankshaft.
        By analyzing this data, the ECU can detect variations in crankshaft speed that are indicative of a misfire.

        Each misfire monitor corresponds to a specific cylinder in the engine:
        - Misfire Monitor Cylinder 1
            - This monitor tests for misfires in cylinder 1.
        - Misfire Monitor Cylinder 2
            - This monitor tests for misfires in cylinder 2.
        - Misfire Monitor Cylinder 3
            - This monitor tests for misfires in cylinder 3.
        - Misfire Monitor Cylinder 4
            - This monitor tests for misfires in cylinder 4.

        If the ECU detects a misfire in one or more cylinders, it will trigger a diagnostic trouble code (DTC) and may illuminate the check engine light.
        Misfires can be caused by various factors, including faulty spark plugs, ignition coils, fuel injectors, or mechanical issues within the engine.

        Returns
        -------
        `str`
            Misfire Monitor [Cylinder 2] test results.
        """
        # https://python-obd.readthedocs.io/en/latest/Responses/#monitors-mode-06-responses  -  for more info on MonitorTest
        response: OBDMonitorResponse = self.__connection.query(obd.commands.MONITOR_MISFIRE_CYLINDER_2)
        tests: list[MonitorTest] = response.tests
        tests_str: str = "Misfire Monitor [Cylinder 2] test results:\n" + str(response)
        return tests_str
    


    def cylinder3_misfire(self) -> str:
        """
        Fetches Misfire Monitor [Cylinder 3] test results.

        "Misfire Monitors" refer to diagnostic monitors that continuously assess the performance of each individual cylinder in the engine for misfires.
        A misfire occurs when a cylinder fails to properly ignite the air-fuel mixture, resulting in incomplete or skipped combustion.

        The misfire monitors are designed to detect misfires in real-time and identify the specific cylinder(s) where the misfire is occurring.
        The ECU uses various sensors, such as the crankshaft position sensor and camshaft position sensor, to monitor the rotational speed and acceleration of the engine's crankshaft.
        By analyzing this data, the ECU can detect variations in crankshaft speed that are indicative of a misfire.

        Each misfire monitor corresponds to a specific cylinder in the engine:
        - Misfire Monitor Cylinder 1
            - This monitor tests for misfires in cylinder 1.
        - Misfire Monitor Cylinder 2
            - This monitor tests for misfires in cylinder 2.
        - Misfire Monitor Cylinder 3
            - This monitor tests for misfires in cylinder 3.
        - Misfire Monitor Cylinder 4
            - This monitor tests for misfires in cylinder 4.

        If the ECU detects a misfire in one or more cylinders, it will trigger a diagnostic trouble code (DTC) and may illuminate the check engine light.
        Misfires can be caused by various factors, including faulty spark plugs, ignition coils, fuel injectors, or mechanical issues within the engine.

        Returns
        -------
        `str`
            Misfire Monitor [Cylinder 3] test results.
        """
        # https://python-obd.readthedocs.io/en/latest/Responses/#monitors-mode-06-responses  -  for more info on MonitorTest
        response: OBDMonitorResponse = self.__connection.query(obd.commands.MONITOR_MISFIRE_CYLINDER_3)
        tests: list[MonitorTest] = response.tests
        tests_str: str = "Misfire Monitor [Cylinder 3] test results:\n" + str(response)
        return tests_str
    


    def cylinder4_misfire(self) -> str:
        """
        Fetches Misfire Monitor [Cylinder 4] test results.

        "Misfire Monitors" refer to diagnostic monitors that continuously assess the performance of each individual cylinder in the engine for misfires.
        A misfire occurs when a cylinder fails to properly ignite the air-fuel mixture, resulting in incomplete or skipped combustion.

        The misfire monitors are designed to detect misfires in real-time and identify the specific cylinder(s) where the misfire is occurring.
        The ECU uses various sensors, such as the crankshaft position sensor and camshaft position sensor, to monitor the rotational speed and acceleration of the engine's crankshaft.
        By analyzing this data, the ECU can detect variations in crankshaft speed that are indicative of a misfire.

        Each misfire monitor corresponds to a specific cylinder in the engine:
        - Misfire Monitor Cylinder 1
            - This monitor tests for misfires in cylinder 1.
        - Misfire Monitor Cylinder 2
            - This monitor tests for misfires in cylinder 2.
        - Misfire Monitor Cylinder 3
            - This monitor tests for misfires in cylinder 3.
        - Misfire Monitor Cylinder 4
            - This monitor tests for misfires in cylinder 4.

        If the ECU detects a misfire in one or more cylinders, it will trigger a diagnostic trouble code (DTC) and may illuminate the check engine light.
        Misfires can be caused by various factors, including faulty spark plugs, ignition coils, fuel injectors, or mechanical issues within the engine.

        Returns
        -------
        `str`
            Misfire Monitor [Cylinder 4] test results.
        """
        # https://python-obd.readthedocs.io/en/latest/Responses/#monitors-mode-06-responses  -  for more info on MonitorTest
        response: OBDMonitorResponse = self.__connection.query(obd.commands.MONITOR_MISFIRE_CYLINDER_4)
        tests: list[MonitorTest] = response.tests
        tests_str: str = "Misfire Monitor [Cylinder 4] test results:\n" + str(response)
        return tests_str
    


    def general_misfire(self) -> str:
        """
        Fetches General Misfire Monitor [Any Cylinder] test results.

        "Misfire Monitor General" refers to a diagnostic monitor that assesses the overall performance of the engine for misfires without specifying a particular cylinder.
        A misfire occurs when one or more of the engine's cylinders fail to properly ignite the air-fuel mixture, resulting in incomplete or skipped combustion.

        The Misfire Monitor General is designed to detect misfires in real-time across all cylinders in the engine.
        The ECU uses various sensors, such as the crankshaft position sensor, to monitor the rotational speed and acceleration of the engine's crankshaft.
        By analyzing this data, the ECU can detect variations in crankshaft speed that are indicative of a misfire.

        If the ECU detects a misfire through the Misfire Monitor General, it will trigger a diagnostic trouble code (DTC) and may illuminate the check engine light. 
        The DTC associated with the Misfire Monitor General typically indicates that a misfire has been detected, but it does not specify which cylinder(s) experienced the misfire.

        Returns
        -------
        `str`
            General Misfire Monitor [Any Cylinder] test results.
        """
        # https://python-obd.readthedocs.io/en/latest/Responses/#monitors-mode-06-responses  -  for more info on MonitorTest
        response: OBDMonitorResponse = self.__connection.query(obd.commands.MONITOR_MISFIRE_GENERAL)
        tests: list[MonitorTest] = response.tests
        tests_str: str = "General Misfire Monitor [Any Cylinder] test results:\n" + str(response)
        return tests_str
    


    def O2Sensor_bank1sensor1(self) -> str:
        """
        Fetches O2 Sensor Monitor [Bank 1, Sensor 1] test results.

        "O2 Sensor Bank1, Sensor 1 Monitor" refers to a diagnostic monitor that assesses the performance and functionality of the primary (pre-catalytic converter) oxygen sensor for the engine cylinders in Bank 1.
        This oxygen sensor, also known as Sensor 1, is typically located in the exhaust manifold or exhaust pipe before the catalytic converter.

        The primary oxygen sensor plays a crucial role in engine performance, fuel efficiency, and emissions control. 
        It measures the oxygen content in the exhaust gases and provides real-time feedback to the ECU about the air-fuel mixture in the combustion chamber. 
        The ECU uses this information to adjust the air-fuel ratio to maintain optimal combustion and minimize emissions.

        The O2 Sensor Bank1, Sensor 1 Monitor continuously evaluates the oxygen sensor's response time, signal voltage, and overall performance to ensure it is functioning properly. 
        The monitor checks for issues such as slow response time, signal voltage outside the expected range, or sensor malfunction.

        Returns
        -------
        `str`
            O2 Sensor Monitor [Bank 1, Sensor 1] test results.
        """
        response: OBDMonitorResponse = self.__connection.query(obd.commands.MONITOR_O2_B1S1)
        tests: list[MonitorTest] = response.tests
        tests_str: str = "O2 Sensor [Bank 1, Sensor 1] Monitor test results:\n" + str(response)
        return tests_str
    


    def O2Sensor_bank1sensor2(self) -> str:
        """
        Fetches O2 Sensor Monitor [Bank 1, Sensor 2] test results.

        "O2 Sensor Bank1, Sensor 2 Monitor" refers to a diagnostic monitor that assesses the performance and functionality of the secondary (post-catalytic converter) oxygen sensor for the engine cylinders in Bank 1.
        This oxygen sensor, also known as Sensor 2, is typically located in the exhaust pipe after the catalytic converter.

        The primary purpose of the secondary oxygen sensor is to monitor the efficiency of the catalytic converter, which is responsible for reducing harmful emissions. 
        The sensor measures the oxygen content in the exhaust gases after they have passed through the catalytic converter. 
        By comparing the readings from the primary and secondary oxygen sensors, the ECU can determine how effectively the catalytic converter is reducing pollutants in the exhaust.

        The O2 Sensor Bank1, Sensor 2 Monitor continuously evaluates the oxygen sensor's signal voltage and overall performance to ensure it is functioning properly. 
        The monitor checks for issues such as signal voltage outside the expected range, sensor malfunction, or a catalytic converter that is not performing efficiently.

        Returns
        -------
        `str`
            O2 Sensor Monitor [Bank 1, Sensor 2] test results.
        """
        response: OBDMonitorResponse = self.__connection.query(obd.commands.MONITOR_O2_B1S2)
        tests: list[MonitorTest] = response.tests
        tests_str: str = "O2 Sensor [Bank 1, Sensor 2] Monitor test results:\n" + str(response)
        return tests_str
    


    def O2SensorHeater_bank1sensor1(self) -> str:
        """
        Fetches O2 Sensor Heater Monitor [Bank 1, Sensor 1] test results.

        "O2 Sensor Bank1, Sensor 1 Heater Monitor" refers to a diagnostic monitor that assesses the performance and functionality of the heater element within the primary (pre-catalytic converter) oxygen sensor for the engine cylinders in Bank 1. 
        This oxygen sensor, also known as Sensor 1, is typically located in the exhaust manifold or exhaust pipe before the catalytic converter.

        Modern oxygen sensors are equipped with a built-in heater element that helps bring the sensor up to its operating temperature more quickly. 
        The heater element is important because oxygen sensors need to reach a certain temperature (usually around `600 °F` or `315 °C`) to provide accurate and reliable readings. 
        By heating the sensor, the ECU ensures that it starts providing accurate feedback on the air-fuel mixture shortly after the engine is started.

        The O2 Sensor Bank1, Sensor 1 Heater Monitor continuously evaluates the performance of the oxygen sensor's heater element, including its resistance, current draw, and ability to reach and maintain the required operating temperature. 
        The monitor checks for issues such as an open or shorted heater circuit, excessive current draw, or a malfunctioning heater element.

        Returns
        -------
        `str`
            O2 Sensor Heater Monitor [Bank 1, Sensor 1] test results.
        """
        response: OBDMonitorResponse = self.__connection.query(obd.commands.MONITOR_O2_HEATER_B1S1)
        tests: list[MonitorTest] = response.tests
        tests_str: str = "O2 Sensor Heater Monitor [Bank 1, Sensor 1] test results:\n" + str(response)
        return tests_str
    


    def O2SensorHeater_bank1sensor2(self) -> str:
        """
        Fetches O2 Sensor Heater Monitor [Bank 1, Sensor 2] test results.

        "O2 Sensor Bank1, Sensor 2 Heater Monitor" refers to a diagnostic monitor that assesses the performance and functionality of the heater element within the secondary (post-catalytic converter) oxygen sensor for the engine cylinders in Bank 1. 
        This oxygen sensor, also known as Sensor 2, is typically located in the exhaust pipe after the catalytic converter.

        Similar to the primary oxygen sensor, the secondary oxygen sensor is equipped with a built-in heater element that helps bring the sensor up to its operating temperature more quickly. 
        The heater element is important because oxygen sensors need to reach a certain temperature (usually around `600 °F` or `315 °C`) to provide accurate and reliable readings. 
        The heater ensures that the sensor starts providing feedback on the efficiency of the catalytic converter shortly after the engine is started.

        The O2 Sensor Bank1, Sensor 2 Heater Monitor continuously evaluates the performance of the oxygen sensor's heater element, including its resistance, current draw, and ability to reach and maintain the required operating temperature. 
        The monitor checks for issues such as an open or shorted heater circuit, excessive current draw, or a malfunctioning heater element.

        Returns
        -------
        `str`
            O2 Sensor Heater Monitor [Bank 1, Sensor 2] test results.
        """
        response: OBDMonitorResponse = self.__connection.query(obd.commands.MONITOR_O2_HEATER_B1S2)
        tests: list[MonitorTest] = response.tests
        tests_str: str = "O2 Sensor Heater Monitor [Bank 1, Sensor 2] test results:\n" + str(response)
        return tests_str
    


    def purge_flow(self) -> str:
        """
        Fetches Purge Flow Monitor test results.

        "Purge Flow Monitor" refers to a diagnostic monitor that assesses the performance and functionality of the evaporative emission control system's (EVAP) purge flow. 
        Specifically, it evaluates the operation of the purge valve (also known as the purge solenoid) and the flow of fuel vapors from the charcoal canister to the engine's intake manifold.

        The EVAP system is designed to capture fuel vapors from the fuel tank and prevent them from being released into the atmosphere. 
        The captured vapors are stored in the charcoal canister until the engine is running and the conditions are appropriate for purging. 
        At that time, the ECU opens the purge valve, allowing the fuel vapors to be drawn into the engine's intake manifold, where they are mixed with the incoming air and burned during the combustion process.

        The Purge Flow Monitor evaluates the purge valve's ability to open and close as commanded by the ECU, as well as the flow of fuel vapors from the charcoal canister to the engine. 
        The monitor checks for issues such as a stuck-open or stuck-closed purge valve, restricted or blocked purge flow, or a malfunctioning purge valve.

        Returns
        -------
        `str`
            Purge Flow Monitor test results.
        """
        response: OBDMonitorResponse = self.__connection.query(obd.commands.MONITOR_PURGE_FLOW)
        tests: list[MonitorTest] = response.tests
        tests_str: str = "Purge Flow Monitor test results:\n" + str(response)
        return tests_str
    


    def VVT_bank1(self) -> str:
        """
        Fetches VVT Monitor [Bank 1] test results.

        "VVT Bank 1 Monitor" refers to a diagnostic monitor that assesses the performance and functionality of the Variable Valve Timing (VVT) system for the engine cylinders in Bank 1. 
        The VVT system is designed to dynamically adjust the timing of the intake and/or exhaust valves to optimize engine performance, fuel efficiency, and emissions across a wide range of operating conditions.
        
        The VVT system typically consists of components such as camshaft phasers (also known as camshaft actuators), oil control solenoids, and camshaft position sensors. 
        The ECU controls the VVT system by sending signals to the oil control solenoids to adjust the position of the camshaft phasers, thereby altering the timing of the valves.

        The VVT Bank 1 Monitor continuously evaluates the operation of the VVT system for the engine cylinders in Bank 1. 
        It monitors parameters such as camshaft position, camshaft actuator operation, and oil control solenoid function. 
        The monitor checks for issues such as incorrect camshaft timing, sluggish or stuck camshaft phasers, malfunctioning oil control solenoids, or discrepancies between the desired and actual camshaft positions.
        
        Returns
        -------
        `str`
            VVT Monitor [Bank 1] test results.
        """
        response: OBDMonitorResponse = self.__connection.query(obd.commands.MONITOR_VVT_B1)
        tests: list[MonitorTest] = response.tests
        tests_str: str = "VVT [Bank 1] Monitor test results:\n" + str(response)
        return tests_str
    

