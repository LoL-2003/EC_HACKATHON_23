# import streamlit as st
# from audio_recorder_streamlit import audio_recorder
# import requests
# import os
# import time

# LANGUAGES = {
#     'afrikaans': 'af',
#     'albanian': 'sq',
#     'amharic': 'am',
#     'arabic': 'ar',
#     'armenian': 'hy',
#     'azerbaijani': 'az',
#     'basque': 'eu',
#     'belarusian': 'be',
#     'bengali': 'bn',
#     'bosnian': 'bs',
#     'bulgarian': 'bg',
#     'catalan': 'ca',
#     'cebuano': 'ceb',
#     'chichewa': 'ny',
#     'chinese (simplified)': 'zh-cn',
#     'chinese (traditional)': 'zh-tw',
#     'corsican': 'co',
#     'croatian': 'hr',
#     'czech': 'cs',
#     'danish': 'da',
#     'dutch': 'nl',
#     'english': 'en',
#     'esperanto': 'eo',
#     'estonian': 'et',
#     'filipino': 'tl',
#     'finnish': 'fi',
#     'french': 'fr',
#     'frisian': 'fy',
#     'galician': 'gl',
#     'georgian': 'ka',
#     'german': 'de',
#     'greek': 'el',
#     'gujarati': 'gu',
#     'haitian creole': 'ht',
#     'hausa': 'ha',
#     'hawaiian': 'haw',
#     'hebrew': 'iw',
#     'hebrew': 'he',
#     'hindi': 'hi',
#     'hmong': 'hmn',
#     'hungarian': 'hu',
#     'icelandic': 'is',
#     'igbo': 'ig',
#     'indonesian': 'id',
#     'irish': 'ga',
#     'italian': 'it',
#     'japanese': 'ja',
#     'javanese': 'jw',
#     'kannada': 'kn',
#     'kazakh': 'kk',
#     'khmer': 'km',
#     'korean': 'ko',
#     'kurdish (kurmanji)': 'ku',
#     'kyrgyz': 'ky',
#     'lao': 'lo',
#     'latin': 'la',
#     'latvian': 'lv',
#     'lithuanian': 'lt',
#     'luxembourgish': 'lb',
#     'macedonian': 'mk',
#     'malagasy': 'mg',
#     'malay': 'ms',
#     'malayalam': 'ml',
#     'maltese': 'mt',
#     'maori': 'mi',
#     'marathi': 'mr',
#     'mongolian': 'mn',
#     'myanmar (burmese)': 'my',
#     'nepali': 'ne',
#     'norwegian': 'no',
#     'odia': 'or',
#     'pashto': 'ps',
#     'persian': 'fa',
#     'polish': 'pl',
#     'portuguese': 'pt',
#     'punjabi': 'pa',
#     'romanian': 'ro',
#     'russian': 'ru',
#     'samoan': 'sm',
#     'scots gaelic': 'gd',
#     'serbian': 'sr',
#     'sesotho': 'st',
#     'shona': 'sn',
#     'sindhi': 'sd',
#     'sinhala': 'si',
#     'slovak': 'sk',
#     'slovenian': 'sl',
#     'somali': 'so',
#     'spanish': 'es',
#     'sundanese': 'su',
#     'swahili': 'sw',
#     'swedish': 'sv',
#     'tajik': 'tg',
#     'tamil': 'ta',
#     'telugu': 'te',
#     'thai': 'th',
#     'turkish': 'tr',
#     'ukrainian': 'uk',
#     'urdu': 'ur',
#     'uyghur': 'ug',
#     'uzbek': 'uz',
#     'vietnamese': 'vi',
#     'welsh': 'cy',
#     'xhosa': 'xh',
#     'yiddish': 'yi',
#     'yoruba': 'yo',
#     'zulu': 'zu',
# }

# # Create a list of language names from the LANGUAGES dictionary
# language_names = list(LANGUAGES.keys())

# in_lang = st.selectbox(
#     "Select your input language",
#     language_names
# )

# # Use the selected language name to get the language code from the LANGUAGES dictionary
# input_language = LANGUAGES.get(in_lang, "en")  # Default to English if not found

# out_lang = st.selectbox(
#     "Select your output language",
#     language_names
# )

