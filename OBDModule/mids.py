"""
# mids.py

Defines the MIDs class, which stores methods for retrieving MIDs for the car.
"""

import obd
from obd.utils import BitArray







class MIDs:
    """
    Collection of 6 methods for retrieving MIDs from the car (A, B, C, D, E, F).
    """
    def __init__(self, connection: obd.OBD) -> "MIDs":
        self.__connection = connection

    
    def A(self) -> str:
        """
        Gets the supported MIDs [01-20].

        MIDs (Monitor IDs) A, B, C, D, E, and F refer to the groups of supported diagnostic tests or monitors 
        that the vehicle's ECU can perform to assess the performance and functionality of various emission-related systems and components.

        These diagnostic tests are also known as "Readiness Monitors" or "OBD Monitors."

        MIDs are organized into groups, with each group covering a specific range of monitors:
        - MID A (01-20): This group covers the first set of 32 monitors, ranging from 01 to 20.
        - MID B (21-40): This group covers the second set of 32 monitors, ranging from 21 to 40.
        - MID C (41-60): This group covers the third set of 32 monitors, ranging from 41 to 60.
        - MID D (61-80): This group covers the fourth set of 32 monitors, ranging from 61 to 80.
        - MID E (81-A0): This group covers the fifth set of 32 monitors, ranging from 81 to A0.
        - MID F (A1-C0): This group covers the sixth set of 32 monitors, ranging from A1 to C0.

        Each MID corresponds to a specific diagnostic test or monitor for a particular emission-related system or component, such as the oxygen sensor, catalytic converter, evaporative emissions system, and more.
        The ECU performs these tests under specific driving conditions to ensure that the vehicle's emission control systems are functioning properly and meet emissions standards.

        Returns
        -------
        `str`
            The supported MIDs [01-20].
        """
        response: BitArray = self.__connection.query(obd.commands.MIDS_A)
        return str(response)
    


    def B(self) -> str:
        """
        Gets the supported MIDs [21-40].

        MIDs (Monitor IDs) A, B, C, D, E, and F refer to the groups of supported diagnostic tests or monitors 
        that the vehicle's ECU can perform to assess the performance and functionality of various emission-related systems and components.

        These diagnostic tests are also known as "Readiness Monitors" or "OBD Monitors."

        MIDs are organized into groups, with each group covering a specific range of monitors:
        - MID A (01-20): This group covers the first set of 32 monitors, ranging from 01 to 20.
        - MID B (21-40): This group covers the second set of 32 monitors, ranging from 21 to 40.
        - MID C (41-60): This group covers the third set of 32 monitors, ranging from 41 to 60.
        - MID D (61-80): This group covers the fourth set of 32 monitors, ranging from 61 to 80.
        - MID E (81-A0): This group covers the fifth set of 32 monitors, ranging from 81 to A0.
        - MID F (A1-C0): This group covers the sixth set of 32 monitors, ranging from A1 to C0.

        Each MID corresponds to a specific diagnostic test or monitor for a particular emission-related system or component, such as the oxygen sensor, catalytic converter, evaporative emissions system, and more.
        The ECU performs these tests under specific driving conditions to ensure that the vehicle's emission control systems are functioning properly and meet emissions standards.

        Returns
        -------
        `str`
            The supported MIDs [21-40].
        """
        response: BitArray = self.__connection.query(obd.commands.MIDS_B)
        return str(response)
    


    def C(self) -> str:
        """
        Gets the supported MIDs [41-60].

        MIDs (Monitor IDs) A, B, C, D, E, and F refer to the groups of supported diagnostic tests or monitors 
        that the vehicle's ECU can perform to assess the performance and functionality of various emission-related systems and components.

        These diagnostic tests are also known as "Readiness Monitors" or "OBD Monitors."

        MIDs are organized into groups, with each group covering a specific range of monitors:
        - MID A (01-20): This group covers the first set of 32 monitors, ranging from 01 to 20.
        - MID B (21-40): This group covers the second set of 32 monitors, ranging from 21 to 40.
        - MID C (41-60): This group covers the third set of 32 monitors, ranging from 41 to 60.
        - MID D (61-80): This group covers the fourth set of 32 monitors, ranging from 61 to 80.
        - MID E (81-A0): This group covers the fifth set of 32 monitors, ranging from 81 to A0.
        - MID F (A1-C0): This group covers the sixth set of 32 monitors, ranging from A1 to C0.

        Each MID corresponds to a specific diagnostic test or monitor for a particular emission-related system or component, such as the oxygen sensor, catalytic converter, evaporative emissions system, and more.
        The ECU performs these tests under specific driving conditions to ensure that the vehicle's emission control systems are functioning properly and meet emissions standards.

        Returns
        -------
        `str`
            The supported MIDs [41-60].
        """
        response: BitArray = self.__connection.query(obd.commands.MIDS_C)
        return str(response)
    


    def D(self) -> str:
        """
        Gets the supported MIDs [61-80].

        MIDs (Monitor IDs) A, B, C, D, E, and F refer to the groups of supported diagnostic tests or monitors 
        that the vehicle's ECU can perform to assess the performance and functionality of various emission-related systems and components.

        These diagnostic tests are also known as "Readiness Monitors" or "OBD Monitors."

        MIDs are organized into groups, with each group covering a specific range of monitors:
        - MID A (01-20): This group covers the first set of 32 monitors, ranging from 01 to 20.
        - MID B (21-40): This group covers the second set of 32 monitors, ranging from 21 to 40.
        - MID C (41-60): This group covers the third set of 32 monitors, ranging from 41 to 60.
        - MID D (61-80): This group covers the fourth set of 32 monitors, ranging from 61 to 80.
        - MID E (81-A0): This group covers the fifth set of 32 monitors, ranging from 81 to A0.
        - MID F (A1-C0): This group covers the sixth set of 32 monitors, ranging from A1 to C0.

        Each MID corresponds to a specific diagnostic test or monitor for a particular emission-related system or component, such as the oxygen sensor, catalytic converter, evaporative emissions system, and more.
        The ECU performs these tests under specific driving conditions to ensure that the vehicle's emission control systems are functioning properly and meet emissions standards.

        Returns
        -------
        `str`
            The supported MIDs [61-80].
        """
        response: BitArray = self.__connection.query(obd.commands.MIDS_D)
        return str(response)
    


    def E(self) -> str:
        """
        Gets the supported MIDs [81-A0].

        MIDs (Monitor IDs) A, B, C, D, E, and F refer to the groups of supported diagnostic tests or monitors 
        that the vehicle's ECU can perform to assess the performance and functionality of various emission-related systems and components.

        These diagnostic tests are also known as "Readiness Monitors" or "OBD Monitors."

        MIDs are organized into groups, with each group covering a specific range of monitors:
        - MID A (01-20): This group covers the first set of 32 monitors, ranging from 01 to 20.
        - MID B (21-40): This group covers the second set of 32 monitors, ranging from 21 to 40.
        - MID C (41-60): This group covers the third set of 32 monitors, ranging from 41 to 60.
        - MID D (61-80): This group covers the fourth set of 32 monitors, ranging from 61 to 80.
        - MID E (81-A0): This group covers the fifth set of 32 monitors, ranging from 81 to A0.
        - MID F (A1-C0): This group covers the sixth set of 32 monitors, ranging from A1 to C0.

        Each MID corresponds to a specific diagnostic test or monitor for a particular emission-related system or component, such as the oxygen sensor, catalytic converter, evaporative emissions system, and more.
        The ECU performs these tests under specific driving conditions to ensure that the vehicle's emission control systems are functioning properly and meet emissions standards.

        Returns
        -------
        `str`
            The supported MIDs [81-A0].
        """
        response: BitArray = self.__connection.query(obd.commands.MIDS_E)
        return str(response)
    


    def F(self) -> str:
        """
        Gets the supported MIDs [A1-C0].

        MIDs (Monitor IDs) A, B, C, D, E, and F refer to the groups of supported diagnostic tests or monitors 
        that the vehicle's ECU can perform to assess the performance and functionality of various emission-related systems and components.

        These diagnostic tests are also known as "Readiness Monitors" or "OBD Monitors."

        MIDs are organized into groups, with each group covering a specific range of monitors:
        - MID A (01-20): This group covers the first set of 32 monitors, ranging from 01 to 20.
        - MID B (21-40): This group covers the second set of 32 monitors, ranging from 21 to 40.
        - MID C (41-60): This group covers the third set of 32 monitors, ranging from 41 to 60.
        - MID D (61-80): This group covers the fourth set of 32 monitors, ranging from 61 to 80.
        - MID E (81-A0): This group covers the fifth set of 32 monitors, ranging from 81 to A0.
        - MID F (A1-C0): This group covers the sixth set of 32 monitors, ranging from A1 to C0.

        Each MID corresponds to a specific diagnostic test or monitor for a particular emission-related system or component, such as the oxygen sensor, catalytic converter, evaporative emissions system, and more.
        The ECU performs these tests under specific driving conditions to ensure that the vehicle's emission control systems are functioning properly and meet emissions standards.

        Returns
        -------
        `str`
            The supported MIDs [A1-C0].
        """
        response: BitArray = self.__connection.query(obd.commands.MIDS_F)
        return str(response)
    

    