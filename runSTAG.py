# import openai
from elevenlabs import generate, play
from elevenlabs import set_api_key
import gmaps
import requests
import os
import re
import PIL.Image
from io import BytesIO
from openai import OpenAI


# import geopy
# import folium
# from selenium import webdriver
# import time
# from bs4 import BeautifulSoup


# openai.api_key = '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'
# tts_api_key = ''


# client = OpenAI()

class CultureAndLanguageModule:
    def __init__(self, destination):
        chatgpt_api_key = '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'
        # chatgpt_text_messages = chatgpt_msg
        self.client = OpenAI(api_key = chatgpt_api_key)
        self.destination = destination
        pass

    def get_cultural_insights(self):
        systemContent = 'You are a module to provide who works on exploring the most significant cultural insights based on a given input city. In your answer, insert an empty line between your cultural insights. For each cultural insight, please keep your answer at least 3 sentences and at most 10 sentences long. '
        userPrompt = f"Please provide at most 10 cultural insights about {self.destination}."
        # messages = [{'role': 'system', 'content': systemContent}, {'role': 'user', 'content': userPrompt}]
        chatgpt_text_messages = [ {"role": "system", "content": systemContent}, {'role': 'user', 'content': userPrompt} ]
        
        # # Append user's input to the message list
        # chatgpt_text_messages.append(
        #     {
        #         "role" : "user",
        #         "content" : prompt
        #     }
        # )

        # Make an API call to get a response
        # response = openai.ChatCompletion.create(
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chatgpt_text_messages,
            temperature=1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        message = response.choices[0].message
        # chatgpt_text_messages.append(message)
        response = message.content

        return response 

    def get_common_phrases(self):
        systemContent = "You are a module to provide who works on exploring the most commonly used phrases and expressions based on a given input city. Please maintain the following format: First give a phrase starting with keyword 'Phrase/Expression:', then describe what it means in English starting with keyword 'English Meaning:'. Please keep your answer as short as possible."
        userPrompt = f"Please provide only 5 common phrases and expressions used in {self.destination}."
        # messages = [{'role': 'system', 'content': systemContent}, {'role': 'user', 'content': userPrompt}]
        chatgpt_text_messages = [ {"role": "system", "content": systemContent}, {'role': 'user', 'content': userPrompt} ]

        # prompt = f"Please provide only 5 Common phrases and expressions in {destination}. "
        # response = self.call_openai_api(prompt)
        # Append user's input to the message list
        # chatgpt_text_messages.append(
        #     {
        #         "role" : "user",
        #         "content" : prompt
        #     }
        # )

        # Make an API call to get a response
        # response = openai.ChatCompletion.create(
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chatgpt_text_messages,
            temperature=1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        message = response.choices[0].message
        # chatgpt_text_messages.append(message)
        response = message.content
        return response

    def get_audio_pronunciations(self, phrases):

        systemContent = "You are a module to convert a given list of phrases to the correct format as given. Give your answer as text that contains a list of cultural phrases followed by english meaning from the input. To be precise, the list should be comma separated such as the following format: A B, C D; where A is the phrase and B is the english meaning and so on. No other descriptions are needed."
        userPrompt = f"Convert the following to the system required format: {phrases}"
        # prompt = f"Give your answer as text that contains a list of cultural phrases followed by english meaning from the following: {phrases}. To be precise, the list should be comma separated such as the following format: A B, C D; where A is the phrase and B is the english meaning and so on. No other descriptions are needed."
        chatgpt_text_messages = [ {"role": "system", "content": systemContent}, {'role': 'user', 'content': userPrompt} ]

        # chatgpt_text_messages.append(
        #     {
        #         "role" : "user",
        #         "content" : prompt
        #     }
        # )

        # Make an API call to get a response
        # response = openai.ChatCompletion.create(
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chatgpt_text_messages,
            temperature=1,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # message = response['choices'][0]['message']
        message = response.choices[0].message
        chatgpt_text_messages.append(message)
        # response = message['content']
        response = message.content

        print("Audio pronunciation: ", response)

        audio = generate(
          text=response,
          voice="Bella",
          model="eleven_multilingual_v2"
        )
        # play(audio)
        # print(audio)
        return audio
        



