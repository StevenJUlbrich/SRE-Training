# JSON Structure Documentation

Root Object
panels (Array): A list of panel objects, each representing a scene in the manuscript.
Panel Object (Elements of panels Array)
Each panel object contains the following key-value pairs:

panel (Integer):

Description: The panel number in sequential order.
Data Type: Integer.
filename (String):

Description: The filename of the image associated with the panel.
Data Type: String.
scene_description (String):

Description: A detailed description of the scene depicted in the panel, including visual elements, colors, and artistic style.
Data Type: String.
characters_in_frame (Array of Strings):

Description: A list of character names present in the panel.
Data Type: Array of strings.
speech_bubbles (Object):

Description: Contains dialogue for characters in the panel.
Data Type: Object.
Structure:
Key: Character name (String).
Value: Dialogue text (String).
narration (String):

Description: Narration text that provides context or commentary for the panel.
Data Type: String.
Example Panel Object
Summary of Data Types

Key            Data Type           Description
panels         Array               Contains all panel objects.
panel          Integer             Panel number.
filename       String              Image filename for the panel.
scene_description String           Description of the scene.
characters_in_frame Array of Strings List of characters in the panel.
speech_bubbles Object              Character dialogues in the panel.
narration      String              Narration text for the panel.

This structure ensures that each panel is well-documented with visual, narrative, and character details.