# # Use the selected language name to get the language code from the LANGUAGES dictionary
# output_language = LANGUAGES.get(out_lang, "en")  # Default to English if not found


# english_accent = st.selectbox(
#     "Select your english accent",
#     (
#         "Default",
#         "India",
#         "United Kingdom",
#         "United States",
#         "Canada",
#         "Australia",
#         "Ireland",
#         "South Africa",
#     ),
# )

# st.set_page_config(page_title="EC_HACKATHON-2023")

# def header_footer():
#     st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
#     st.markdown("""
#     <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
#       <div class="container-fluid">
#         <a class="navbar-brand" href="#"><img 
#           src= 
#     "https://assets-global.website-files.com/5fac161927bf86485ba43fd0/6229d40f625c70840c12bcd7_BlogGif_2.gif" 
#           alt="" width="150" 
#           height="45"></a></a>
#         <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavbar">
#           <span class="navbar-toggler-icon"></span>
#         </button>
#         <div class="collapse navbar-collapse" id="collapsibleNavbar">
#           <ul class="navbar-nav">
#             <li class="nav-item">
#               <a class="nav-link" href="#">Contact Us</a>
#             </li>
#             <li class="nav-item">
#               <a class="nav-link" href="#">GitHub</a>
#             </li>
#             <li class="nav-item">
#               <a class="nav-link" href="#">About Project</a>
#             </li>
#           </ul>
#         </div>
#       </div>
#     </nav>
#     """, unsafe_allow_html=True)
#     hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             footer:after {content:'Made with ❤️ by ADITYA PURI';visibility: visible;display: block;}
#             .st-emotion-cache-cio0dv {
#             padding-left: 20%;
#             padding-right: 1rem;
#             }
#             header {visibility: hidden;}
#             </style>
#             """
#     st.markdown(hide_st_style, unsafe_allow_html=True)
    
# header_footer()

# st.write("Select an option:")
# option = st.radio(
#     'How would you like to use the bot?',
#     ('Record & Transcribe', 'Transcribe Pre-recorded Audio')
# )

# if option == 'Record & Transcribe':
#     st.subheader("Voice Recorder and Transcription Bot")
#     st.write("Record and play back your voice")

#     st.write("Click the 'Record' button to start recording:")
#     recorded_audio_bytes = audio_recorder()
#     if recorded_audio_bytes:
#         st.audio(recorded_audio_bytes, format="audio/wav", start_time=0)

#     if st.button("Play Recorded Audio") and recorded_audio_bytes:
#         st.write("Playing recorded audio:")
#         st.audio(recorded_audio_bytes, format="audio/wav", start_time=0)

#     if st.button("Transcribe Recorded Audio") and recorded_audio_bytes:
#      st.write("Transcribing recorded audio:")
#      transcript_container = st.empty()
#      headers = {"Authorization": "Bearer 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"}

#      with st.spinner("Transcribing..."):
#         API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v2"
#         response = requests.post(API_URL, headers=headers, data=recorded_audio_bytes)
#         output = response.json().get('text', "")

#         transcript = "**Bot🤖:** "
#         for char in output:
#             transcript += char
#             transcript_container.markdown(transcript)
#             time.sleep(0.05)
            
#         st.success("Transcription completed")
#         st.balloons()

# else:
#     st.write("Audio Transcription from Pre-recorded Files")
#     st.caption("Upload an audio file, and the bot will transcribe it for you.")
#     uploaded_file = st.file_uploader("Upload an audio file (MP3, WAV, etc.)")
#     API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v2"

#     if uploaded_file is not None:
#         st.audio(uploaded_file, format="audio/mp3", start_time=0)
#         st.write("Transcription:")
#         transcript_container = st.empty()

#         audio_file_path = "temp_audio" + os.path.splitext(uploaded_file.name)[-1]
#         with open(audio_file_path, "wb") as f:
#             f.write(uploaded_file.read())

#         with open(audio_file_path, "rb") as f:
#             audio_data = f.read()

#         headers = {"Authorization": "Bearer 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"}

#         with st.spinner("Transcribing..."):
#             response = requests.post(API_URL, headers=headers, data=audio_data)
#             output = response.json().get('text', "")

#             transcript = "**Bot🤖:** "
#             for char in output:
#                 transcript += char
#                 transcript_container.markdown(transcript)
#                 time.sleep(0.05)

