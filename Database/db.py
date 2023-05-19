"""
# Database\db.py


"""

import firebase_admin
from firebase_admin import db

# credentials = firebase_admin.credentials.Certificate("Database/service_account_key.json")
# firebase_admin.initialize_app(credentials, {'databaseURL': "https://pi-obd-default-rtdb.firebaseio.com/"})





class Database:
    def __init__(self):
        self._url = "https://pi-obd-default-rtdb.firebaseio.com/"
        self._credentials = firebase_admin.credentials.Certificate("Database/service_account_key.json")
        self._firebase_admin = firebase_admin.initialize_app(self._credentials, {'databaseURL': self._url})
        self._ref = db.reference("/")
        # self._ref_root = db.reference("/")
        self._structure = {
            'accelerator': {
                'position_d': 0,
                'position_e': 0,
            },
            'ambient_air': {
                'pressure': 0,
                'temperature': 0,
            },
            'catalyst_temperature': {
                'bank1': {
                    'sensor1': 0,
                    'sensor2': 0,
                },
            },
            'commanded_equivalence_ratio': 0,
            'commanded_evaporative_purge': 0,
            'control_module_voltage': 0,
            'coolant_temperature': 0,
            'dtc': {
                'count': 0,
                'distance_since_clear': 0,
                'latest_code': "",
                'latest_code_description': "",
                'time_since_clear': 0,
                'warmups_since_clear': 0,
            },
            'engine_load': {
                'absolute': 0,
                'calculated': 0,
            },
            'engine_rpm': 0,
            'engine_run_time': 0,
            'evap_vapor_pressure': 0,
            'fuel_level': 0,
            'fuel_rail_pressure': 0,
            'fuel_status': "",
            'fuel_trim': {
                'long_term': {
                    'bank1': 0,
                },
                'short_term': {
                    'bank1': 0,
                },
            },
            'intake_manifold': {
                'pressure': 0,
                'temperature': 0,
            },
            'monitor_results': {
                'catalyst': {
                    'bank1': "",
                },
                'evap': {
                    '_020': "",
                    '_040': "",
                    '_090': "",
                    '_150': "",
                    'purge_flow': "",
                },
                'misfire': {
                    'cylinder1': "",
                    'cylinder2': "",
                    'cylinder3': "",
                    'cylinder4': "",
                    'general': "",
                },
                'o2_sensor': {
                    'bank1': {
                        'sensor1': "",
                        'sensor2': "",
                    },
                },
                'o2_sensor_heater': {
                    'bank1': {
                        'sensor1': "",
                        'sensor2': "",
                    },
                },
                'vvt': {
                    'bank1': "",
                },
            },
            'o2_sensor': {
                'bank1': {
                    'sensor1_wr_lambda': 0,
                    'sensor2': 0,
                },
            },
            'o2_trim': {
                'long_term': {
                    'bank1': 0,
                },
                'short_term': {
                    'bank1': 0,
                },
            },
            'throttle_position': {
                'absolute': 0,
                'absolute_b': 0,
                'commanded': 0,
                'relative': 0,
            },
            'timing_advance': 0,
            'vehicle_speed': 0,
        }
        self._ref.update(self._structure)  # initialize the database with the structure




    def update_node(self, node: str, data: dict):
        """
        Update a node in the database with the given data.

        ## Parameters
        - `node` : str
            - The node to update.
        - `data` : dict
            - The data to update the node with.
        """
        self._ref.child(node).update(data)

    def update_all(self, data: dict):
        """
        Update the entire database with the given data.

        ## Parameters
        - `data` : dict
            - The data to update the database with.
        """
        self._ref.update(data)

    def get_node(self, node: str):
        """
        Get the data from a node in the database.

        ## Parameters
        - `node` : str
            - The node to get the data from.

        ## Returns
        - `data` : dict
            - The data from the given node.
        """
        return self._ref.child(node).get()
    
    def get_all(self):
        """
        Get the data from the entire database.

        ## Returns
        - `data` : dict
            - The data from the entire database.
        """
        return self._ref.get()





database = Database()

# database.update_node('accelerator', {'position_d': 1.2, 'position_e': 42})
# database.update_node('ambient_air', {'pressure': 1.2, 'temperature': 42})


# ref = db.reference("/")

# # update the "temperature" key in the "ambient_air" node
# ref.update({
#     'ambient_air': {
#         'pressure': 1.2,
#         'temperature': 42
#     }
# })















# import socketio



# sio = socketio.Client()
# sio.connect('http://localhost:5000')


# sensor_data = {
#     'timestamp': 0,
#     'speed': 0,
#     'engine_RPM': 0,
# }


# sio.emit('sensor_data', sensor_data)





