import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open("RF.pkl", "rb"))

st.title("Mushroom Classification")
cap_shapes = ['bell', 'conical', 'flat', 'knobbed', 'sunken', 'convex']
cap_surfaces = ['fibrous', 'grooves', 'smooth', 'scaly']
cap_colors =  ['buff', 'cinnamon', 'red', 'gray', 'brown', 'pink', 'green', 'purple', 'white', 'yellow']
bruises = ['no', 'bruises']
odors = ['almond', 'creosote', 'foul', 'anise', 'musty', 'none', 'pungent', 'spicy', 'fishy']
gill_attachments = ['attached', 'free']
gill_spacings = ['close', 'crowded']
gill_sizes = ['broad', 'narrow']
gill_colors =  ['black', 'red', 'gray', 'chocolate', 'black', 'brown', 'orange', 'pink', 'green', 'purple', 'white', 'yellow']
stalk_shapes = ['enlarging', 'tapering']
stalk_roots =  ['missing', 'bulbous', 'clup', 'equal', 'rooted']
stalk_surface_above_rings = ['fibrous', 'silky', 'smooth', 'scaly']
stalk_surface_below_rings = ['fibrous', 'silky', 'smooth', 'scaly']
stalk_color_above_rings = ['buff', 'cinnamon', 'red', 'gray', 'brown', 'orange', 'pink', 'white', 'yellow']
stalk_color_below_rings = ['buff', 'cinnamon', 'red', 'gray', 'brown', 'orange', 'pink', 'white', 'yellow']
veil_types =  ['partial']
veil_colors = ['brown', 'orange', 'white', 'yellow']
ring_numbers = ['none', 'one', 'two']
ring_types =  ['evanescent', 'flaring', 'large', 'none', 'pendant']
spore_print_colors = ['buff', 'chocolate', 'black', 'brown', 'orange', 'green', 'purple', 'white', 'yellow']
populations =  ['abundant', 'clustered', 'numerous', 'scattered', 'several', 'solitary']
habitats = ['woods', 'grasses', 'leaves', 'meadows', 'paths', 'urban', 'waste']

cap_shape = st.selectbox("Cap Shape", cap_shapes)
cap_surface = st.selectbox("Cap Surface", cap_surfaces)
cap_color = st.selectbox("Cap Color", cap_colors)
bruise = st.selectbox("Bruise", bruises)
odor = st.selectbox("Odor", odors)
gill_attachment = st.selectbox("Gill Attachment", gill_attachments)
gill_spacing = st.selectbox("Gill Spacing", gill_spacings)
gill_size = st.selectbox("Gill Size", gill_sizes)
gill_color = st.selectbox("Gill Color", gill_colors)
stalk_shape = st.selectbox("Stalk Shape", stalk_shapes)
stalk_root = st.selectbox("Stalk Root", stalk_roots)
stalk_surface_above_ring = st.selectbox("Stalk Surface Above Ring", stalk_surface_above_rings)
stalk_surface_below_ring = st.selectbox("Stalk Surface Below Ring", stalk_surface_below_rings)
stalk_color_above_ring = st.selectbox("Stalk Color Above Ring", stalk_color_above_rings)
stalk_color_below_ring = st.selectbox("Stalk Color Below Ring", stalk_color_below_rings)
veil_type = st.selectbox("Veil Type", veil_types)
veil_color = st.selectbox("Veil Color", veil_colors)
ring_number = st.selectbox("Ring Number", ring_numbers)
ring_type = st.selectbox("Ring Type", ring_types)
spore_print_color = st.selectbox("Spore Print Color", spore_print_colors)
population = st.selectbox("Population", populations)
habitat = st.selectbox("Habitat", habitats)

if st.button("Predict"):
	cap_shape = cap_shapes.index(cap_shape)
	cap_surface = cap_surfaces.index(cap_surface)
	cap_color = cap_colors.index(cap_color)
	bruise = bruises.index(bruise)
	odor = odors.index(odor)
	gill_attachment = gill_attachments.index(gill_attachment)
	gill_spacing = gill_spacings.index(gill_spacing)
	gill_size = gill_sizes.index(gill_size)
	gill_color = gill_colors.index(gill_color)
	stalk_shape = stalk_shapes.index(stalk_shape)
	stalk_root = stalk_roots.index(stalk_root)
	stalk_surface_above_ring = stalk_surface_above_rings.index(stalk_surface_above_ring)
	stalk_surface_below_ring = stalk_surface_below_rings.index(stalk_surface_below_ring)
	stalk_color_above_ring = stalk_color_above_rings.index(stalk_color_above_ring)
	stalk_color_below_ring = stalk_color_below_rings.index(stalk_color_below_ring)
	veil_type = veil_types.index(veil_type)
	veil_color = veil_colors.index(veil_color)
	ring_number = ring_numbers.index(ring_number)
	ring_type = ring_types.index(ring_type)
	spore_print_color = spore_print_colors.index(spore_print_color)
	population = populations.index(population)
	habitat = habitats.index(habitat)

	test = np.array([[cap_shape, cap_surface, cap_color, bruise, odor, gill_attachment, gill_spacing, gill_size, gill_color, stalk_shape, stalk_root, stalk_surface_above_ring, stalk_surface_below_ring, stalk_color_above_ring, stalk_color_below_ring, veil_type, veil_color, ring_number, ring_type, spore_print_color, population, habitat]])
	res = model.predict(test).item()
	print(res)
	if res == 1:
		st.success("Prediction: Edible")
	else:
		st.success("Prediction: Poisonous")