#         st.success("Transcription completed")
#         st.balloons()


import streamlit as st
from audio_recorder_streamlit import audio_recorder
import requests
import os
import time
import glob
from gtts import gTTS
from googletrans import Translator

LANGUAGES = {
    'default(hindi)': 'hi',
    'afrikaans': 'af',
    'albanian': 'sq',
    'amharic': 'am',
    'arabic': 'ar',
    'armenian': 'hy',
    'azerbaijani': 'az',
    'basque': 'eu',
    'belarusian': 'be',
    'bengali': 'bn',
    'bosnian': 'bs',
    'bulgarian': 'bg',
    'catalan': 'ca',
    'cebuano': 'ceb',
    'chichewa': 'ny',
    'chinese (simplified)': 'zh-cn',
    'chinese (traditional)': 'zh-tw',
    'corsican': 'co',
    'croatian': 'hr',
    'czech': 'cs',
    'danish': 'da',
    'dutch': 'nl',
    'english': 'en',
    'esperanto': 'eo',
    'estonian': 'et',
    'filipino': 'tl',
    'finnish': 'fi',
    'french': 'fr',
    'frisian': 'fy',
    'galician': 'gl',
    'georgian': 'ka',
    'german': 'de',
    'greek': 'el',
    'gujarati': 'gu',
    'haitian creole': 'ht',
    'hausa': 'ha',
    'hawaiian': 'haw',
    'hebrew': 'iw',
    'hebrew': 'he',
    'hindi': 'hi',
    'hmong': 'hmn',
    'hungarian': 'hu',
    'icelandic': 'is',
    'igbo': 'ig',
    'indonesian': 'id',
    'irish': 'ga',
    'italian': 'it',
    'japanese': 'ja',
    'javanese': 'jw',
    'kannada': 'kn',
    'kazakh': 'kk',
    'khmer': 'km',
    'korean': 'ko',
    'kurdish (kurmanji)': 'ku',
    'kyrgyz': 'ky',
    'lao': 'lo',
    'latin': 'la',
    'latvian': 'lv',
    'lithuanian': 'lt',
    'luxembourgish': 'lb',
    'macedonian': 'mk',
    'malagasy': 'mg',
    'malay': 'ms',
    'malayalam': 'ml',
    'maltese': 'mt',
    'maori': 'mi',
    'marathi': 'mr',
    'mongolian': 'mn',
    'myanmar (burmese)': 'my',
    'nepali': 'ne',
    'norwegian': 'no',
    'odia': 'or',
    'pashto': 'ps',
    'persian': 'fa',
    'polish': 'pl',
    'portuguese': 'pt',
    'punjabi': 'pa',
    'romanian': 'ro',
    'russian': 'ru',
    'samoan': 'sm',
    'scots gaelic': 'gd',
    'serbian': 'sr',
    'sesotho': 'st',
    'shona': 'sn',
    'sindhi': 'sd',
    'sinhala': 'si',
    'slovak': 'sk',
    'slovenian': 'sl',
    'somali': 'so',
    'spanish': 'es',
    'sundanese': 'su',
    'swahili': 'sw',
    'swedish': 'sv',
    'tajik': 'tg',
    'tamil': 'ta',
    'telugu': 'te',
    'thai': 'th',
    'turkish': 'tr',
    'ukrainian': 'uk',
    'urdu': 'ur',
    'uyghur': 'ug',
    'uzbek': 'uz',
    'vietnamese': 'vi',
    'welsh': 'cy',
    'xhosa': 'xh',
    'yiddish': 'yi',
    'yoruba': 'yo',
    'zulu': 'zu',
}

translator = Translator()

