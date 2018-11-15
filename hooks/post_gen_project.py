import arcpy
import os.path
import shutil

# create locations 
existing_project_path = os.path.abspath(r'./arcgis/cookiecutter.aprx')
new_project_path = os.path.abspath(r'./arcgis/{{ cookiecutter.project_name }}.aprx')
    
# copy the existing template project
old_aprx = arcpy.mp.ArcGISProject(existing_project_path)
old_aprx.saveACopy(new_project_path)

# now create a reference to the new project
new_aprx = arcpy.mp.ArcGISProject(new_project_path)

# set the default geodatabase to be an interim file geodatabase
interim_gdb = os.path.join(
    os.getcwd(),
    'data',
    'interim',
    'interim.gdb'
)
if not arcpy.Exists(interim_gdb):
    arcpy.management.CreateFileGDB(os.path.dirname(interim_gdb), os.path.basename(interim_gdb))

new_aprx.defaultGeodatabase = interim_gdb

# create a matched name toolbox, and set the new project to reference it
new_name = os.path.basename(new_project_path).split('.')[0]

new_toolbox_path = os.path.abspath(os.path.join(
    os.path.dirname(new_project_path),
    new_name + '.tbx'
))

shutil.copyfile(old_aprx.defaultToolbox, new_toolbox_path)

new_aprx.defaultToolbox = new_toolbox_path

# save new settings for aprx
new_aprx.save()

# now delete the old toolbox and project
arcpy.management.Delete(old_aprx.defaultToolbox)
arcpy.management.Delete(existing_project_path)