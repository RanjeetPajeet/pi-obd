"""
st_app.py
---------

Streamlit app for visualizing data.
"""
import datetime
import numpy as np
import pandas as pd
from data import Data
import streamlit as st
from github import Github
import matplotlib.pyplot as plt
from dataclasses import dataclass
from collections import namedtuple
from scipy.signal import savgol_filter

# ACCESS_TOKEN = "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"     # makaufmanUI
ACCESS_TOKEN = "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"       # ranjeetpajeet
g = Github(ACCESS_TOKEN)
repo = g.get_repo('ranjeetpajeet/pi-obd')

def get_most_recent_data_file():
    contents = repo.get_contents("data")
    most_recent = None
    for content_file in contents:
        filename = content_file.name
        filedate = datetime.datetime.strptime(filename, "%Y-%m-%d_%H-%M-%S.txt")
        if most_recent is None or filedate > most_recent:
            most_recent = filedate
    return f'data/{most_recent.strftime("%Y-%m-%d_%H-%M-%S.txt")}'

def get_all_data_files(sort_by_date: bool = True):
    contents = repo.get_contents("data")
    files = []
    for content_file in contents:
        filename = content_file.name
        files.append(filename)
    if sort_by_date:
        files.sort(key=lambda x: datetime.datetime.strptime(x, "%Y-%m-%d_%H-%M-%S.txt"))
    return files


st.set_page_config(
    layout     = "centered",
    page_icon  = "📊",
    page_title = "OBD2 Data Visualization"
)
st.markdown(body=\
    """ <style>
    section.main > div {max-width:50rem}
    </style> """, unsafe_allow_html=True
)


# @st.cache
# def load_data() -> Data:
#     return Data('data_txt.txt')

# load data
if 'data' not in st.session_state:
    st.session_state.data = load_data()


@dataclass
class EngineLoad:
    absolute: pd.Series
    calculated: pd.Series

@dataclass
class ThrottlePosition:
    relative: pd.Series
    absolute: pd.Series

@dataclass
class CatalystTemperature:
    pre_cat: pd.Series
    post_cat: pd.Series

@dataclass
class O2Sensor:
    pre_cat_current: pd.Series
    post_cat_voltage: pd.Series

@dataclass
class Fuel:
    level: pd.Series
    rail_pressure: pd.Series

@dataclass
class ShortTermTrim:
    o2: pd.Series
    fuel: pd.Series



@st.cache
def plot_data(x: pd.Series, y: pd.Series, xlabel: str, ylabel: str, title: str = None, savgol: bool = False, savgol_window_length: int = 51, savgol_polyorder: int = 3) -> None:
    if savgol:
        y = savgol_filter(y, savgol_window_length, savgol_polyorder)
    plt.plot(x, y)
    if title is not None:
        plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    st.pyplot()


@st.cache
def plot_data_many(x: pd.Series, ys: list[pd.Series], xlabel: str, titles: list[str], ylabel: str = None, savgol: bool = False, savgol_window_length: int = 51, savgol_polyorder: int = 3) -> None:
    if savgol:
        for i in range(len(ys)):
            ys[i] = savgol_filter(ys[i], savgol_window_length, savgol_polyorder)
    for i in range(len(ys)):
        plt.plot(x, ys[i], label=titles[i])
    plt.title(titles[0])
    plt.xlabel(xlabel)
    if ylabel is not None:
        plt.ylabel(ylabel)
    plt.legend()
    st.pyplot()




# data = st.session_state.data
# timestamps = data.timestamps

# rpm = data.rpm
# speed = data.speed
# timing_advance = data.timing_advance
# coolant_temperature = data.coolant_temperature
# intake_manifold_pressure = data.intake_manifold_pressure

# fuel = Fuel(data.fuel_level, data.fuel_rail_pressure)
# engine_load = EngineLoad(data.absolute_engine_load, data.calculated_engine_load)
# o2_sensor = O2Sensor(data.o2_bank1sensor1_wr_lambda_current, data.o2_bank1sensor2_voltage)
# throttle_position = ThrottlePosition(data.relative_throttle_pos, data.absolute_throttle_pos)
# short_term_trim = ShortTermTrim(data.short_term_o2_trim_bank1, data.short_term_fuel_trim_bank1)
# catalyst_temperature = CatalystTemperature(data.catalyst_temperature_bank1sensor1, data.catalyst_temperature_bank1sensor2)




st.title("OBD2 Data Visualization")
st.markdown("---")
# st.markdown("# ")


