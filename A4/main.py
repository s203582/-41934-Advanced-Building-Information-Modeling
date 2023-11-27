from pathlib import Path
import ifcopenshell
import ifcopenshell.api
import bpy

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
####################################
# Calculation of total beam length

beams = model.by_type("IfcBeam")

total_beam_length = 0

for entity in model.by_type("IfcBeam"):
    #we need to get the attributes
   for relDefinesByProperties in entity.IsDefinedBy:
        for prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
            #and then get the attribute we are looking for
            if prop.Name == 'Span':
                #add the length to the total length
                total_beam_length += prop.NominalValue.wrappedValue

total_beam_length = round(total_beam_length/1000,2)

print(f"\nThere are {total_beam_length} meters of beam in the model")

beam_price = 950 #estimated price in kr/m

total_beam_price = f"{total_beam_length*beam_price:,}"

#print(f"\nThe total price for the beams in the project is: {total_beam_price} kr.")

# Test if everything works:
#beams = model.by_type("IfcBeam")
#for beam in beams:
#    print(beam.Name)

##########################################################################################
# Assignment 3

for beam_type in model.by_type("IfcBeamType"):
    pset = ifcopenshell.api.run("pset.add_pset", model, product=beam_type, name="Price_property")
    if "SHS" in beam_type.Name:
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

# Save properties to new IFC file called "test.ifc":
model.write(r'C:\Users\Mathias Braarup\OneDrive\Dokumenter\DTU\7. Semester\41934 Videregående BIM\Assignments\Assignment 3\test.ifc')
