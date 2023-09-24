import sys
print(sys.path)
import ifcopenshell
print(ifcopenshell.version)
 
import ifcopenshell
model = ifcopenshell.open('/Users/sabindahal/Downloads/OpenDataIFC-20230913/AC20-FZK-Haus-40.ifc')

print(model.schema)

print(model.by_id(1))
walls = model.by_type('IfcWall')
print(len(walls))
wall = model.by_type('IfcWall')[0]
print(wall.is_a())
print(model.by_guid('0lY6P5Ur90TAQnnnI6wtnb'))
print(wall.is_a('IfcWall')) # Returns True
print(wall.is_a('IfcElement')) # Returns True
print(wall.is_a('IfcWindow')) # Returns False
print(wall.id())
print(wall[0]) # The first attribute is the GlobalId
print(wall[2]) # The third attribute is the Name
print(wall.GlobalId)
print(wall.Name)
print(wall.get_info())
import ifcopenshell.util
import ifcopenshell.util.element
print(ifcopenshell.util.element.get_psets(wall))
print(wall.IsDefinedBy)
print(model.get_inverse(wall))

import ifcopenshell
from ifctester import ids, reporter


# create new IDS
my_ids = ids.Ids(title="My IDS")

# add specification to it
my_spec = ids.Specification(name="My first specification")
my_spec.applicability.append(ids.Entity(name="IFCWALLSTANDARDCASE"))
property = ids.Property(
    name="IsExternal", 
    value="TRUE", 
    propertySet="Pset_WallCommon", 
    datatype="IfcBoolean",
    uri="https://identifier.buildingsmart.org/uri/.../prop/LoadBearing", 
    instructions="Walls need to be load bearing.",
    minOccurs=1,
    maxOccurs="unbounded")
my_spec.requirements.append(property)
my_ids.specifications.append(my_spec)

# Save such IDS to file
result = my_ids.to_xml("/Users/sabindahal/Downloads/IFCtester/abc.xml")

# open  IFC file:
my_ifc = ifcopenshell.open("/Users/sabindahal/Downloads/IFCtester/AC20-FZK-Haus-40.ifc")

# validate IFC model against IDS requirements:
my_ids.validate(my_ifc)

# show results:
reporter.Console(my_ids).report()
