

import re

# Input text
input_text = """
### Historical Overview ###
1. The Visigothic Era (6th - 8th centuries): During this period, the region of Madrid was under the rule of the Visigoths, a Germanic tribe. Although Madrid itself was not a prominent city at the time, it was an important strategic location due to its proximity to the Tagus River. The most significant event during this era was the Councils of Toledo, where important decisions were made and laws were established.

2. Arab Rule and the Moors (8th - 11th centuries): In the early 8th century, the Umayyad Caliphate invaded the Iberian Peninsula, including the region around Madrid. The city then became part of Al-Andalus, the Muslim territory in Spain. During this period, the city was known as "Mayrit" and developed as a frontier fortress. One noteworthy event was the construction of the Alcázar of Madrid, which served as the residence for various Arab rulers.

3. Christian Reconquest and Habsburg Rule (11th - 16th centuries): In the 11th century, Christian forces from the Kingdom of Castile began the Reconquista, the reconquest of the Iberian Peninsula from the Moors. Madrid played a strategic role in this process and the city gradually transitioned into Christian hands. Significant events during this era include the conquest of Madrid by the forces of Alfonso VI of Castile in the 11th century and its subsequent incorporation into the Crown of Castile.

4. Bourbon Dynasty and Modernization (18th - 19th centuries): In the 18th century, the Bourbon Dynasty ascended to the Spanish throne, ushering in an era of reforms and modernization. Madrid became the official capital of Spain in 1561, under the reign of Philip II. During this time, Madrid witnessed the construction of many important buildings and urban development projects, such as the Royal Palace and the creation of the city's iconic boulevards and squares.

5. Spanish Civil War and Dictatorship (20th century): Madrid played a crucial role during the Spanish Civil War (1936-1939), as it remained loyal to the Republican government. The city was heavily bombarded by Francoist forces, enduring a lengthy and brutal siege. The war had a profound impact on the city and its people. Following the war, Spain experienced a lengthy period of dictatorship under Francisco Franco, which significantly shaped the political and social landscape of Madrid.

These historical overviews provide a brief glimpse into some of the major epochs and events that have shaped the history of Madrid. Each era has left its mark on the city and contributed to its rich and complex heritage.
"""

# Use regular expression to find bullet points
bullet_points = re.findall(r'\d+\.\s+(.+)', input_text)

# Print the result
image_generation_list = []
for point in bullet_points:
    image_generation_list.append(str(point.strip()))

print(image_generation_list)
