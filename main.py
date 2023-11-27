# importing the needed packages to use the implemented functions in the scipt
from pathlib import Path
import ifcopenshell
import ifcopenshell.api
import bpy

# naming the skylab-file that we using
modelname = "LLYN - STRU"

try:
    dir_path = Path(__file__).parent
    model_url = Path.joinpath(dir_path, 'model', modelname).with_suffix('.ifc')
    model = ifcopenshell.open(model_url)
except OSError:
    try:
        import bpy
        model_url = Path.joinpath(Path(bpy.context.space_data.text.filepath).parent, 'model', modelname).with_suffix('.ifc')
        model = ifcopenshell.open(model_url)
    except OSError:
        print(f"ERROR: please check your model folder : {model_url} does not exist")

# Your script goes here

####################################   Assignment 2   ########################################
###########################   CALCULATION OF TOTAL BEAM LENGTH   #############################

# extracting all elements types categorized as beams from the IFC
beams = model.by_type("IfcBeam")

# making a empty parameter
total_beam_length = 0

# creating a loop to assemble the lenghts of the beams in the IFC-file as an iteratve process
for entity in model.by_type("IfcBeam"):
    # accessing the desired attributes
   for relDefinesByProperties in entity.IsDefinedBy:
        for prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
            # then get the attribute we are looking for
            if prop.Name == 'Span':
                # adding the length to the total length
                total_beam_length += prop.NominalValue.wrappedValue

# calculating the total length of the beams in the IFC-file by using the collected data from the loop
total_beam_length = round(total_beam_length/1000,2)

# making an output as a text line of the total lenghts of beams in the IFC-file
print(f"\nThere are {total_beam_length} meters of beam in the model")

# defining a specfic price for the beams
beam_price = 950 #estimated price in kr/m

# calculating the cost of the total beams in the IFC-file
total_beam_price = f"{total_beam_length*beam_price:,}"

# this code is to check if everything works by extracting information of the beams 
#beams = model.by_type("IfcBeam")
#for beam in beams:
#    print(beam.Name)

###################################   Assignment 3   ############################################
###########################   ADDING A NEW PROPERTY OF COST   #############################

# creating a loop to add a property for a specific element in the IFC-file in an iteratve process
for beam_type in model.by_type("IfcBeamType"):
    # using a function that execute the desires of making a new property
    # "pset.add_psey": adding a property set (pset) to the model
    # "model": referring to the IFC-file being operated on
    # "product=beam_type": specifing the object to which the property set will be added
    # "name="Price_property": name of the property set being added
    pset = ifcopenshell.api.run("pset.add_psey", model, product=beam_type, name="Price_property")
    # checking if the profile "SHS" is contained within the name attribute of the beam type
    # if it's present, the code within this if statement will be executed
    if "SHS" in beam_type.Name:
        # if the above condition is true, a function in IfcOpenShell to edit a property set
        # "model": referring to the IFC model
        # "pset": specifing the property set being edited
        # "properties": setting the name of the property to 'Price' and its correponding value of '880'     
        ifcopenshell.api.run("pset.edit_pset", model, pset=pset, properties={"Price": "800"})
    elif "Rectangular" in beam_type.Name:
        ifcopenshell.api.run("pset.edit_pset", model, pset=pset, properties={"Price": "800"})
    elif "Square" in beam_type.Name:
        ifcopenshell.api.run("pset.edit_pset", model, pset=pset, properties={"Price": "800"})
    elif "I-profil" in beam_type.Name:
        ifcopenshell.api.run("pset.edit_pset", model, pset=pset, properties={"Price": "900"})
    elif "IPE" in beam_type.Name:
        ifcopenshell.api.run("pset.edit_pset", model, pset=pset, properties={"Price": "900"})
    elif "H-Wide" in beam_type.Name:
        ifcopenshell.api.run("pset.edit_pset", model, pset=pset, properties={"Price": "1000"})
    elif "HEB-profil" in beam_type.Name:
        ifcopenshell.api.run("pset.edit_pset", model, pset=pset, properties={"Price": "1000"})
    else:
        ifcopenshell.api.run("pset.edit_pset", model, pset=pset, properties={"Price": "1000"})

# Saving properties of the price to a new IFC file called 'test.ifc'
model.write(r'C:\Users\45272\OneDrive - Danmarks Tekniske Universitet\Dokumenter\DTU\Master\7. Semester\41934 Advanced Building Information Modeling (BIM)\Assignment 3\output')
#model.write(r'C:\Users\Mathias Braarup\OneDrive\Dokumenter\DTU\7. Semester\41934 Videregående BIM\Assignments\Assignment 3\test.ifc')