# Sidebar
st.sidebar.title("Options")
st.sidebar.markdown("---")
st.sidebar.markdown("# Data")
st.sidebar.write(" ")
data_file = st.sidebar.selectbox("Data file", options=[*get_all_data_files()], index=0, key="data_file", help="Select the data file to use for visualization.")
st.sidebar.markdown("---")
st.sidebar.markdown("# Plotting")
st.sidebar.write(" ")
use_savgol = st.sidebar.checkbox("Use Savitzky-Golay filter", value=False, key="use_savgol", help="Use Savitzky-Golay filter to smooth data.")
savgol_window_length = st.sidebar.slider("Savitzky-Golay window length", min_value=3, max_value=101, value=51, step=2, key="savgol_window_length", help="Window length of Savitzky-Golay filter.")
savgol_polyorder = st.sidebar.slider("Savitzky-Golay polynomial order", min_value=1, max_value=10, value=3, step=1, key="savgol_polyorder", help="Polynomial order of Savitzky-Golay filter.")
st.sidebar.markdown("---")


# Main
st.markdown("### Data to Visualize")
st.markdown("### ")
# rpm_col, speed_col, timing_advance_col, coolant_temperature_col, intake_manifold_pressure_col = st.columns(5)
# rpm_col.metric(label="RPM", value=f"{rpm.iloc[-1]:.0f}", delta=f"{rpm.iloc[-1] - rpm.iloc[-2]:.0f}", delta_color="inverse")
# speed_col.metric(label="Speed", value=f"{speed.iloc[-1]:.0f}", delta=f"{speed.iloc[-1] - speed.iloc[-2]:.0f}", delta_color="inverse")

rpm_checkbox = st.checkbox("RPM", value=False, key="rpm_checkbox")

col1a, col2a = st.columns(2)
with col1a:
    speed_checkbox = st.checkbox("Speed", value=False, key="speed_checkbox")
with col2a:
    fuel_level_checkbox = st.checkbox("Fuel Level", value=False, key="fuel_level_checkbox")
    

col1, col2 = st.columns(2)
with col1:
    timing_advance_checkbox = st.checkbox("Timing Advance", value=False, key="timing_advance_checkbox")
    fuel_rail_pressure_checkbox = st.checkbox("Fuel Rail Pressure", value=False, key="fuel_rail_pressure_checkbox")
    short_term_o2_trim_checkbox = st.checkbox("Short Term O2 Trim", value=False, key="short_term_o2_trim_checkbox")
    short_term_fuel_trim_checkbox = st.checkbox("Short Term Fuel Trim", value=False, key="short_term_fuel_trim_checkbox")
    coolant_temperature_checkbox = st.checkbox("Coolant Temperature", value=False, key="coolant_temperature_checkbox")
    absolute_engine_load_checkbox = st.checkbox("Absolute Engine Load", value=False, key="absolute_engine_load_checkbox")
    calculated_engine_load_checkbox = st.checkbox("Calculated Engine Load", value=False, key="calculated_engine_load_checkbox")
with col2:
    intake_manifold_pressure_checkbox = st.checkbox("Intake Manifold Pressure", value=False, key="intake_manifold_pressure_checkbox")
    relative_throttle_pos_checkbox = st.checkbox("Relative Throttle Position", value=False, key="relative_throttle_pos_checkbox")
    absolute_throttle_pos_checkbox = st.checkbox("Absolute Throttle Position", value=False, key="absolute_throttle_pos_checkbox")
    o2_sensor1_current_checkbox = st.checkbox("O2 Sensor Current - Pre-Catalytic Converter", value=False, key="o2_sensor1_current_checkbox")
    o2_sensor2_voltage_checkbox = st.checkbox("O2 Sensor Voltage - Post-Catalytic Converter", value=False, key="o2_sensor2_voltage_checkbox")
    catalyst_temperature_sensor1_checkbox = st.checkbox("Catalyst Temperature - Pre-Catalytic Converter", value=False, key="catalyst_temperature_sensor1_checkbox")
    catalyst_temperature_sensor2_checkbox = st.checkbox("Catalyst Temperature - Post-Catalytic Converter", value=False, key="catalyst_temperature_sensor2_checkbox")



st.markdown("---")
st.markdown("# ")

_, submit_col, _ = st.columns(3)
with submit_col:
    submit = st.button("Submit", key="submit_button")

st.markdown("# ")


