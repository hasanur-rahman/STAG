from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="Witness the resilience during the Spanish Civil War: Amidst the turmoil of the 1930s, visualize the perseverance of Madrid as it became the heart of the Republican faction during the Spanish Civil War. Capture the spirit of defiance against the Nationalist forces, showcases of solidarity, and the brave citizens who faced the intense bombardment and siege.",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)