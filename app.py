import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import io
import base64
from streamlit_option_menu import option_menu
import os
import about # Import the about page

def save_uploaded_file(uploaded_file, filename):
    with open(os.path.join("Documents", filename), "wb") as f:
        f.write(uploaded_file.getbuffer())


# Set page config
st.set_page_config(page_title="GAN Image Generator", layout="wide")

# Load model
@st.cache_resource
def load_generator_model():
    return tf.keras.models.load_model("C:\\Users\\ASUS\\Desktop\\Streamlitwebgan\\checkponts\\generator_model.h5")

generator = load_generator_model()

# Function to generate an image
def generate_image(model, noise_dim=100):
    noise = tf.random.normal([1, noise_dim])
    generated_image = model(noise, training=False)
    generated_image = (generated_image[0] * 127.5 + 127.5).numpy().astype(np.uint8)
    return generated_image

# Helper function to encode images to base64
def image_to_base64(img):
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Add background color using CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #e0f7fa;  /* Light cyan background */
    }
    .navigation-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .image-container {
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin-top: 20px;
    }
    .image-container div {
        text-align: center;
    }
    .img {
        width: 300px;
        height: 300px;
        object-fit: cover;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .download-button-container {
        display: flex;
        justify-content: center;
        margin-top: 20px;
    }
    .download-button {
        background-color: #1976D2; /* Dark, muted blue color */
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app
# Navigasi
with st.sidebar:
    selected = option_menu("Menu", ["Beranda", "Tentang"], 
        icons=['house', "list-task"], 
        menu_icon="cast", default_index=0, orientation="vertical")

if selected == "Beranda":
    st.title("GAN Image Generator")

    # Paragraf tentang GAN
    st.markdown("""
    <div class="justified-text">
        <p>
            <strong>Generative Adversarial Networks (GANs)</strong> adalah kelas model pembelajaran mesin yang digunakan untuk menghasilkan data baru yang serupa dengan data yang ada. GAN terdiri dari dua jaringan saraf yang saling bersaing satu sama lain: Generator, yang mencoba membuat data palsu yang tampak nyata, dan Discriminator, yang mencoba membedakan antara data nyata dan data palsu. Melalui proses pelatihan, Generator belajar membuat data yang semakin sulit dibedakan oleh Discriminator.
        </p>
        <p>
            Anda dapat melihat kode proyek lengkap di <a href="https://github.com/username/repo">GitHub</a> dan dataset yang digunakan dapat diunduh dari <a href="https://mega.nz/file/HslSXS4a#7UBanJTjJqUl_2Z-JmAsreQYiJUKC-8UlZDR0rUsarw">sini</a>. Anda juga bisa mencoba menghasilkan gambar dengan mengunggah gambar ke dalam kolom yang disediakan ini:
        </p>
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Content
    uploaded_file = st.file_uploader("", type=["png", "jpg", "jpeg"], key="upload-section", accept_multiple_files=False, help="Allowed formats: png, jpg, jpeg")

    generated_image = None

    if uploaded_file is not None:
        img = Image.open(uploaded_file)
        img_base64 = image_to_base64(img)

        if st.button("Generate Image", key="generate-section"):
            generated_image = generate_image(generator)
            generated_image_pil = Image.fromarray(generated_image)
            generated_image_base64 = image_to_base64(generated_image_pil)
        
        st.markdown(
            f"""
            <div class='image-container'>
                <div>
                    <h3>Uploaded Image</h3>
                    <img src='data:image/png;base64,{img_base64}' class='img'>
                </div>
                <div>
                    <h3>Generated Image</h3>
                    {'<img src="data:image/png;base64,' + generated_image_base64 + '" class="img">' if generated_image is not None else ""}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Centering the download button
    if generated_image is not None:
        im_pil = Image.fromarray(generated_image)
        buf = io.BytesIO()
        im_pil.save(buf, format='PNG')
        byte_im = buf.getvalue()
        
        st.markdown(
            f"""
            <div class='download-button-container'>
                <a href='data:image/png;base64,{base64.b64encode(byte_im).decode()}' download='generated_image.png'>
                    <button class='download-button'>Download Image</button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

elif selected == "Tentang":
    about.show_about()