# Plot data
if submit:
    st.session_state.data = Data(f"data/{data_file}")
    data = st.session_state.data
    timestamps = data.timestamps
    rpm = data.rpm
    speed = data.speed
    timing_advance = data.timing_advance
    coolant_temperature = data.coolant_temperature
    intake_manifold_pressure = data.intake_manifold_pressure
    fuel = Fuel(data.fuel_level, data.fuel_rail_pressure)
    engine_load = EngineLoad(data.absolute_engine_load, data.calculated_engine_load)
    o2_sensor = O2Sensor(data.o2_bank1sensor1_wr_lambda_current, data.o2_bank1sensor2_voltage)
    throttle_position = ThrottlePosition(data.relative_throttle_pos, data.absolute_throttle_pos)
    short_term_trim = ShortTermTrim(data.short_term_o2_trim_bank1, data.short_term_fuel_trim_bank1)
    catalyst_temperature = CatalystTemperature(data.catalyst_temperature_bank1sensor1, data.catalyst_temperature_bank1sensor2)

    # check if more than one checkbox is selected
    if sum([rpm_checkbox, speed_checkbox, timing_advance_checkbox, fuel_rail_pressure_checkbox, short_term_o2_trim_checkbox, short_term_fuel_trim_checkbox, coolant_temperature_checkbox, absolute_engine_load_checkbox, calculated_engine_load_checkbox, intake_manifold_pressure_checkbox, relative_throttle_pos_checkbox, absolute_throttle_pos_checkbox, o2_sensor1_current_checkbox, o2_sensor2_voltage_checkbox, catalyst_temperature_sensor1_checkbox, catalyst_temperature_sensor2_checkbox]) > 1:
        to_plot = []
        titles = []
        if rpm_checkbox:
            to_plot.append(rpm)
            titles.append("RPM")
        if speed_checkbox:
            to_plot.append(speed)
            titles.append("Speed")
        if timing_advance_checkbox:
            to_plot.append(timing_advance)
            titles.append("Timing Advance")
        if fuel_rail_pressure_checkbox:
            to_plot.append(fuel.rail_pressure)
            titles.append("Fuel Rail Pressure")
        if short_term_o2_trim_checkbox:
            to_plot.append(short_term_trim.o2)
            titles.append("Short Term O2 Trim")
        if short_term_fuel_trim_checkbox:
            to_plot.append(short_term_trim.fuel)
            titles.append("Short Term Fuel Trim")
        if coolant_temperature_checkbox:
            to_plot.append(coolant_temperature)
            titles.append("Coolant Temperature")
        if absolute_engine_load_checkbox:
            to_plot.append(engine_load.absolute)
            titles.append("Absolute Engine Load")
        if calculated_engine_load_checkbox:
            to_plot.append(engine_load.calculated)
            titles.append("Calculated Engine Load")
        if intake_manifold_pressure_checkbox:
            to_plot.append(intake_manifold_pressure)
            titles.append("Intake Manifold Pressure")
        if relative_throttle_pos_checkbox:
            to_plot.append(throttle_position.relative)
            titles.append("Relative Throttle Position")
        if absolute_throttle_pos_checkbox:
            to_plot.append(throttle_position.absolute)
            titles.append("Absolute Throttle Position")
        if o2_sensor1_current_checkbox:
            to_plot.append(o2_sensor.pre_cat_current)
            titles.append("O2 Sensor Current - Pre-Catalytic Converter")
        if o2_sensor2_voltage_checkbox:
            to_plot.append(o2_sensor.post_cat_voltage)
            titles.append("O2 Sensor Voltage - Post-Catalytic Converter")
        if catalyst_temperature_sensor1_checkbox:
            to_plot.append(catalyst_temperature.pre_cat)
            titles.append("Catalyst Temperature - Pre-Catalytic Converter")
        if catalyst_temperature_sensor2_checkbox:
            to_plot.append(catalyst_temperature.post_cat)
            titles.append("Catalyst Temperature - Post-Catalytic Converter")
        if use_savgol:
            plot_data_many(timestamps, to_plot, "Time (s)", titles, savgol=True, savgol_window_length=savgol_window_length, savgol_polyorder=savgol_polyorder)
        else:
            plot_data_many(timestamps, to_plot, "Time (s)", titles)
    else:
        # get the one checkbox that is selected
        if rpm_checkbox:
            plot_data(timestamps, rpm, "Time (s)", "RPM", savgol=use_savgol, savgol_window_length=savgol_window_length, savgol_polyorder=savgol_polyorder)
        elif speed_checkbox:
            plot_data(timestamps, speed, "Time (s)", "Speed ($mph$)", savgol=use_savgol, savgol_window_length=savgol_window_length, savgol_polyorder=savgol_polyorder)
        elif timing_advance_checkbox:
            plot_data(timestamps, timing_advance, "Time (s)", "Timing Advance ($deg$)", savgol=use_savgol, savgol_window_length=savgol_window_length, savgol_polyorder=savgol_polyorder)
        elif fuel_rail_pressure_checkbox:
            plot_data(timestamps, fuel.rail_pressure, "Time (s)", "Fuel Rail Pressure ($psi$)", savgol=use_savgol, savgol_window_length=savgol_window_length, savgol_polyorder=savgol_polyorder)
        elif short_term_o2_trim_checkbox:
            plot_data(timestamps, short_term_trim.o2, "Time (s)", "O2 Trim ($%$)", savgol=use_savgol, savgol_window_length=savgol_window_length, savgol_polyorder=savgol_polyorder)
        elif short_term_fuel_trim_checkbox:
            plot_data(timestamps, short_term_trim.fuel, "Time (s)", "Fuel Trim ($%$)", savgol=use_savgol, savgol_window_length=savgol_window_length, savgol_polyorder=savgol_polyorder)
        elif coolant_temperature_checkbox:
            plot_data(timestamps, coolant_temperature, "Time (s)", "Coolant Temperature ($F$)", savgol=use_savgol, savgol_window_length=savgol_window_length, savgol_polyorder=savgol_polyorder)
        elif absolute_engine_load_checkbox:
            plot_data(timestamps, engine_load.absolute, "Time (s)", "Absolute Engine Load ($%$)", savgol=use_savgol, savgol_window_length=savgol_window_length, savgol_polyorder=savgol_polyorder)
        elif calculated_engine_load_checkbox:
            plot_data(timestamps, engine_load.calculated, "Time (s)", "Calculated Engine Load ($%$)", savgol=use_savgol, savgol_window_length=savgol_window_length, savgol_polyorder=savgol_polyorder)
        elif fuel_level_checkbox:
            plot_data(timestamps, fuel.level, "Time (s)", "Fuel Level ($%$)", savgol=use_savgol, savgol_window_length=savgol_window_length, savgol_polyorder=savgol_polyorder)
        elif intake_manifold_pressure_checkbox:
            plot_data(timestamps, intake_manifold_pressure, "Time (s)", "Intake Manifold Pressure ($psi$)", savgol=use_savgol, savgol_window_length=savgol_window_length, savgol_polyorder=savgol_polyorder)
        elif relative_throttle_pos_checkbox:
            plot_data(timestamps, throttle_position.relative, "Time (s)", "Relative Throttle Position ($%$)", savgol=use_savgol, savgol_window_length=savgol_window_length, savgol_polyorder=savgol_polyorder)
        elif absolute_throttle_pos_checkbox:
            plot_data(timestamps, throttle_position.absolute, "Time (s)", "Absolute Throttle Position ($%$)", savgol=use_savgol, savgol_window_length=savgol_window_length, savgol_polyorder=savgol_polyorder)
        elif o2_sensor1_current_checkbox:
            plot_data(timestamps, o2_sensor.pre_cat_current, "Time (s)", "Pre-Cat O2 Sensor Current ($mA$)", savgol=use_savgol, savgol_window_length=savgol_window_length, savgol_polyorder=savgol_polyorder)
        elif o2_sensor2_voltage_checkbox:
            plot_data(timestamps, o2_sensor.post_cat_voltage, "Time (s)", "Post-Cat O2 Sensor Voltage ($V$)", savgol=use_savgol, savgol_window_length=savgol_window_length, savgol_polyorder=savgol_polyorder)
        elif catalyst_temperature_sensor1_checkbox:
            plot_data(timestamps, catalyst_temperature.pre_cat, "Time (s)", "Pre-Cat Catalyst Temperature ($F$)", savgol=use_savgol, savgol_window_length=savgol_window_length, savgol_polyorder=savgol_polyorder)
        elif catalyst_temperature_sensor2_checkbox:
            plot_data(timestamps, catalyst_temperature.post_cat, "Time (s)", "Post-Cat Catalyst Temperature ($F$)", savgol=use_savgol, savgol_window_length=savgol_window_length, savgol_polyorder=savgol_polyorder)