def text_Tmodel(transcribe_Text):
    text = transcribe_Text

    language_names = list(LANGUAGES.keys())

    input_language = 'en'  # Default to English 

    out_lang = st.selectbox(
        "Select your output language",
        language_names
    )

    output_language = LANGUAGES.get(out_lang, "hi")  # Default to English if not found
    english_accent = st.selectbox(
        "Select your english accent",
        (
            "Default",
            "India",
            "United Kingdom",
            "United States",
            "Canada",
            "Australia",
            "Ireland",
            "South Africa",
        ),
    )
    if english_accent == "Default":
        tld = "co.in"
    elif english_accent == "India":
        tld = "co.in"
    elif english_accent == "United Kingdom":
        tld = "co.uk"
    elif english_accent == "United States":
        tld = "com"
    elif english_accent == "Canada":
        tld = "ca"
    elif english_accent == "Australia":
        tld = "com.au"
    elif english_accent == "Ireland":
        tld = "ie"
    elif english_accent == "South Africa":
        tld = "co.za"
        
    if not os.path.exists("temp"):
        os.makedirs("temp")
    translation = translator.translate(text, src=input_language, dest=output_language)
    trans_text = translation.text
    tts= gTTS(trans_text, lang=output_language, tld=tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    
    # Here, we play the generated audio using the st.audio() function
    audio_file = open(f"temp/{my_file_name}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3", start_time=0,)
    display_output_text = st.checkbox("Display transcription")
    if display_output_text:
        st.markdown(f"## transcription text:")
        st.write(f" {trans_text}")


st.set_page_config(page_title="EC_HACKATHON-2023")

def header_footer():
    st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
    st.markdown("""
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
      <div class="container-fluid">
        <a class="navbar-brand" href="#"><img 
          src= 
    "https://assets-global.website-files.com/5fac161927bf86485ba43fd0/6229d40f625c70840c12bcd7_BlogGif_2.gif" 
          alt="" width="150" 
          height="45"></a></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavbar">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="collapsibleNavbar">
          <ul class="navbar-nav">
            <li class="nav-item">
              <a class="nav-link" href="#">Contact Us</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">GitHub</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">About Project</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    """, unsafe_allow_html=True)
    hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {content:'Made with ❤️ by ADITYA PURI';visibility: visible;display: block;}
            .st-emotion-cache-cio0dv {
            padding-left: 20%;
            padding-right: 1rem;
            }
            header {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)
    
header_footer()
st.title('EC HACKATHON 2023')
st.write("Select an option:")
option = st.radio(
    'How would you like to use the bot?',
    ('Transcribe Pre-recorded Audio', 'Record & Transcribe')
)

if option == 'Transcribe Pre-recorded Audio':
    st.write("Audio Transcription from Pre-recorded Files")
    st.caption("Upload an audio file, and the bot will transcribe it for you.")
    uploaded_file = st.file_uploader("Upload an audio file (MP3, WAV, etc.)")
    API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v2"

    if uploaded_file is not None:
        st.audio(uploaded_file, format="audio/mp3", start_time=0)
        st.write("Transcription:")
        transcript_container = st.empty()

        audio_file_path = "temp_audio" + os.path.splitext(uploaded_file.name)[-1]
        with open(audio_file_path, "wb") as f:
            f.write(uploaded_file.read())

        with open(audio_file_path, "rb") as f:
            audio_data = f.read()

        headers = {"Authorization": "Bearer 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"}

        with st.spinner("Transcribing..."):
            response = requests.post(API_URL, headers=headers, data=audio_data)
            output = response.json().get('text', "")

            transcript = "**Bot🤖:** "
            for char in output:
                transcript += char
                transcript_container.markdown(transcript)
                time.sleep(0.05)
            text_Tmodel(output)
        st.success("Transcription completed")
        st.balloons()

    st.subheader("Voice Recorder and Transcription Bot")
    st.write("Record and play back your voice")
else:
    st.write("Click the 'Record' button to start recording:")
    recorded_audio_bytes = audio_recorder()
    if recorded_audio_bytes:
        st.audio(recorded_audio_bytes, format="audio/wav", start_time=0)

    if st.button("Play Recorded Audio") and recorded_audio_bytes:
        st.write("Playing recorded audio:")
        st.audio(recorded_audio_bytes, format="audio/wav", start_time=0)

    if st.button("Transcribe Recorded Audio") and recorded_audio_bytes:
     st.write("Transcribing recorded audio:")
     transcript_container = st.empty()
     headers = {"Authorization": "Bearer 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"}

     with st.spinner("Transcribing..."):
        API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v2"
        response = requests.post(API_URL, headers=headers, data=recorded_audio_bytes)
        output = response.json().get('text', "")

        transcript = "**Bot🤖:** "
        for char in output:
            transcript += char
            transcript_container.markdown(transcript)
            time.sleep(0.05)
        #text_Tmodel(output)
     st.success("Transcription completed")
     st.balloons()
