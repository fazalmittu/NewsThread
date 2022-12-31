import os
import openai
from dotenv import load_dotenv
import json

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_thread(text: str):

    context = """
                Here is an example: 

                Intro: Paleontologists have long been enthralled by the fossilized record of mass death events in the West Union Canyon of Nevada. After decades of research, a new study published in Current Biology has finally solved the mystery. Here are 8 tweets delineating the research process and findings of this study!
                1. The fossilized site in the West Union Canyon of Nevada has captivated paleontologists for decades. It is home to a mass death event of whale-sized ichthyosaurs, which swam the seas while dinosaurs walked the earth. 
                2. A research team conducted a study to investigate this enigma, and published their results in the journal Current Biology. To uncover the cause of the mass death, they used 3-D scans to digitally reconstruct the fossils and observe sedimentology, oxygen and mercury levels. 
                3. In addition, the research team also studied museum collections of tiny Shonisaurus bones to make an unexpected discovery: instead of a graveyard of mass death, the canyon served as a wellspring of mass life. 
                4. These fossilized bones contained embryos and newborns of the ichthyosaurs, suggesting that the animals were coming here to give birth. The findings indicate that the ichthyosaurs lived and traveled in large groups, similarly to whales today. 
                5. This addendum to the mass death hypothesis provides a more complete evolutionary picture of these marine reptiles. The new evidence suggests that the massive creatures used the canyon as a birthing ground, and not as an unlucky site of death. 
                6. The research team also believes that this technique could be applied to other turtle-rich fossil sites similarly to uncover more details about their original depths and environments. 
                7. This study is a great example of how lateral thinking and creative problem solving can be used to uncover the secrets of the fossil record. It reveals the power of interdisciplinary efforts, merging the efforts of archaeologists, geophysicists, and experts on this new technique. 
                8. The findings of this study offer a unique way to explore the fossil records of the universe and provide valuable insights into the history of the Levant and its different narratives. It has opened up a world of possibilities for scientists, and will hopefully help answer the biggest mystery of all: why the ichthyosaurs went extinct 88 million years ago.

                Here is another example: 

                Intro: Archaeologists and geophysicists have long been trying to discover the hidden secrets behind the timelines of different historical movements and military campaigns recorded in the Bible. After years of hard work, a new technique  called archaeomagnetic dating has been developed. Here are 8 tweets about this incredible new discovery! 
                1. Archaeomagnetic dating is a revolutionary new method that scientists are using to gain insights into the history of the Levant and its different narratives. It utilizes the consistently reliable geomagnetic data to accurately date organic remains and archaeological artifacts. 
                2. This technique can help determine the date when certain layers of sediment might have been destroyed during biblical battles, as reflected in the magnetic signals of burned materials recorded at different sites. 
                3. The new dating method can provide a sort of “geobiblical clock”, allowing experts to narrow things down to a decadal level, which is extremely important for understanding ancient historical events and connecting them to the archaeological record. 
                4. Archaeomagnetic dating stands out for its interdisciplinary approach, as it combines the efforts of archaeologists, geophysicists, and experts on the new technique. It also provides valuable information on Earth’s magnetic field, which is one of the most mysterious phenomena in geoscience. 
                5. By examining the magnetic readings of burned materials at various sites, the researchers have been able to accurately recreate the intensity of Earth’s magnetic field on the day of the Babylonian army's annihilation of the First Temple, as well as other historical events. 
                6. The new data disproves previous claims regarding the destruction of the ancient settlement of Tel Beit She’an and establishes that it was burned to the ground some 70 to 100 years earlier, linking the destruction to the Egyptian pharaoh Shoshenq’s campaign. 
                7. Furthermore, the data has helped settle the longstanding debate over how exactly the Kingdom of Judah fell by providing evidence that the intensity of the magnetic field as recorded in the destruction layer of the site of Malhata was different and significantly lower than the one recorded in the Babylonian destruction of Jerusalem.
                8. The findings from this revolutionary new technique have opened up a world of possibilities for scientists, offering an unprecedented way to explore the universe and uncover its secrets. #ArchaeomagneticDating #GeobiblicalClock #LevantHistory

                Write me an in depth thread about the article above that includes specific details listed in the article. If there are any important quotes, then add those in the thread. Make each tweet less than 280 characters and don't use any hashtags. The thread should have 8 tweets. Include an introduction, background information, and explain the overall impact of the discussed topic. 

                Write the thread: 

              """

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Write me a twitter thread that is 8 tweets long for the following article." +
               "Article: " + text + context,
        temperature=0.85,
        max_tokens=597,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    # print(json.dumps(response, indent=4))

    return response.choices[0].text