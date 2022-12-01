# Preparing animations in Rhino/GH

Example files camera_anim_presentation.3dm and camera_anim_presentation.gh
show how you can create certain camera animations and start them by pressing certain key "a", "s", "d", ...

Simply try it out!

## For your own presentation:

1. Open your 3dm file
2. Define some good views through "NamedViews".
3. Open  camera_anim_presentation.gh
4. Update the names of the views
5. Select the type of animation:
    * Make a tween between 2 views
    * Walk along a path
    * Turn around your head


## Requirements:
You need to install INTERACTOOL plugin for grasshopper which you can find here:
https://www.food4rhino.com/app/interactool#downloads_list

Simply download the Zip file and move the files into the Components folder of gh.
(Grasshopper window: File > Special Folders > Components folder)
Make sure the component is not blocked. To double check this, right click on the .gha file 
properties and unblock the component.
