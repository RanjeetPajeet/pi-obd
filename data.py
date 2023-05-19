"""
data.py
-------

Data class.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

to_f = lambda c: c * 9/5 + 32
to_psi = lambda kPa: kPa * 0.145038
to_mph = lambda m_per_s: m_per_s * 2.23694




class Data:
    def __init__(self, filename: str):
        self._file = filename
        self._data = pd.read_csv(self._file, sep=',', names=[
            'timestamp',                         'speed',                              'rpm',
            'calculated_engine_load',            'absolute_engine_load',               'relative_throttle_pos',
            'absolute_throttle_pos',             'timing_advance',                     'fuel_rail_pressure',
            'intake_manifold_pressure',          'coolant_temperature',                'fuel_level',
            'catalyst_temperature_bank1sensor1', 'catalyst_temperature_bank1sensor2',  'o2_bank1sensor2_voltage',
            'o2_bank1sensor1_wr_lambda_current', 'short_term_fuel_trim_bank1',         'short_term_o2_trim_bank1',
        ], skiprows=1)
        self._data['timestamp'] = self._data['timestamp'].apply(lambda x: x - self._data['timestamp'][0])
        self._data['speed'] = self._data['speed'].apply(lambda x: to_mph(x))
        self._data['fuel_rail_pressure'] = self._data['fuel_rail_pressure'].apply(lambda x: to_psi(x))
        self._data['intake_manifold_pressure'] = self._data['intake_manifold_pressure'].apply(lambda x: to_psi(x))
        self._data['coolant_temperature'] = self._data['coolant_temperature'].apply(lambda x: to_f(x))
        self._data['catalyst_temperature_bank1sensor1'] = self._data['catalyst_temperature_bank1sensor1'].apply(lambda x: to_f(x))
        self._data['catalyst_temperature_bank1sensor2'] = self._data['catalyst_temperature_bank1sensor2'].apply(lambda x: to_f(x))

    @property
    def data(self) -> pd.DataFrame:
        return self._data
    
    @property
    def timestamps(self) -> pd.Series:
        return self._data['timestamp']
    
    @property
    def speed(self) -> pd.Series:
        return self._data['speed']
    
    @property
    def rpm(self) -> pd.Series:
        return self._data['rpm']
    
    @property
    def calculated_engine_load(self) -> pd.Series:
        return self._data['calculated_engine_load']
    
    @property
    def absolute_engine_load(self) -> pd.Series:
        return self._data['absolute_engine_load']
    
    @property
    def relative_throttle_pos(self) -> pd.Series:
        return self._data['relative_throttle_pos']
    
    @property
    def absolute_throttle_pos(self) -> pd.Series:
        return self._data['absolute_throttle_pos']
    
    @property
    def timing_advance(self) -> pd.Series:
        return self._data['timing_advance']
    
    @property
    def fuel_rail_pressure(self) -> pd.Series:
        return self._data['fuel_rail_pressure']
    
    @property
    def intake_manifold_pressure(self) -> pd.Series:
        return self._data['intake_manifold_pressure']
    
    @property
    def coolant_temperature(self) -> pd.Series:
        return self._data['coolant_temperature']
    
    @property
    def fuel_level(self) -> pd.Series:
        return self._data['fuel_level']
    
    @property
    def catalyst_temperature_bank1sensor1(self) -> pd.Series:
        return self._data['catalyst_temperature_bank1sensor1']
    
    @property
    def catalyst_temperature_bank1sensor2(self) -> pd.Series:
        return self._data['catalyst_temperature_bank1sensor2']
    
    @property
    def o2_bank1sensor2_voltage(self) -> pd.Series:
        return self._data['o2_bank1sensor2_voltage']
    
    @property
    def o2_bank1sensor1_wr_lambda_current(self) -> pd.Series:
        return self._data['o2_bank1sensor1_wr_lambda_current']
    
    @property
    def short_term_fuel_trim_bank1(self) -> pd.Series:
        return self._data['short_term_fuel_trim_bank1']
    
    @property
    def short_term_o2_trim_bank1(self) -> pd.Series:
        return self._data['short_term_o2_trim_bank1']
    



# if __name__ == "__main__":
#     data = Data('data_txt.txt')

#     print(data.data.head())

#     plt.figure(figsize=(12,9))
#     # plt.plot(data.timestamps, data.speed, label='speed')
#     plt.plot(data.timestamps, data.rpm, label='rpm')
#     # plt.plot(data.timestamps, data.calculated_engine_load, label='calculated_engine_load')
#     # plt.plot(data.timestamps, data.absolute_engine_load, label='absolute_engine_load')
#     # plt.plot(data.timestamps, data.relative_throttle_pos, label='relative_throttle_pos')
#     # plt.plot(data.timestamps, data.absolute_throttle_pos, label='absolute_throttle_pos')
#     # plt.plot(data.timestamps, data.timing_advance, label='timing_advance')
#     # plt.plot(data.timestamps, data.fuel_rail_pressure, label='fuel_rail_pressure')
#     # plt.plot(data.timestamps, data.intake_manifold_pressure, label='intake_manifold_pressure')
#     # plt.plot(data.timestamps, data.coolant_temperature, label='coolant_temperature')
#     # plt.plot(data.timestamps, data.fuel_level, label='fuel_level')
#     plt.plot(data.timestamps, data.catalyst_temperature_bank1sensor1, label='catalyst_temperature_bank1sensor1')
#     plt.plot(data.timestamps, data.catalyst_temperature_bank1sensor2, label='catalyst_temperature_bank1sensor2')
#     # plt.plot(data.timestamps, data.o2_bank1sensor2_voltage, label='o2_bank1sensor2_voltage')
#     # plt.plot(data.timestamps, data.o2_bank1sensor1_wr_lambda_current, label='o2_bank1sensor1_wr_lambda_current')
#     # plt.plot(data.timestamps, data.short_term_fuel_trim_bank1, label='short_term_fuel_trim_bank1')
#     # plt.plot(data.timestamps, data.short_term_o2_trim_bank1, label='short_term_o2_trim_bank1')
#     plt.legend()
#     plt.show()

    