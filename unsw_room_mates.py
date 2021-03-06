#!/usr/bin/python3
from flask import Flask, g, session, request, jsonify, render_template
from backend.unsw_room_mates_backend import *

app = Flask(__name__)

# API CALLS

# Get a list of all buildings by name
@app.route("/buildings/name", methods = ["GET"])
def get_all_building_names_route():
    return jsonify(get_all_building_names())


# Get a list of all buildings by ID
@app.route("/buildings/id", methods = ["GET"])
def get_all_building_ids_route():
    return jsonify(get_all_building_ids())


# Get a buildings mapping (list of tuples/list)
@app.route("/buildings/mapping", methods = ["GET"])
def get_all_building_mappings_route():
    return jsonify(get_all_building_mappings_parsed())

# Get a list of buildings and the rooms free at a given time
@app.route("/buildings/free", methods = ["POST"])
def get_buildings_free_route():

    # Get the post data
    data = request.form

    # Get the time data
    time_int, day, week = convert_from_epoch(data["epoch_time"])

    # Get buildings sorted by number of free rooms
    free_buildings = get_buildings_free(time_int, day, week)

    return jsonify(free_buildings)


# Get a list of all room names in a given building
@app.route("/rooms/<buildingID>/name", methods = ["GET"])
def get_all_room_names_route(buildingID):
    return jsonify(get_all_room_names(buildingID))


# Get a list of all room IDs in a given building
@app.route("/rooms/<buildingID>/id", methods = ["GET"])
def get_all_room_ids_route(buildingID):
    return jsonify(get_all_room_ids(buildingID))


# Get a room mapping in a given building
@app.route("/rooms/<buildingID>/mapping", methods = ["GET"])
def get_all_room_ids_mapping(buildingID):
    return jsonify(get_all_room_mapping(buildingID))



# Get a room's free time from a given building and given time
@app.route("/rooms", methods = ["POST"])
def get_room_route():

    # Get the post data
    data = request.form
    
    buildingID = data["buildingID"]
    roomID     = data["roomID"]

    # Get the time data
    _, day, week = convert_from_epoch(data["epoch_time"])

    # Return the free_time array
    return jsonify(get_room_from_day_week(buildingID, roomID, day, week))

if __name__ == "__main__":
    app.run()