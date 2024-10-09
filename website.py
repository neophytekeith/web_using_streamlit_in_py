import requests
from streamlit import *
from streamlit_lottie import st_lottie

#https://www.webfx.com/tools/emoji-cheat-sheet/
set_page_config(page_title="Website ni Keith", page_icon="👾", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://lottie.host/0de42146-b608-492a-8e47-2a9dec937f6d/78WXdFxMQs.json")
lottie_robot = load_lottieurl("https://lottie.host/d698fee8-07c0-4052-b415-975a5f8eae69/XTxe2VPFJa.json")

with container():
    left_column, right_column = columns(2)
    with left_column:
        markdown("<h3>Hi, I'm <span style='color: #FF5733;'>Keith!</span></h3>", unsafe_allow_html=True)
        markdown("<h4><strong> A second year <span style='color: #02fa0b;'>computer science</span> student. </strong></h4>", unsafe_allow_html=True)
        write(f"I’m passionate about coding, technology, and exploring new tools in the field.")
        write("Currently honing my skills in web development and problem solving, I’m always eager to learn and grow in the tech world.")
    with right_column:
        st_lottie(lottie_robot, height=300, key="robot")

with container():
    write("---")
    left_column, right_column = columns(2)
    with left_column:
        header("What I Do")
        write(
              """
            Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Maecenas porttitor congue massa. Fusce posuere, magna sed pulvinar ultricies, purus lectus malesuada libero, sit amet commodo magna eros quis urna. Nunc viverra imperdiet enim. Fusce est.
            Vivamus a tellus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin pharetra nonummy pede. Mauris et orci. Aenean nec lorem.
            In porttitor. Donec laoreet nonummy augue. Suspendisse dui purus, scelerisque at, vulputate vitae, pretium mattis, nunc. Mauris eget neque at sem venenatis eleifend. Ut nonummy.
              """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
        
write("---")
markdown("<h2>Contact Me</h2>", unsafe_allow_html=True)

contact = """
<form action="https://submit-form.com/oztAIJPms" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="hidden" name="_redirect" value="https://keithwebusingstinpy.streamlit.app/">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email"  required>
     <textarea name="message" placeholder = "Your message"  required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = columns(2)
with left_column:
    markdown(contact, unsafe_allow_html=True)
with right_column:
    empty()
markdown("""
<div style="text-align: center;">
    <p>
        <a href="https://www.facebook.com/rnzrmbln">FACEBOOK </a> | 
        <a href="https://www.instagram.com/kith_rrr">INSTAGRAM </a> |
        <a href="https://github.com/neophytekeith">GITHUB </a> 
    </p>
</div>
""", unsafe_allow_html=True)

