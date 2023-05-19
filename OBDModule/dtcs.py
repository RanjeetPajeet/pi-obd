"""
# dtcs.py

Defines the DTCs class, which is a container for OBD functions that involve Diagnostic Trouble Codes (DTCs).
"""

import obd
from typing import NamedTuple
from collections import namedtuple
from obd.OBDResponse import Status as OBDStatusResponse





class DTCs:
    """
    Collection of methods for Diagnostic Trouble Code (DTC) related OBD commands.
    """
    def __init__(self, connection: obd.OBD) -> "DTCs":
        self.__connection = connection

    
    def count(self) -> int:
        """
        Gets the number of Diagnostic Trouble Codes (DTCs) currently stored in the ECU's memory.

        DTCs are standardized alphanumeric codes that are stored in the ECU's memory when it detects a problem or malfunction in the vehicle's systems or components.

        DTCs are generated when the ECU receives data from various sensors and modules that falls outside of the expected or predefined parameters.
        When a fault is detected, the ECU records the corresponding DTC and may also trigger the Check Engine Light (CEL) or Malfunction Indicator Lamp (MIL) on the vehicle's dashboard to alert the driver to the issue.
        
        DTCs follow a standardized format defined by the Society of Automotive Engineers (SAE).
        
        A typical DTC consists of five characters:
        - The first character indicates the main system where the fault has occurred:
            - `P`: Powertrain (engine, transmission, etc.)
            - `B`: Body (climate control, lighting, etc.)
            - `C`: Chassis (brakes, suspension, etc.)
            - `U`: Network and vehicle integration (communication between control modules, etc.)
        - The second character specifies whether the code is manufacturer-specific (`1-3`) or generic, applicable to all vehicles (`0`).
        - The third character identifies the specific subsystem within the main system where the fault has occurred (e.g., fuel system, ignition system, etc.).
        - The fourth and fifth characters are a unique identifier for the specific fault or malfunction.

        For example, a DTC such as `P0302` indicates a "Powertrain" (`P`) generic code (`0`) related to the ignition system (`3`) and identifies a misfire detected in cylinder 2 (`02`).

        Returns
        -------
        `int`
            The total count, as an integer.
        """
        response = self.__connection.query(obd.commands.GET_DTC)
        return len(response.value)



    def distance_since_last_clear(self, as_meters: bool = False, as_feet: bool = False, as_miles: bool = False) -> float:
        """
        Gets the distance traveled since the Diagnostic Trouble Codes (DTCs) were last cleared.

        DTCs are standardized alphanumeric codes that are stored in the ECU's memory when it detects a problem or malfunction in the vehicle's systems or components.

        DTCs are generated when the ECU receives data from various sensors and modules that falls outside of the expected or predefined parameters.
        When a fault is detected, the ECU records the corresponding DTC and may also trigger the Check Engine Light (CEL) or Malfunction Indicator Lamp (MIL) on the vehicle's dashboard to alert the driver to the issue.
        
        DTCs follow a standardized format defined by the Society of Automotive Engineers (SAE).
        
        A typical DTC consists of five characters:
        - The first character indicates the main system where the fault has occurred:
            - `P`: Powertrain (engine, transmission, etc.)
            - `B`: Body (climate control, lighting, etc.)
            - `C`: Chassis (brakes, suspension, etc.)
            - `U`: Network and vehicle integration (communication between control modules, etc.)
        - The second character specifies whether the code is manufacturer-specific (`1-3`) or generic, applicable to all vehicles (`0`).
        - The third character identifies the specific subsystem within the main system where the fault has occurred (e.g., fuel system, ignition system, etc.).
        - The fourth and fifth characters are a unique identifier for the specific fault or malfunction.

        For example, a DTC such as `P0302` indicates a "Powertrain" (`P`) generic code (`0`) related to the ignition system (`3`) and identifies a misfire detected in cylinder 2 (`02`).

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
            The distance traveled since the DTCs were last cleared, in kilometers, meters, feet, or miles.
        """
        response = self.__connection.query(obd.commands.DISTANCE_SINCE_DTC_CLEAR)
        value = response.value.magnitude
        if as_meters:
            value = value * 1000
        elif as_feet:
            value = value * 3280.84
        elif as_miles:
            value = value * 0.621371
        return value
    


    def status_since_last_clear(self) -> NamedTuple:
        """
        Gets the status since the Diagnostic Trouble Codes (DTCs) were last cleared.

        The `STATUS` command returns information about the Malfunction Indicator Lamp (`MIL`) or Check Engine Light (`CEL`),
        the number of trouble codes being thrown, and the type of engine.

        Returns
        -------
        `NamedTuple`
            A NamedTuple containing the following values:
            - `is_MIL_on`: Whether the MIL is on or off.
            - `DTC_count`: The number of DTCs being thrown.

        Example
        -------
        ```
        status = car.DTCs.status_since_last_clear()

        print(status.is_MIL_on)
        >>> True

        print(status.DTC_count)
        >>> 1
        ```
        """
        response: OBDStatusResponse = self.__connection.query(obd.commands.STATUS)
        is_MIL_on = response.MIL
        DTC_count = response.DTC_count
        return namedtuple("Status", ["is_MIL_on", "DTC_count"])(is_MIL_on, DTC_count)
    


    def time_since_last_clear(self, as_minutes: bool = False, as_hours: bool = False) -> float:
        """
        Gets the time since the Diagnostic Trouble Codes (DTCs) were last cleared.

        Parameters
        ----------
        `as_minutes` : bool, optional
            Whether to return the time in minutes (default is seconds).
        `as_hours` : bool, optional
            Whether to return the time in hours (default is seconds).

        Returns
        -------
        `float`
            The time since the DTCs were last cleared, in seconds, minutes, or hours.
        """
        response = self.__connection.query(obd.commands.TIME_SINCE_DTC_CLEARED)
        value = response.value.magnitude
        value = value * 60  # default return value is in minutes, need to convert to seconds first
        if as_minutes:
            value = value / 60
        elif as_hours:
            value = value / 3600
        return value
    


    def warmups_since_last_clear(self) -> int:
        """
        Gets the number of warm-ups since the Diagnostic Trouble Codes (DTCs) were last cleared.

        Returns
        -------
        `int`
            The total count, as an integer.
        """
        response = self.__connection.query(obd.commands.WARMUPS_SINCE_DTC_CLEAR)
        return response.value.magnitude



    def read(self) -> NamedTuple:
        """
        Reads the Diagnostic Trouble Codes (DTCs) that are currently stored in the ECU's memory.

        DTCs are standardized alphanumeric codes that are stored in the ECU's memory when it detects a problem or malfunction in the vehicle's systems or components.

        DTCs are generated when the ECU receives data from various sensors and modules that falls outside of the expected or predefined parameters.
        When a fault is detected, the ECU records the corresponding DTC and may also trigger the Check Engine Light (CEL) or Malfunction Indicator Lamp (MIL) on the vehicle's dashboard to alert the driver to the issue.
        
        DTCs follow a standardized format defined by the Society of Automotive Engineers (SAE).
        
        A typical DTC consists of five characters:
        - The first character indicates the main system where the fault has occurred:
            - `P`: Powertrain (engine, transmission, etc.)
            - `B`: Body (climate control, lighting, etc.)
            - `C`: Chassis (brakes, suspension, etc.)
            - `U`: Network and vehicle integration (communication between control modules, etc.)
        - The second character specifies whether the code is manufacturer-specific (`1-3`) or generic, applicable to all vehicles (`0`).
        - The third character identifies the specific subsystem within the main system where the fault has occurred (e.g., fuel system, ignition system, etc.).
        - The fourth and fifth characters are a unique identifier for the specific fault or malfunction.

        For example, a DTC such as `P0302` indicates a "Powertrain" (`P`) generic code (`0`) related to the ignition system (`3`) and identifies a misfire detected in cylinder 2 (`02`).

        Returns
        -------
        `NamedTuple`
            A NamedTuple containing the following values:
            - `code`: The DTC code.
            - `description`: The description of the DTC code.
        
        Example
        -------
        ```
        dtcs = car.DTCs.read()

        for dtc in dtcs:
            print(dtc.code, ' -- ', dtc.description)

        >>> P0302  --  Cylinder 2 Misfire Detected
        >>> P0303  --  Cylinder 3 Misfire Detected
        ```
        """
        response = self.__connection.query(obd.commands.GET_DTC)
        if isinstance(response.value, tuple):   # only one DTC
            value = [response.value]            # convert to list of tuples of length 1
        else:
            value = response.value
        return [namedtuple("DTC", ["code", "description"])(code, description) for code, description in value]
    


    def read_from_latest_driving_cycle(self) -> NamedTuple:
        """
        Reads the Diagnostic Trouble Codes (DTCs) stored in the ECU's memory originating from the current/last driving cycle.

        DTCs are standardized alphanumeric codes that are stored in the ECU's memory when it detects a problem or malfunction in the vehicle's systems or components.

        DTCs are generated when the ECU receives data from various sensors and modules that falls outside of the expected or predefined parameters.
        When a fault is detected, the ECU records the corresponding DTC and may also trigger the Check Engine Light (CEL) or Malfunction Indicator Lamp (MIL) on the vehicle's dashboard to alert the driver to the issue.
        
        DTCs follow a standardized format defined by the Society of Automotive Engineers (SAE).
        
        A typical DTC consists of five characters:
        - The first character indicates the main system where the fault has occurred:
            - `P`: Powertrain (engine, transmission, etc.)
            - `B`: Body (climate control, lighting, etc.)
            - `C`: Chassis (brakes, suspension, etc.)
            - `U`: Network and vehicle integration (communication between control modules, etc.)
        - The second character specifies whether the code is manufacturer-specific (`1-3`) or generic, applicable to all vehicles (`0`).
        - The third character identifies the specific subsystem within the main system where the fault has occurred (e.g., fuel system, ignition system, etc.).
        - The fourth and fifth characters are a unique identifier for the specific fault or malfunction.

        For example, a DTC such as `P0302` indicates a "Powertrain" (`P`) generic code (`0`) related to the ignition system (`3`) and identifies a misfire detected in cylinder 2 (`02`).

        Returns
        -------
        `NamedTuple`
            A NamedTuple containing the following values:
            - `code`: The DTC code.
            - `description`: The description of the DTC code.

        Example
        -------
        ```
        dtcs = car.DTCs.read_from_latest_driving_cycle()

        for dtc in dtcs:
            print(dtc.code, ' -- ', dtc.description)

        >>> P0302  --  Cylinder 2 Misfire Detected
        >>> P0303  --  Cylinder 3 Misfire Detected
        ```
        """
        response = self.__connection.query(obd.commands.GET_CURRENT_DTC)
        if isinstance(response.value, tuple):   # only one DTC
            value = [response.value]            # convert to list of tuples of length 1
        else:
            value = response.value
        return [namedtuple("DTC", ["code", "description"])(code, description) for code, description in value]
    


    def clear(self) -> None:
        """
        Clears the Diagnostic Trouble Codes (DTCs) and freezes data from the ECU's memory.

        DTCs are standardized alphanumeric codes that are stored in the ECU's memory when it detects a problem or malfunction in the vehicle's systems or components.

        DTCs are generated when the ECU receives data from various sensors and modules that falls outside of the expected or predefined parameters.
        When a fault is detected, the ECU records the corresponding DTC and may also trigger the Check Engine Light (CEL) or Malfunction Indicator Lamp (MIL) on the vehicle's dashboard to alert the driver to the issue.
        
        DTCs follow a standardized format defined by the Society of Automotive Engineers (SAE).
        
        A typical DTC consists of five characters:
        - The first character indicates the main system where the fault has occurred:
            - `P`: Powertrain (engine, transmission, etc.)
            - `B`: Body (climate control, lighting, etc.)
            - `C`: Chassis (brakes, suspension, etc.)
            - `U`: Network and vehicle integration (communication between control modules, etc.)
        - The second character specifies whether the code is manufacturer-specific (`1-3`) or generic, applicable to all vehicles (`0`).
        - The third character identifies the specific subsystem within the main system where the fault has occurred (e.g., fuel system, ignition system, etc.).
        - The fourth and fifth characters are a unique identifier for the specific fault or malfunction.

        For example, a DTC such as `P0302` indicates a "Powertrain" (`P`) generic code (`0`) related to the ignition system (`3`) and identifies a misfire detected in cylinder 2 (`02`).

        Returns
        -------
        `None`
        """
        response = self.__connection.query(obd.commands.CLEAR_DTC)
        return response.value