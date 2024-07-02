Smart Travel Assistant Guide
=====

* Done the project for a course final project.
* Build the framework, **STAG**, using generative AI models.
* Wahid Alam (mohammadwahidul-alam@uiowa.edu) is one of the contributors.

## Goal
The goal is to develop a Smart Travel Assisting Guide using generative AI to provide personalized recommendations and culturally sensitive insights, enhancing the travel experience by catering to individual preferences and promoting respectful engagement with diverse cultures. 


## Modules
The Smart Travel Assisting Guide (STAG) comprises four distinct submodules.
* Culture and Language Module: This module serves as a comprehensive resource, furnishing users with valuable insights into the local culture, traditions, and etiquette of the chosen destination.
* Virtual City Exploration Module: This submodule utilizes the Google Maps API to obtain destination coordinates and relevant attraction data, then employs the OpenAI API to generate an image prompt for the DALL-E-3 model, producing an image URL that is integrated into an HTML file for seamless accessibility by the rendering script.
* Historical Overview Module: This platform provides users with rich historical overviews, incorporating significant events and visual representations associated with the chosen destination.
* Personalized Itinerary Generator: Users input their preferences, such as interests, dietary restrictions, budget, and trip duration, and the Smart Travel Assisting Guide (STAG) generates personalized itineraries. By considering factors like current location, destination, and preferred transportation, STAG ensures the travel plan is closely aligned with the user's unique needs for an optimized travel experience.

## How to Execute
Checkout `app.py` script to run our framework. 
Keep in mind that users need to put the API keys in the placeholders. Users can find the placeholders by searching the scripts with *placeholder_api_key*.
Users will be prompted with inputs when they execute `python3 app.py`.


## License

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

[![CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

