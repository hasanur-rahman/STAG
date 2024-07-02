from flask import Flask, render_template, request
from runSTAG import VirtualCityExplorationModule, CultureAndLanguageModule, HistoricalOverviewModule, PersonalizedItineraryGenerator, UtilityModule

from elevenlabs import set_api_key
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    destination = request.form['destination']
    current_location = request.form['current_location']
    interests = request.form.getlist('interests')
    dietary_restrictions = request.form['dietary_restrictions']
    budget = float(request.form['budget'])
    number_of_days = int(request.form['number_of_days'])
    transportation_mode = request.form['transportation_mode']

    preferences = {
        "interests": interests,
        "dietary_restrictions": dietary_restrictions,
        "budget": budget,
        "number_of_days": number_of_days
    }

    openai_key = 'placeholder_api_key'
    gmaps_key = 'placeholder_api_key'
    set_api_key("placeholder_api_key")
    
    utility_module = UtilityModule()

    print("\n\nVirtual City Exploration.")
    city_exploration_module = VirtualCityExplorationModule(destination, openai_key, gmaps_key, NumberofAttractions=1)
    city_exploration_module.generateAttractionsImage()


    
    # culture_language_module = CultureAndLanguageModule(destination)
    # cultural_insights = culture_language_module.get_cultural_insights()
    # print("\n\n### Cultural Insights ###")
    # print(cultural_insights)
    # common_phrases = culture_language_module.get_common_phrases()
    # print("\n\n### Common Phrases ###")
    # print(common_phrases)
    # culture_language_module.get_audio_pronunciations(common_phrases)
    # print("\n\nVirtual City Exploration.")
    # city_exploration_module = VirtualCityExplorationModule(destination, gmaps_key)
    # city_exploration_module.generateAttractionsImage()
    
    culture_language_module = CultureAndLanguageModule(destination)
    cultural_insights = culture_language_module.get_cultural_insights()
    # print("\n\n### Cultural Insights ###")
    # print(cultural_insights)
    common_phrases = culture_language_module.get_common_phrases()
    # print("\n\n### Common Phrases ###")
    # print(common_phrases)
    audio_data_phrases = culture_language_module.get_audio_pronunciations(common_phrases)
    audio_phrases_base64 = base64.b64encode(audio_data_phrases).decode('utf-8')

    historical_overview_module = HistoricalOverviewModule(destination)
    historical_overview_result,historical_overview_result_list = historical_overview_module.generate_historical_overview()
    # print("\n\n### Historical Overview ###")
    # print(historical_overview_result)
    image_prompts_list = historical_overview_module.generate_imagepromt_urllist_basedon_historical_overview(historical_overview_result_list)
    # print("\n\n### Image Prompts List ###")
    image_urls = []
    image_number = 1
    for historical_overview, image_prompt in image_prompts_list:
        print(image_prompt)
        image_url = historical_overview_module.generate_image_from_image_prompt(image_prompt)
        # print("image url: ", image_url)
        image_urls.append(image_url)
    #     utility_module.save_image_from_url(image_url, str(image_number), destination.replace(' ', '-'), "HistoricalOverviewImages")
        image_number = image_number + 1
        


        

    # # print("\n\nShowing Images")
    # # for url in image_urls:
    # #     open_image_from_url(url)

    itinerary_generator = PersonalizedItineraryGenerator(preferences, current_location, destination, transportation_mode)
    personalized_itinerary = itinerary_generator.generate_personalized_itinerary()
    print("\n### Personalized Itinerary ###")
    print(personalized_itinerary)

    # # return render_template('result.html', historical_overview_result=historical_overview_result,historical_overview_result_list=historical_overview_result_list, image_urls=image_urls,cultural_insights=cultural_insights, common_phrases=common_phrases, personalized_itinerary=personalized_itinerary)
    # return render_template('result.html', TopAttractionImageUrl=city_exploration_module.topLocationsImageUrl, CityName=city_exploration_module.city_name ,CityLoc= city_exploration_module.getCityCordinates(), TopAttractionCord = city_exploration_module.getTopAttractions())
    # return render_template('result.html', personalized_itinerary=personalized_itinerary)
    # return render_template('result.html', audio_pronunciation_common_phrases=audio_pronunciation_common_phrases)
    return render_template('result.html', cultural_insights=cultural_insights, common_phrases=common_phrases, audio_phrases_base64=audio_phrases_base64, personalized_itinerary=personalized_itinerary, historical_overview_result_list=historical_overview_result_list, image_urls=image_urls, TopAttractionImageUrl=city_exploration_module.topLocationsImageUrl, CityName=city_exploration_module.city_name ,CityLoc= city_exploration_module.getCityCordinates(), TopAttractionCord = city_exploration_module.getTopAttractions())

if __name__ == '__main__':
    app.run(debug=True)