class VirtualCityExplorationModule:
    def __init__(self, cityName, openai_key, gmaps_key, NumberofAttractions=5) -> None:
        self.openai_key = openai_key
        self.gmaps_key = gmaps_key
        self.client = OpenAI(api_key = openai_key)
        # self.client = OpenAI()
        gmaps.configure(api_key= gmaps_key)
        self.city_name= cityName
        self.numAttractions = NumberofAttractions

    def generateImagePrompt(self, attractionName):
        systemContent = 'You write image generation prompts for DALL-E 3 from the given input request. For example, if you were asked to write a prompt for an image about garden of God in Victor, Colorado, USA, you may output: Mountainous terrain with dense forests and trees, peaceful and serene, in the vicinity of garden of God of Victor, Colorado, USA. Shot on a Canon EOS R6 with a Canon RF 24-105mm f/4L IS USM Lens,, 4K film still, natural lighting, vibrant colors, crisp details, and soft shadows.'
        userPrompt = f'I want you to write a DALL-E image generation prompt to generate an image related to {attractionName} in the town of  {self.city_name}'
        # messages = [{'role': 'system', 'content': systemContent}, {'role': 'user', 'content': userPrompt}]
        chatgpt_text_messages = [ {"role": "system", "content": systemContent}, {'role': 'user', 'content': userPrompt} ]

        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chatgpt_text_messages,
            temperature=1,
            max_tokens=300,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        message = response.choices[0].message.content
        # print(message)
        return message
    
    def getCityCordinates (self):
        base_url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {
            "address": self.city_name,
            "key": self.gmaps_key
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if len(data['results'])>0:
                self.cityLocation = data['results'][0]['geometry']['location']
                # print(f"{self.city_name} locates at {self.cityLocation['lat']}, {self.cityLocation['lng']}")
                print(f"\n Obtained {self.city_name} coordinates\n")
                return self.cityLocation
        return None, None
    
    def getTopAttractions(self, radius=3000, type='tourist_attraction'):
        cityCoord = self.getCityCordinates()
        base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        params = {
        "location": f"{cityCoord['lat']},{cityCoord['lng']}",
        "radius": radius,
        "type": type,
        "key": self.gmaps_key
        }
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if 'results' in data:
                print('\n Getting cooridnates for top attractions within the radius of {radius} meters from CityCenter \n')
                return data['results'][:self.numAttractions]
        return None
    
    def generateAttractionsImage(self):
        self.topLocations = self.getTopAttractions()
        print(f"\n Generate image prompt for each of the top {len(self.topLocations)} attractions within {self.city_name} \n")
        self.topLocationsImageUrl = dict()
        for attraction in self.topLocations:
            print(f"generating image for {attraction['name']}")
            imagePrompt = self.generateImagePrompt(attraction['name'])
            # Generate the image
            print(f"\n \t Calling dall-e-3 api and generate image for {attraction['name']}\n")
            response = self.client.images.generate(
                model="dall-e-3",
                prompt=imagePrompt,
                n=1,
                size="1024x1024",
                quality="standard",
                style = 'natural'
            )
            # Get the image URL from the response
            image_url = response.data[0].url
            self.topLocationsImageUrl[attraction['name']] = image_url



class HistoricalOverviewModule:
    def __init__(self, destination):
        chatgpt_api_key = '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'
        self.client = OpenAI(api_key= chatgpt_api_key)
        self.destination = destination
        

    def generate_historical_overview(self):
        systemContent = "Please provide in details the important historical overviews around given destination. Please also separate two consecutive historical overviews with an empty line. Number of sentences for each historical overview should not be greater than 10."
        userPrompt = f"Please provide in details at most 5 important historical overviews around {self.destination}."
        # prompt = f"Give your answer as text that contains a list of cultural phrases followed by english meaning from the following: {phrases}. To be precise, the list should be comma separated such as the following format: A B, C D; where A is the phrase and B is the english meaning and so on. No other descriptions are needed."
        chatgpt_text_messages = [ {"role": "system", "content": systemContent}, {'role': 'user', 'content': userPrompt} ]

        # prompt = f"Please provide in details at most 5 important historical overviews around {place}. Please also separate two consecutive historical overviews with an empty line. Number of sentences for each historical overview should not be greater than 10."
        # chatgpt_text_messages.append(
        #     {
        #         "role" : "user",
        #         "content" : prompt
        #     }
        # )

        # Make an API call to get a response
        # response = openai.ChatCompletion.create(
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chatgpt_text_messages,
            temperature=1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # message = response['choices'][0]['message']
        message = response.choices[0].message
        chatgpt_text_messages.append(message)
        # response = message['content']
        response = message.content
        text = response


        topics = re.split(r'\n\s*\n', text)

        historical_overview_list = []
        # Print each separated topic
        for i, topic in enumerate(topics, start=1):
            # print(f"Topic {i}:\n{topic.strip()}\n")
            historical_overview_list.append(topic.strip())

        return response, historical_overview_list
    

    def generate_imagepromt_urllist_basedon_historical_overview(self, historical_overview_list):
        
        image_generation_prompt_list = []
        for historical_overview in historical_overview_list:
            # print("Current historial overview: ", historical_overview)
            systemContent = 'You write image generation prompts for DALL-E 3 from the given input description. Basically, you must extract 3-5 most important information (each information should consist of at most 5 words) from the input description. The extract information should cover all the topics discussed in the input description. Please keep your answer short and concise. Do not use any numeric order among them, it should be just comma separated.'
            userPrompt = f'{historical_overview}'
            # messages = [{'role': 'system', 'content': systemContent}, {'role': 'user', 'content': userPrompt}]
            chatgpt_text_messages = [ {"role": "system", "content": systemContent}, {'role': 'user', 'content': userPrompt} ]

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=chatgpt_text_messages,
                temperature=1,
                max_tokens=1000,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            # message = response['choices'][0]['message']
            message = response.choices[0].message
            # chatgpt_text_messages.append(message)
            # response = message['content']
            response = message.content
            # print("Image prompt: ", response)
            image_generation_prompt_list.append((historical_overview, response))

        return image_generation_prompt_list
        


    def generate_image_from_image_prompt(self, image_promt):
        # client = OpenAI()
        response = self.client.images.generate(
            model="dall-e-3",
            prompt=image_promt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url
        
        return image_url
    


class PersonalizedItineraryGenerator:

    def __init__(self, user_preferences, current_location, destination, transportation_mode):
        # openai.api_key = self.GPT_API_KEY
        chatgpt_api_key = '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'
        self.client = OpenAI(api_key= chatgpt_api_key)
        # self.client = OpenAI()
        self.user_preferences = user_preferences
        self.current_location = current_location
        self.destination = destination
        self.transportation_mode = transportation_mode

    def generate_personalized_itinerary(self):
        interests = self.user_preferences.get('interests', [])
        dietary_restrictions = self.user_preferences.get('dietary_restrictions', '')
        budget = self.user_preferences.get('budget', 0)
        number_of_days = self.user_preferences.get("number_of_days", 1)

        # Generate personalized itinerary using GPT
        # prompt = f"Create a personalized itinerary for a trip for {number_of_days} days from {current_location} to {destination} with interests: {', '.join(interests)}, dietary restrictions: {dietary_restrictions}, and budget: {budget}. Please keep your answers short."

        systemContent = "Create a personalized itinerary for a trip for given number_of_days from user given current location to user given destination with considering the user given restrictions on personal interestes, dietary restrictions, and budget. Please also keep in mind the user given preference on transportation mode."
        userPrompt = f"Create a personalized itinerary for a trip for {number_of_days} days from {self.current_location} to {self.destination} with interests: {', '.join(interests)}, dietary restrictions: {dietary_restrictions}, and budget: {budget}. Users prefer {self.transportation_mode} transportation mode for the trip."
        # prompt = f"Give your answer as text that contains a list of cultural phrases followed by english meaning from the following: {phrases}. To be precise, the list should be comma separated such as the following format: A B, C D; where A is the phrase and B is the english meaning and so on. No other descriptions are needed."
        chatgpt_text_messages = [ {"role": "system", "content": systemContent}, {'role': 'user', 'content': userPrompt} ]

        # chatgpt_text_messages.append(
        #     {
        #         "role" : "user",
        #         "content" : prompt
        #     }
        # )

        # Make an API call to get a response
        # response = openai.ChatCompletion.create(
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=chatgpt_text_messages,
            temperature=1,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # message = response['choices'][0]['message']
        message = response.choices[0].message
        # chatgpt_text_messages.append(message)
        # response = message['content']
        response = message.content
        return response

class UtilityModule:
    def __init__(self):
        pass

    def open_image_from_url(self,image_url):
        try:
            # Download the image
            response = requests.get(image_url)
            response.raise_for_status()

            # Open the image using Pillow
            image = PIL.Image.open(BytesIO(response.content))

            # Display the image
            image.show()

        except Exception as e:
            print(f"Error: {e}")


    def save_image_from_url(self,image_url, image_name, save_directory, subdirectory_name):
        try:
            # Download the image
            response = requests.get(image_url)
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)
            if not os.path.exists(os.path.join(save_directory, subdirectory_name)):
                os.makedirs(os.path.join(save_directory, subdirectory_name))
            with open(os.path.join(save_directory, subdirectory_name, f"{image_name}.png"), 'wb') as f:
                f.write(response.content)

        except Exception as e:
            print(f"Cannot Find The Image Error: {e}")
    

# User Interface
def main():
    # Instantiate modules
    # api_key = 'your-api-key'  # Replace with your OpenAI API key
    # culture_language_module = CultureAndLanguageModule(api_key)
    # culture_language_module = CultureAndLanguageModule()
    # openai_key = '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'
    # gmaps_key = 'AIzaSyAzKG2cNwaXnqgNh8MzWRqCPMVTKsCQPQc'
    # city_exploration_module = VirtualCityExplorationModule(cityName, openai_key, gmaps_key, NumberofAttractions=5)
    # historical_overview_module = HistoricalOverviewModule()
    # itinerary_generator = PersonalizedItineraryGenerator()

    # chatgpt_text_messages = [
    #     {
    #         "role": "system",
    #         "content": ""
    #     }
    # ]
    pass

    # # User inputs
    # # destination = input("Enter your destination: ")
    # # city_exploration_module = VirtualCityExplorationModule(destination, openai_key, gmaps_key)
    # # city_exploration_module.generateAttractionsImage()

    # # preferences = {
    # #     "interests": input("Enter your interests (comma-separated): ").split(","),
    # #     "dietary_restrictions": input("Enter your dietary restrictions: "),
    # #     "budget": float(input("Enter your budget: ")),
    # # }
    # # landmark_info = input("Enter landmark information: ")
    # # transportation_mode = input("Enter preferred transportation mode: ")
    # current_location = "Chicago"
    # destination = "Madrid"
    # preferences = {
    #     "interests": ["Sport"],
    #     "dietary_restrictions": "Halal",
    #     "budget": 1000,
    #     "number_of_days": 7
    # }
    # # landmark_info = "CampNou"
    # transportation_mode = "Driving"

    # # Instantiate modules
    
    # gmaps_key = 'AIzaSyAzKG2cNwaXnqgNh8MzWRqCPMVTKsCQPQc'
    # set_api_key("3af892a1fb2875dfe482a456441d6ea4")

    # utility_module = UtilityModule()
    


    # print("\n\nVirtual City Exploration.")
    # city_exploration_module = VirtualCityExplorationModule(destination, gmaps_key)
    # city_exploration_module.generateAttractionsImage()
    
    # culture_language_module = CultureAndLanguageModule(destination)
    # cultural_insights = culture_language_module.get_cultural_insights()
    # print("\n\n### Cultural Insights ###")
    # print(cultural_insights)
    # common_phrases = culture_language_module.get_common_phrases()
    # print("\n\n### Common Phrases ###")
    # print(common_phrases)
    # culture_language_module.get_audio_pronunciations(common_phrases)
    # culture_language_module = CultureAndLanguageModule(destination)
    # cultural_insights = culture_language_module.get_cultural_insights()
    # print("\n\n### Cultural Insights ###")
    # print(cultural_insights)
    # common_phrases = culture_language_module.get_common_phrases()
    # print("\n\n### Common Phrases ###")
    # print(common_phrases)
    # culture_language_module.get_audio_pronunciations(common_phrases)

    # historical_overview_module = HistoricalOverviewModule(destination)
    # historical_overview_result,historical_overview_result_list = historical_overview_module.generate_historical_overview()
    # print("\n\n### Historical Overview ###")
    # print(historical_overview_result)
    # image_prompts_list = historical_overview_module.generate_imagepromt_urllist_basedon_historical_overview(historical_overview_result_list)
    # print("\n\n### Image Prompts List ###")
    # image_urls = []
    # image_number = 1
    # for historical_overview, image_prompt in image_prompts_list:
    #     print(image_prompt)
    #     image_url = historical_overview_module.generate_image_from_image_prompt(image_prompt)
    #     # print("image url: ", image_url)
    #     image_urls.append(image_url)
    #     utility_module.save_image_from_url(image_url, str(image_number), destination.replace(' ', '-'), "HistoricalOverviewImages")
    #     image_number = image_number + 1


        

    # # print("\n\nShowing Images")
    # # for url in image_urls:
    # #     utility_module.open_image_from_url(url)

    # itinerary_generator = PersonalizedItineraryGenerator(preferences, current_location, destination)
    # personalized_itinerary = itinerary_generator.generate_personalized_itinerary()
    # print("\n### Personalized Itinerary ###")
    # print(personalized_itinerary)
    # itinerary_generator = PersonalizedItineraryGenerator(preferences, current_location, destination)
    # personalized_itinerary = itinerary_generator.generate_personalized_itinerary()
    # print("\n### Personalized Itinerary ###")
    # print(personalized_itinerary)

    

    


# Sample inputs
# Enter your destination: Paris
# Enter your interests (comma-separated): History,Art
# Enter your dietary restrictions: Vegetarian
# Enter your budget: 1000
# Enter landmark information: Eiffel Tower
# Enter preferred transportation mode: Walking

if __name__ == "__main__":
    main()
